class Property(object):
    def __init__(self, name, price, zone, type, images, reference):
        self.name = name
        self.price = price
        self.zone = zone
        self.type = type
        self.images = images
        self.reference = reference

    def __str__(self):
        rep = "Property:\n"
        rep += "name: " + self.name.encode('utf-8').strip() + "\n"
        rep += "price: " + self.price.encode('utf-8').strip() + "\n"
        rep += "zone: " + self.zone.encode('utf-8').strip() + "\n"
        rep += "type: " + str(self.type).encode('utf-8').strip() + "\n"
        rep += "images: " + \
            (', '.join([str(image).encode('utf-8') for image in self.images]))\
            + "\n"
        rep += "reference: " + self.reference.encode('utf-8').strip() + "\n"
        return rep
