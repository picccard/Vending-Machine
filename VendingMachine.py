from Pricelist import Pricelist
from CoinBox import CoinBox
from Raffle import Raffle
class VendingMachine:
    def __init__(self, pricelistSize, coinBoxSize):
        self.pricelist = Pricelist(pricelistSize)
        self.coinBox = CoinBox(coinBoxSize)

    def play(self, player):
        self.coinBox.addCoin(player.pay())
        return Raffle()

    def setPrice(self, currency, price):
        self.pricelist.setPrice(currency, price)

    def isCoinBoxFull(self):
        return self.coinBox.isFull()

    def getPriceForAGuess(self, currency):
        return self.pricelist.getPriceForAGuess(currency)

    def getAllowedGuesses(self, currency, value):
        return self.pricelist.getAllowedGuesses(currency, value)

    def getPricelist(self):
        return self.pricelist.getPricelist()

    def getCoinBox(self):
        return self.coinBox.getCoinBox()

    def getMatches(self, raffle, player):
        return raffle.getMatches(player.guess)
