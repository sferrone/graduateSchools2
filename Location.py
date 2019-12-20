class Location:
    def __init__(self, country, city):
        self.SetCountry(country)
        self.SetCity(city)

    def SetCountry(self, country):
        self.country = country

    def SetCity(self, city):
        self.city = city
