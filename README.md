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
```bash
git clone <repository-url>
cd confluence-exporter
```
2. Install dependencies using Poetry:
```bash
poetry install
```
3. Set environment variables:
```bash
export CONFLUENCE_URL="https://your-domain.atlassian.net"
export USERNAME="your.email@company.com"
export API_TOKEN="your-api-token"
```
To get an API token:

1. Log in to Atlassian account
2. Go to Account Settings > Security > Create and manage API tokens
3. Click "Create API token"
4. Give it a name and copy the token

## Usage

Run the tool using Poetry:
### Basic usage
```bash
poetry run python grab_docs/main.py SPACE-KEY FORMAT
```
### With custom output directory
```bash
poetry run python grab_docs/main.py SPACE-KEY FORMAT --output-dir custom_directory
```
### Export to HTML
```bash
poetry run python grab_docs/main.py PSE html
```
### Export to PDF
```bash
poetry run python grab_docs/main.py PSE pdf
```
### Export to Markdown with custom directory
```bash
poetry run python grab_docs/main.py PSE md --output-dir documentation
```