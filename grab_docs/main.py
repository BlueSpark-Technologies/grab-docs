from confluence_client import ConfluenceClient
from converters.html_converter import HTMLConverter
from converters.pdf_converter import PDFConverter
from converters.markdown_converter import MarkdownConverter
import argparse
import sys
import os
from typing import Dict, Type
from converters.base_converter import BaseConverter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from environment variables
CONFLUENCE_URL = os.getenv('CONFLUENCE_URL')
USERNAME = os.getenv('USERNAME')
API_TOKEN = os.getenv('API_TOKEN')

if not all([CONFLUENCE_URL, USERNAME, API_TOKEN]):
    print("Error: Missing required environment variables. Please check your .env file.")
    sys.exit(1)

# Available converters
CONVERTERS: Dict[str, Type[BaseConverter]] = {
    "html": HTMLConverter,
    "pdf": PDFConverter,
    "md": MarkdownConverter
}

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Convert Confluence space content to various formats.',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'space_key',
        help='The Confluence space key to convert (e.g., "PSE")'
    )
    
    parser.add_argument(
        'format',
        choices=list(CONVERTERS.keys()),
        help='Output format (html, pdf, md, or docx)'
    )
    
    parser.add_argument(
        '--output-dir',
        help='Custom output directory (default: <format>_docs)',
        default=None
    )

    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Set output directory
    output_dir = args.output_dir or f"{args.format}_docs"
    
    try:
        # Initialize the Confluence client
        client = ConfluenceClient(CONFLUENCE_URL, args.space_key, USERNAME, API_TOKEN)
        
        # Initialize the appropriate converter
        converter_class = CONVERTERS.get(args.format)
        if not converter_class:
            raise ValueError(f"Unsupported format: {args.format}")
        
        converter = converter_class(output_dir, client)
        
        # Fetch and convert pages
        print(f"Fetching pages from Confluence space '{args.space_key}'...")
        pages = client.get_all_pages()
        print(f"Found {len(pages)} pages.")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        for index, page in enumerate(pages, 1):
            title = page["title"]
            content = page["body"]["view"]["value"]
            
            print(f"Converting page {index}/{len(pages)}: {title}")
            try:
                output_path = converter.process_page(title, content)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Error converting page '{title}': {str(e)}")
                continue

        print(f"\nConversion complete! Files saved in: {output_dir}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 