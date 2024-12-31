from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import os
from typing import Any

class BaseConverter(ABC):
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    @abstractmethod
    def convert_content(self, title: str, content: str) -> Any:
        """Convert HTML content to the target format."""
        pass

    @abstractmethod
    def save_file(self, title: str, converted_content: Any, output_path: str):
        """Save the converted content to a file."""
        pass

    def process_page(self, title: str, content: str) -> str:
        """Process a single page and return the output path."""
        safe_title = "".join([c for c in title if c.isalnum() or c in (' ', '-', '_')]).rstrip()
        output_path = os.path.join(self.output_dir, f"{safe_title}.{self.file_extension}")
        
        converted_content = self.convert_content(title, content)
        self.save_file(title, converted_content, output_path)
        
        return output_path 