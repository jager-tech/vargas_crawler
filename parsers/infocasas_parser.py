from bs4 import BeautifulSoup
from domain import Property, Zones, Types

# This is the parser for Infocasas website
def parse(soup):
    properties = []

    for propertyItem in soup.findAll('div', {'class':'propiedades-slider'}):
        imageItem = propertyItem.find('div', {'class':'prop-img'})
        name = propertyItem.find('p', {'class': 'titulo'}).text
        price = imageItem.find('div', {'class': 'precio'}).text
        zone = imageItem.find('p', {'class': 'barrio'}).text
        link = propertyItem.find('a', {'title': name})
        if(link is not None):
            reference = "https://www.infocasas.com.uy" + link.get('href')
            property = Property.Property(name, price, zone, Types.Types.ALQUILER, reference)
            properties.append(property)
    return properties
