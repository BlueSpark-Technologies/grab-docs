import requests
from requests.auth import HTTPBasicAuth
import os
import time
from typing import List, Dict, Any

class ConfluenceClient:
    def __init__(self, base_url: str, space_key: str, username: str, api_token: str):
        self.base_url = base_url
        self.space_key = space_key
        self.auth = HTTPBasicAuth(username, api_token)
        
    def get_all_pages(self) -> List[Dict[str, Any]]:
        """Fetch all pages from a Confluence space."""
        url = f"{self.base_url}/wiki/rest/api/space/{self.space_key}/content"
        pages = []
        start = 0
        limit = 50

        while True:
            response = requests.get(
                url,
                params={"start": start, "limit": limit, "expand": "body.view"},
                auth=self.auth
            )
            response.raise_for_status()
            data = response.json()
            pages.extend(data['page']["results"])

            if "next" not in data["_links"]:
                break

            start += limit
            time.sleep(1)  # Be nice to the API

        return pages

    def download_attachment(self, url: str) -> bytes:
        """Download an attachment from Confluence."""
        response = requests.get(url, auth=self.auth, stream=True)
        response.raise_for_status()
        return response.content

    def get_safe_filename(self, title: str) -> str:
        """Convert a title to a safe filename."""
        return "".join([c for c in title if c.isalnum() or c in (' ', '-', '_')]).rstrip() 