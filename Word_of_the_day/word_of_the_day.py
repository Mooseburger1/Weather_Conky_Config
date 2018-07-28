import requests
from bs4 import BeautifulSoup


site = requests.get('https://www.merriam-webster.com/word-of-the-day').text
soup = BeautifulSoup(site, 'lxml')


wotd = soup.h1.text
print(wotd.title())
