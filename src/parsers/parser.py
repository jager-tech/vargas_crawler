from domain import Property

from src.domain import Types


# This is the parser for Vargas website
def parse(soup):
    properties = []

    for propertyItem in soup.findAll('div', {'class': 'propiedad'}):
        image_url = propertyItem.find('div', {'class': 'imagen'})
        name = propertyItem.find('h4', {'class': 'titulo'}).text
        price = propertyItem.find('div', {'class': 'precio'}).text
        #location = propertyItem.find('div', {'class': 'ubicacion tright'}).text
        link = propertyItem.find('a', {'class': 'link'})
        images = [image_url]
        if link is not None:
            reference = "https://www.vargasinmobiliaria.com.uy" + link.get('href')
            property = Property.Property(name,
                                         price,
                                         "",
                                         Types.Types.ALQUILER,
                                         images,
                                         reference)
            properties.append(property)
    return properties
