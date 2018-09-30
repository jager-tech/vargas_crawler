from bs4 import BeautifulSoup
from domain import Property

def parse(soup):
    for paragraph in soup.findAll('p', {'class':'titulo'}):
        name = paragraph.text
        link = soup.find('a', {'title': name})
        if(link is not None):
            href = "https://www.infocasas.com.uy" + link.get('href')
            print(href)
            property = Property(name)
            print(property)
