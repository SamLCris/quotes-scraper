import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import time
import json

BASE_URL = "https://quotes.toscrape.com/"

def scrape_page(url):
    '''scrapes a single page returns quotes and next page url if exists'''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for q in soup.select('.quote'):
        text = q.select_one('.text').get_text(strip=True)
        author = q.select_one('.author').get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.select('.tags .tag')]
        results.append({'text': text, 'author': author, 'tags': tags})
        
    #find next page link
    next_btn = soup.select_one('.pager .next a')
    next_url = urljoin(url, next_btn["href"]) if next_btn else None
    
    return results, next_url

def scrape_all(start_url=BASE_URL):
    '''follow pagination until no next page'''
    all_quotes = []
    url = start_url
    page = 1
    
    while url:
        print(f"Scraping page {page}: {url}")
        quotes, url = scrape_page(url)
        all_quotes.extend(quotes)
        page += 1
        time.sleep(0.5)
    
    return all_quotes

def save_json(quotes, path='quotes.json'):
    """ save quotes to json file """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)
        

if __name__ == "__main__":
    quotes = scrape_all()
    print(f"scraped {len(quotes)} quotes in total.")
    
    save_json(quotes)
    print("Quotes saved to quotes.json")

