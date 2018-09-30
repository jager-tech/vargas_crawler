import requests
from parsers import vargas_parser
from bs4 import BeautifulSoup
import threading

max_pages = 1
def getPage():
    page = 1
    while page <= max_pages:
        if(page == 1):
            url_suffix = ''
        else:
            url_suffix = '("pagina" +str(page))'
        url = 'https://www.infocasas.com.uy/venta/inmuebles/montevideo/' + url_suffix
        print('Getting: ' + url)
        source_code = requests.get(url)
        plain_txt = source_code.text
        soup = BeautifulSoup(plain_txt)
        vargas_parser.parse(soup)
        page += 1

def main():
    threading.Thread(target=getPage).start()

if __name__ == '__main__':
    main()
