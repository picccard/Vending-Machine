from Price import Price


class Pricelist:
    def __init__(self, tableSize):
        self.prices = [0] * tableSize
        self.numberOfPrices = 0

    def setPrice(self, currency, price):
        self.prices.append(Price(currency, price))
        self.numberOfPrices += 1

    def getAllowedGuesses(self, currency, value):
        for price in self.prices:
            if price.currency == currency:
                return price.getAllowedGuesses(value)
        return 0

    def getPriceForAGuess(self, currency):
        for price in self.prices:
            if price.currency == currency:
                return price.price
        return None

    def getPricelist(self):
        answer = '~ Pricelist:\n'
        for price in self.prices:
            answer += '{}\t{}\n'.format(price.currency, "{0:.2f}".format(price.price))
        return answer
