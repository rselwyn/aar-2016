class Stock:
    #basic info
    def __init__(self, datetime_object, price):
        self.date = datetime_object
        self.price = price

    def get_date(self):
        return self.date

    def get_price(self):
        return self.price
