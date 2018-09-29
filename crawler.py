import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
        if(page == 1):
            url_suffix = ''
        else:
            url_suffix = '("pagina" +str(page))'
        url = 'https://www.infocasas.com.uy/venta/inmuebles/montevideo/' + url_suffix
        source_code = requests.get(url)
        plain_txt = source_code.text
        soup = BeautifulSoup(plain_txt)
        parser(soup)
        page += 1


def parser(soup):
    for paragraph in soup.findAll('p', {'class':'titulo'}):
        name = paragraph.text
        link = soup.find('a', {'title': name})
        if(link is not None):
            href = "https://www.infocasas.com.uy" + link.get('href')
            print(href)
            print(name)


spider(1)
