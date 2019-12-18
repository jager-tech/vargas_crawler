class Property(object):
    def __init__(self, title, description, price, zone, types, images, reference, link):
        self.title = title
        self.description = description
        self.price = price
        self.zone = zone
        self.types = types
        self.images = images
        self.reference = reference
        self.link = link

    def __str__(self):
        prop = '"'
        prop += self.title.strip()
        prop += '","'
        prop += self.description.strip()
        prop += '","'
        prop += self.price.strip()
        prop += '","'
        prop += self.zone.strip()
        prop += '","'
        prop += str(self.type)
        prop += '","'
        prop += self.reference.strip()
        prop += '","'
        prop += self.link.strip()
        prop += '","'
        prop += '"['
        for image in self.images:
            prop += image
            prop += ','
        prop += ']"'
        prop += '\n'
        return prop
