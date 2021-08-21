class Purchase:
    """ class to house real estate data"""
    
    def __init__(self, street, city, zip, state, beds, baths, sqft, type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sqft = sqft
        self.type = type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            float(lookup['sqft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude'])
            )
