import requests
from bs4 import BeautifulSoup, NavigableString


# This is the parser for Vargas website
def parse(soup):
    properties = []
    prop_count = 1
    properties_html = soup.findAll('div', {'class': 'propiedad'})
    for property_item in properties_html:
        property_url = property_item.find('a', {'class': 'link'})['href']
        if property_url:
            response = requests.get(f'http://www.vargasinmobiliaria.com.uy{property_url}')
            if response.status_code < 400:
                plain_txt = response.text
                property_soup = BeautifulSoup(plain_txt, 'html5lib')
                property = process_property(property_soup, property_url)
                print(f'Se proceso la propiedad {prop_count} de {len(properties_html)}.')
                properties.append(property)
                prop_count += 1
    return properties


def process_property(property_soup, property_url):
    image_url = property_soup.find('div', {'class': 'imagen'})['style'].split('(')[1].replace(')','')
    images = [image_url]
    reference = property_soup.find('div', {'class': 'titulo_seccion'}).find('strong').text

    old_format = len(property_soup.find('div', {'class': 'contenido ficha'}).contents) > 5

    if old_format:
        description = property_soup.find('div', {'class': 'contenido ficha'}).contents[11].text
        title = property_soup.find('div', {'class': 'info_full'}).contents[5].text
        quick_desc = property_soup.find('div', {'class': 'info_full'}).contents[1].text.split('\n')
        if len(quick_desc) > 7:
            price = quick_desc[7].strip()
        else:
            price = quick_desc[3].strip()

    else:
        contents = property_soup.find('div', {'class': 'col_left'}).contents
        description = find_description(contents)
        title = property_soup.find('div', {'class': 'titulo_2'}).text
        price = property_soup.find('div', {'class': 'titulo_1'}).text.strip()
        for image in property_soup.findAll('div', {'class': 'foto'}):
            img_url = image.find('a').attrs['href']
            images.append(img_url)
    return {
        "title": title,
        "description": description,
        "price": price,
        "zone": "",
        "types": "ALQUILER",
        "images": images,
        "reference": reference,
        "link": f'http://www.vargasinmobiliaria.com.uy{property_url}'
    }


def find_description(contents):
    pos = 0
    for item in contents:
        if (not isinstance(item, NavigableString)) and item.text == 'DESCRIPCIÃN':
            return contents[pos + 4].text
        pos += 1
    return ''