import threading
import requests
from bs4 import BeautifulSoup

from src.parsers import parser

max_pages = 10
properties = []
remainingPages = True


def getPage(page):
    url = f'http://www.vargasinmobiliaria.com.uy/propiedades/Alquiler/U$S/Sin_precio_m%C3%ADnimo/Sin_precio_m%C3%A1ximo/Todos_los_tipos/Todas_las_zonas/P%C3%A1gina-{page}'
    print('Getting page: ' + str(page))
    response = requests.get(url)
    if response.status_code < 400:
        plain_txt = response.text
        soup = BeautifulSoup(plain_txt, features="html.parser")
        properties.extend(parser.parse(soup))
    else:
        print("Got to the end")


def main():
    page = 1
    print(f'Getting {max_pages} pages from Vargas')
    while (page <= max_pages and remainingPages):
        threading.Thread(target=getPage(page)).start()
        page += 1
    print(f'Se obtuvieron {len(properties)} propiedades')
    for property in properties:
        print(property.price)

if __name__ == '__main__':
    main()
