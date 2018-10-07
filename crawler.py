import requests
from parsers import infocasas_parser
from bs4 import BeautifulSoup
import threading

max_pages = 1
properties = []
remainingPages = True


def getPage(page):
    if(page == 1):
        url_suffix = '?&ordenListado=3'
    else:
        url_suffix = '("pagina" +str(page))?&ordenListado=3'
    url = 'https://www.infocasas.com.uy/alquiler/inmuebles/montevideo/' + \
        url_suffix
    print('Getting page: ' + str(page))
    response = requests.get(url)
    if (response.status_code < 400):
        plain_txt = response.text
        soup = BeautifulSoup(plain_txt, features="html.parser")
        properties.extend(infocasas_parser.parse(soup))
    else:
        remainingPages = False
        print("Got to the end")


def main():
    page = 1
    print('Getting {} pages from InfoCasas'.format(str(max_pages)))
    while (page <= max_pages and remainingPages):
        threading.Thread(target=getPage(page)).start()
        page += 1
    print('Se obtuvieron {} propiedades'.format(len(properties)))


if __name__ == '__main__':
    main()
