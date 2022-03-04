import requests
from bs4 import BeautifulSoup

response = requests.get("https://bbc.co.uk/news")
soup = BeautifulSoup(response.text, 'html.parser')
breaking = soup.find('h3', attrs={"class": "gs-c-promo-heading__title gel-canon-bold nw-o-link-split__text"})

print("Top headline from BBC News: " + breaking.text)
