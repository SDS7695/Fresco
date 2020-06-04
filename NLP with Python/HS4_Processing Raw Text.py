# TASK 1
from bs4 import BeautifulSoup as bs
import requests
html_content = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)#References').content
soup = bs(html_content, 'html.parser')
n_links = [item['href'] for item in soup.select('.reflist a')]
print(len(n_links))

# TASK 2
table = soup.find("table", { "class" : 'wikitable'})
rows = table.find_all('tr')
rows = rows[1:]
for row in rows:
  cols = row.find_all('td')
  print(cols[0].get_text())