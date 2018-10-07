class Location(object)
    lon
    lat

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def __str__(self):
        return '(%g, %g)' % (self.lon, self.lat)
