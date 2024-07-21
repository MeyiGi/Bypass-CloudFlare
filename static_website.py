import requests
from bs4 import BeautifulSoup

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'YOUR_API_KEY',
      'url': 'https://www.paperpapers.com/', ## Cloudflare protected website 
      'bypass': 'cloudflare_level_1',
  },
)

soup = BeautifulSoup(response.text, "lxml")

print('Title: ', soup.title)