from bs4 import BeautifulSoup
import requests

def fetch_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    return title

def fetch_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    base_url = url.split('//')[1].split('/')[0]  # Extract base URL
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith(('http://', 'https://')) and base_url not in link:
            links.append(link)
    return links