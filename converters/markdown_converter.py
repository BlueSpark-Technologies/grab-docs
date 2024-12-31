from .base_converter import BaseConverter
from bs4 import BeautifulSoup, Tag
import os
import urllib.parse
import base64
from typing import Optional, Dict, Any

class MarkdownConverter(BaseConverter):
    file_extension = "md"

    def __init__(self, output_dir: str, confluence_client):
        super().__init__(output_dir)
        self.confluence_client = confluence_client
        self.images_dir = os.path.join(output_dir, 'images')
        os.makedirs(self.images_dir, exist_ok=True)
        
        # Define information panel emojis
        self.info_emojis = {
            'note': '📝',
            'info': 'ℹ️',
            'tip': '💡',
            'warning': '⚠️',
            'error': '❌'
        }

    def download_image(self, img_url: str, page_title: str) -> str:
        """Download image and return local path."""
        try:
            page_images_dir = os.path.join(self.images_dir, page_title)
            os.makedirs(page_images_dir, exist_ok=True)
            
            parsed_url = urllib.parse.urlparse(img_url)
            img_filename = os.path.basename(parsed_url.path)
            if not img_filename:
                img_filename = f"image_{base64.urlsafe_b64encode(img_url.encode()).decode()[:10]}.png"
            
            local_path = os.path.join(page_images_dir, img_filename)
            relative_path = os.path.join('images', page_title, img_filename)
            
            if not os.path.exists(local_path):
                image_content = self.confluence_client.download_attachment(img_url)
                with open(local_path, 'wb') as f:
                    f.write(image_content)
                    
            return relative_path
        except Exception as e:
            print(f"Error downloading image {img_url}: {str(e)}")
            return img_url

    def convert_table(self, table: Tag) -> str:
        """Convert HTML table to Markdown table."""
        markdown_table = []
        
        # Process headers
        headers = []
        header_row = table.find('tr')
        if header_row:
            for th in header_row.find_all(['th', 'td']):
                headers.append(th.get_text().strip())
        
        if not headers and table.find('tr'):
            # If no headers found, use first row as header
            for td in table.find('tr').find_all('td'):
                headers.append(td.get_text().strip())
        
        # Add headers to table
        if headers:
            markdown_table.append('| ' + ' | '.join(headers) + ' |')
            markdown_table.append('|' + '|'.join(['---' for _ in headers]) + '|')
        
        # Process rows
        rows = table.find_all('tr')[1:] if headers else table.find_all('tr')
        for row in rows:
            cells = []
            for cell in row.find_all(['td', 'th']):
                # Replace newlines with spaces in cells
                cell_text = cell.get_text().strip().replace('\n', ' ')
                cells.append(cell_text)
            
            # Pad row if necessary
            while len(cells) < len(headers):
                cells.append('')
            
            markdown_table.append('| ' + ' | '.join(cells) + ' |')
        
        return '\n'.join(markdown_table) + '\n\n'

    def convert_info_panel(self, panel: Tag) -> str:
        """Convert Confluence info panel to Markdown blockquote with emoji."""
        panel_type = None
        for cls in panel.get('class', []):
            if 'confluence-information-macro-' in cls:
                panel_type = cls.replace('confluence-information-macro-', '')
                break
        
        emoji = self.info_emojis.get(panel_type, 'ℹ️')
        content = panel.get_text().strip()
        
        return f"> {emoji} **{panel_type.upper() if panel_type else 'INFO'}**\n> \n> {content}\n\n"

    def convert_code_block(self, code_block: Tag) -> str:
        """Convert code block to Markdown format."""
        language = ''
        for cls in code_block.get('class', []):
            if 'language-' in cls:
                language = cls.replace('language-', '')
                break
        
        code = code_block.get_text().strip()
        return f"```{language}\n{code}\n```\n\n"

    def convert_content(self, title: str, content: str) -> str:
        """Convert HTML content to Markdown format."""
        soup = BeautifulSoup(content, 'html.parser')
        markdown_content = []
        
        # Add title
        markdown_content.append(f"# {title}\n\n")
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'table', 'div', 'pre', 'img']):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(element.name[1])
                markdown_content.append(f"{'#' * level} {element.get_text().strip()}\n\n")
            
            elif element.name == 'p':
                text = element.get_text().strip()
                if text:
                    # Handle text formatting
                    for strong in element.find_all('strong'):
                        text = text.replace(str(strong), f"**{strong.get_text()}**")
                    for em in element.find_all('em'):
                        text = text.replace(str(em), f"*{em.get_text()}*")
                    markdown_content.append(f"{text}\n\n")
            
            elif element.name == 'ul':
                for li in element.find_all('li', recursive=False):
                    markdown_content.append(f"* {li.get_text().strip()}\n")
                markdown_content.append('\n')
            
            elif element.name == 'ol':
                for i, li in enumerate(element.find_all('li', recursive=False), 1):
                    markdown_content.append(f"{i}. {li.get_text().strip()}\n")
                markdown_content.append('\n')
            
            elif element.name == 'table':
                markdown_content.append(self.convert_table(element))
            
            elif element.name == 'div' and 'confluence-information-macro' in element.get('class', []):
                markdown_content.append(self.convert_info_panel(element))
            
            elif element.name == 'pre':
                markdown_content.append(self.convert_code_block(element))
            
            elif element.name == 'img':
                src = element.get('src', '')
                alt = element.get('alt', '')
                if src:
                    if not src.startswith(('http://', 'https://')):
                        src = urllib.parse.urljoin(self.confluence_client.base_url, src)
                    local_path = self.download_image(src, title)
                    markdown_content.append(f"![{alt}]({local_path})\n\n")

        return ''.join(markdown_content)

    def save_file(self, title: str, converted_content: str, output_path: str):
        """Save the Markdown content to a file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted_content) 