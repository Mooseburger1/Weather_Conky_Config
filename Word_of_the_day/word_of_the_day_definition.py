import requests
from bs4 import BeautifulSoup


site = requests.get('https://www.merriam-webster.com/word-of-the-day').text
soup = BeautifulSoup(site, 'lxml')


[cls.decompose() for cls in soup.findAll('p', class_ = 'blurb')]
[cls.decompose() for cls in soup.findAll('p', class_ = 'lead')]
defdiv = soup.find("div", {"class": "wod-definition-container"})
extract_alL_definitions = defdiv.findAll(['p','strong'])
definitions = [d.next_sibling.strip() for d in extract_alL_definitions if d.next_sibling.strip() not in ['','?']]

	

[print(d.title()) for d in definitions]
