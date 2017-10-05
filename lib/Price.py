import math
class Price:
    def __init__(self, currency, price):
        self.currency = currency
        self.price = price

    def getAllowedGuesses(self, value):
        return math.floor(value / self.price)
