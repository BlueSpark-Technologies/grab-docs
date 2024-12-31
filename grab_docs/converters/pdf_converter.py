from .base_converter import BaseConverter
from bs4 import BeautifulSoup, Tag
import os
import urllib.parse
import base64
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    Image, ListFlowable, ListItem, PageBreak
)
from typing import List, Any, Dict, Tuple

class PDFConverter(BaseConverter):
    file_extension = "pdf"

    def __init__(self, output_dir: str, confluence_client):
        super().__init__(output_dir)
        self.confluence_client = confluence_client
        self.images_dir = os.path.join(output_dir, 'images')
        os.makedirs(self.images_dir, exist_ok=True)
        
        # Define information panel styles
        self.info_styles = {
            'note': {'bgcolor': colors.HexColor('#EAE6FF'), 'textcolor': colors.black},
            'info': {'bgcolor': colors.HexColor('#DEEBFF'), 'textcolor': colors.black},
            'tip': {'bgcolor': colors.HexColor('#E3FCEF'), 'textcolor': colors.black},
            'warning': {'bgcolor': colors.HexColor('#FFEDEB'), 'textcolor': colors.black}
        }
        
        # Create styles once during initialization
        self.styles = self.create_styles()

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
            
            if not os.path.exists(local_path):
                image_content = self.confluence_client.download_attachment(img_url)
                with open(local_path, 'wb') as f:
                    f.write(image_content)
                    
            return local_path
        except Exception as e:
            print(f"Error downloading image {img_url}: {str(e)}")
            return None

    def create_styles(self) -> Dict[str, ParagraphStyle]:
        """Create custom styles for PDF elements."""
        styles = getSampleStyleSheet()
        
        # Custom heading styles
        for i in range(1, 7):
            style_name = f'CustomHeading{i}'
            if style_name not in styles:
                styles.add(ParagraphStyle(
                    name=style_name,
                    parent=styles['Heading1'],
                    fontSize=24-(i*2),
                    spaceAfter=20,
                    spaceBefore=20
                ))
        
        # Code block style
        if 'CustomCode' not in styles:
            styles.add(ParagraphStyle(
                name='CustomCode',
                parent=styles['Code'],
                fontSize=9,
                fontName='Courier',
                spaceAfter=12,
                spaceBefore=12,
                backColor=colors.HexColor('#F4F5F7')
            ))
        
        # Info panel style
        if 'CustomInfoPanel' not in styles:
            styles.add(ParagraphStyle(
                name='CustomInfoPanel',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=12,
                spaceBefore=12,
                borderPadding=10,
                borderWidth=1,
                borderColor=colors.grey
            ))
        
        return styles

    def convert_table(self, table: Tag, available_width: float) -> Table:
        """Convert HTML table to ReportLab Table."""
        data = []
        
        # Process headers
        headers = []
        header_row = table.find('tr')
        if header_row:
            for th in header_row.find_all(['th', 'td']):
                headers.append(Paragraph(th.get_text().strip(), self.styles['Normal']))
        
        if headers:
            data.append(headers)
        
        # Process rows
        rows = table.find_all('tr')[1:] if headers else table.find_all('tr')
        for row in rows:
            cells = []
            for cell in row.find_all(['td', 'th']):
                cells.append(Paragraph(cell.get_text().strip(), self.styles['Normal']))
            if cells:
                data.append(cells)
        
        # Calculate column widths
        num_cols = max(len(row) for row in data)
        col_width = available_width / num_cols
        
        # Create table
        table = Table(data, colWidths=[col_width] * num_cols)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F4F5F7')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        return table

    def convert_info_panel(self, panel: Tag) -> List[Any]:
        """Convert Confluence info panel to PDF elements."""
        panel_type = None
        for cls in panel.get('class', []):
            if 'confluence-information-macro-' in cls:
                panel_type = cls.replace('confluence-information-macro-', '')
                break
        
        style = self.info_styles.get(panel_type, self.info_styles['info'])
        content = panel.get_text().strip()
        
        # Create panel style name with unique identifier
        panel_style_name = f'CustomInfoPanel_{panel_type}'
        if panel_style_name not in self.styles:
            self.styles.add(ParagraphStyle(
                panel_style_name,
                parent=self.styles['CustomInfoPanel'],
                backColor=style['bgcolor'],
                textColor=style['textcolor']
            ))
        
        return [
            Paragraph(content, self.styles[panel_style_name]),
            Spacer(1, 12)
        ]

    def convert_content(self, title: str, content: str) -> List[Any]:
        """Convert HTML content to PDF elements."""
        soup = BeautifulSoup(content, 'html.parser')
        elements = []
        
        # Add title
        elements.append(Paragraph(title, self.styles['CustomHeading1']))
        elements.append(Spacer(1, 30))
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'table', 'div', 'pre', 'img']):
            try:
                if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    level = int(element.name[1])
                    elements.append(Paragraph(element.get_text().strip(), self.styles[f'CustomHeading{level}']))
                    elements.append(Spacer(1, 12))
                
                elif element.name == 'p':
                    text = element.get_text().strip()
                    if text:
                        elements.append(Paragraph(text, self.styles['Normal']))
                        elements.append(Spacer(1, 12))
                
                elif element.name in ['ul', 'ol']:
                    items = []
                    for li in element.find_all('li', recursive=False):
                        items.append(ListItem(Paragraph(li.get_text().strip(), self.styles['Normal'])))
                    elements.append(ListFlowable(
                        items,
                        bulletType='bullet' if element.name == 'ul' else '1',
                        leftIndent=20,
                        spaceBefore=10,
                        spaceAfter=10
                    ))
                
                elif element.name == 'table':
                    elements.append(self.convert_table(element, 6.5*inch))
                    elements.append(Spacer(1, 12))
                
                elif element.name == 'div' and 'confluence-information-macro' in element.get('class', []):
                    elements.extend(self.convert_info_panel(element))
                
                elif element.name == 'pre':
                    code = element.get_text().strip()
                    elements.append(Paragraph(code, self.styles['CustomCode']))
                    elements.append(Spacer(1, 12))
                
                elif element.name == 'img':
                    src = element.get('src', '')
                    if src:
                        if not src.startswith(('http://', 'https://')):
                            src = urllib.parse.urljoin(self.confluence_client.base_url, src)
                        local_path = self.download_image(src, title)
                        if local_path:
                            img = Image(local_path)
                            available_width = 6.5 * inch
                            if img.imageWidth > available_width:
                                ratio = available_width / img.imageWidth
                                img.drawWidth = available_width
                                img.drawHeight = img.imageHeight * ratio
                            elements.append(img)
                            elements.append(Spacer(1, 12))
            
            except Exception as e:
                print(f"Error converting element {element.name}: {str(e)}")
                elements.append(Paragraph(f"Error converting {element.name} element", self.styles['Normal']))
                elements.append(Spacer(1, 12))
        
        return elements

    def save_file(self, title: str, elements: List[Any], output_path: str):
        """Save the PDF content to a file."""
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        try:
            doc.build(elements)
        except Exception as e:
            print(f"Error building PDF for {title}: {str(e)}")
            # Fallback to simple version
            doc.build([
                Paragraph(title, self.styles['CustomHeading1']),
                Spacer(1, 30),
                Paragraph("Error creating PDF. Content too complex.", self.styles['Normal'])
            ]) 