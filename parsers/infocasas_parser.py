from domain import Property, Types


# This is the parser for Infocasas website
def parse(soup):
    properties = []

    for propertyItem in soup.findAll('div', {'class': 'propiedades-slider'}):
        imageItem = propertyItem.find('div', {'class': 'prop-img'})
        name = propertyItem.find('p', {'class': 'titulo'}).text
        price = imageItem.find('div', {'class': 'precio'}).text
        zone = imageItem.find('p', {'class': 'barrio'}).text
        link = propertyItem.find('a', {'title': name})
        images = []
        for imageContainer in imageItem.findAll('div', {'class': 'owl-item'}):
            print('entre')
            loading = imageContainer.find('img')['alt'] == 'loading'
            imageURL = ''
            if(loading):
                imageURL = imageContainer.find('div',
                                               {'class': 'item imagen'})
                ['data-img']
            else:
                imageURL = imageContainer.find('img')['src']
            print('This is the received url: {}'.format(imageURL))
            images.append(imageURL)
        if(link is not None):
            reference = "https://www.infocasas.com.uy" + link.get('href')
            property = Property.Property(name,
                                         price,
                                         zone,
                                         Types.Types.ALQUILER,
                                         images,
                                         reference)
            properties.append(property)
    return properties
