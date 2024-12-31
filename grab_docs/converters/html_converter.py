from .base_converter import BaseConverter
from bs4 import BeautifulSoup
import os
import urllib.parse
import base64

class HTMLConverter(BaseConverter):
    file_extension = "html"

    def __init__(self, output_dir: str, confluence_client):
        super().__init__(output_dir)
        self.confluence_client = confluence_client
        self.images_dir = os.path.join(output_dir, 'images')
        os.makedirs(self.images_dir, exist_ok=True)

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

    def convert_content(self, title: str, content: str) -> str:
        """Convert HTML content preserving images and styling."""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Process images
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src:
                if not src.startswith(('http://', 'https://')):
                    src = urllib.parse.urljoin(self.confluence_client.base_url, src)
                local_path = self.download_image(src, title)
                img['src'] = local_path
        
        # Preserve Confluence classes and structure
        for element in soup.find_all(['div', 'span', 'table', 'tr', 'td', 'th']):
            if 'class' in element.attrs:
                element['class'] = ' '.join(element['class'])
            if element.name == 'table':
                if 'class' not in element.attrs:
                    element['class'] = 'confluence-table'
        
        return self.get_html_template(title, str(soup))

    def get_html_template(self, title: str, content: str) -> str:
        """Return the HTML template with complete Confluence styling."""
        return f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
            <style>
                /* Base styles */
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
                    line-height: 1.6;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                    color: #172B4D;
                }}

                /* Headings */
                h1, h2, h3, h4, h5, h6 {{
                    color: #172B4D;
                    margin-top: 24px;
                    margin-bottom: 16px;
                    font-weight: 500;
                }}
                h1 {{ font-size: 2.0em; }}
                h2 {{ font-size: 1.5em; }}
                h3 {{ font-size: 1.25em; }}

                /* Tables */
                .confluence-table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                .confluence-table th,
                .confluence-table td {{
                    border: 1px solid #DFE1E6;
                    padding: 8px 12px;
                    text-align: left;
                }}
                .confluence-table th {{
                    background-color: #F4F5F7;
                    font-weight: bold;
                }}
                .confluence-table tr:nth-child(even) {{
                    background-color: #FAFBFC;
                }}
                .confluence-table tr:hover {{
                    background-color: #F4F5F7;
                }}

                /* Images */
                img {{
                    max-width: 100%;
                    height: auto;
                    margin: 10px 0;
                }}

                /* Lists */
                ul, ol {{
                    margin: 10px 0;
                    padding-left: 30px;
                }}
                li {{
                    margin: 5px 0;
                }}

                /* Information panels */
                .confluence-information-macro {{
                    border-radius: 3px;
                    margin: 10px 0;
                    padding: 12px;
                }}
                .confluence-information-macro-note {{
                    background-color: #EAE6FF;
                    border: 1px solid #998DD9;
                }}
                .confluence-information-macro-tip {{
                    background-color: #E3FCEF;
                    border: 1px solid #57D9A3;
                }}
                .confluence-information-macro-warning {{
                    background-color: #FFEDEB;
                    border: 1px solid #FF5630;
                }}
                .confluence-information-macro-information {{
                    background-color: #DEEBFF;
                    border: 1px solid #2684FF;
                }}

                /* Code blocks */
                .code-block {{
                    background: #F4F5F7;
                    border: 1px solid #DFE1E6;
                    border-radius: 3px;
                    padding: 10px;
                    font-family: Monaco, Consolas, "Courier New", monospace;
                    font-size: 0.9em;
                    overflow-x: auto;
                    white-space: pre-wrap;
                }}

                /* Expand/Collapse sections */
                .expand-container {{
                    border: 1px solid #DFE1E6;
                    border-radius: 3px;
                    margin: 10px 0;
                }}
                .expand-header {{
                    background: #F4F5F7;
                    padding: 10px;
                    cursor: pointer;
                }}
                .expand-content {{
                    padding: 10px;
                }}

                /* Status macros */
                .status-macro {{
                    display: inline-block;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-size: 0.9em;
                    font-weight: bold;
                }}
                .status-macro.status-green {{
                    background-color: #E3FCEF;
                    color: #006644;
                }}
                .status-macro.status-red {{
                    background-color: #FFEDEB;
                    color: #BF2600;
                }}
                .status-macro.status-yellow {{
                    background-color: #FFF7D6;
                    color: #172B4D;
                }}

                /* Links */
                a {{
                    color: #0052CC;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}

                /* Task lists */
                .task-list {{
                    list-style-type: none;
                    padding-left: 0;
                }}
                .task-list-item {{
                    margin: 5px 0;
                    display: flex;
                    align-items: center;
                }}
                .task-list-item input[type="checkbox"] {{
                    margin-right: 10px;
                }}
            </style>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    // Handle expand/collapse sections
                    document.querySelectorAll('.expand-header').forEach(function(header) {{
                        header.addEventListener('click', function() {{
                            const content = this.nextElementSibling;
                            content.style.display = content.style.display === 'none' ? 'block' : 'none';
                        }});
                    }});
                }});
            </script>
        </head>
        <body>
            <h1>{title}</h1>
            {content}
        </body>
        </html>"""

    def save_file(self, title: str, converted_content: str, output_path: str):
        """Save the HTML content to a file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted_content) 