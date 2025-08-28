# Quotes Scraper

A beginner-friendly Python web scraper that collects quotes, authors, and tags from [quotes.toscrape.com](https://quotes.toscrape.com/).

## Features
- Scrapes all 10 pages (pagination supported)
- Exports results to `quotes.csv` and `quotes.json`
- Tags stored as a `|`-separated string in CSV
- Uses `requests` + `BeautifulSoup`

## Usage

```bash
pip install requests beautifulsoup4
python quotes_scraper.py
