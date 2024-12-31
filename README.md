# Confluence Content Exporter

A Python tool to export Confluence spaces to various formats (HTML, PDF, Markdown).

## Features

- Export entire Confluence spaces
- Multiple output formats supported:
  - HTML (with preserved styling and images)
  - PDF (with formatting and layout)
  - Markdown (with images and basic formatting)
- Maintains original formatting and structure
- Downloads and preserves images locally
- Handles tables, code blocks, and special Confluence macros

## Prerequisites

- Python 3.7 or higher
- [Poetry](https://python-poetry.org/docs/#installation) (Python dependency manager)

## Installation

1. Clone the repository:
git clone <repository-url>
cd confluence-exporter
:
bash
poetry install
:
env
CONFLUENCE_URL="https://your-domain.atlassian.net"
USERNAME="your.email@company.com"
API_TOKEN="your-api-token"

To get an API token:
1. Log in to Atlassian account
2. Go to Account Settings > Security > Create and manage API tokens
3. Click "Create API token"
4. Give it a name and copy the token

## Usage

Run the tool using Poetry:
Basic usage
poetry run python main.py SPACE-KEY FORMAT
With custom output directory
poetry run python main.py SPACE-KEY FORMAT --output-dir custom_directory

Export to HTML
poetry run python main.py PSE html
Export to PDF
poetry run python main.py PSE pdf
Export to Markdown with custom directory
poetry run python main.py PSE md --output-dir documentation