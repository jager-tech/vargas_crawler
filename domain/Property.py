class Property(object):
    def __init__(self, name, price, zone, type, reference):
        self.name = name
        self.price = price
        self.zone = zone
        self.type = type
        self.reference = reference


    def __str__(self):
        rep = "Property:\n"
        rep += "name: " + self.name.encode('utf-8').strip() + "\n"
        rep += "price: " + self.price.encode('utf-8').strip() + "\n"
        rep += "zone: " + self.zone.encode('utf-8').strip() + "\n"
        rep += "type: " + str(self.type).encode('utf-8').strip() + "\n"
        rep += "reference: " + self.reference.encode('utf-8').strip() + "\n"
        return rep
