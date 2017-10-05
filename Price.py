import math
class Pris:
    def __init__(self, currencyName, price):
        self.currencyName = currencyName
        self.price = price

    def finnAntallTippetall(self, value):
        return math.floor(value / self.price)
