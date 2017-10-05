from Mynt import Mynt


class Spiller:
    def __init__(self, tipping, currency, value):
        self.coin = Mynt(currency, value)
        self.tipping = tipping
        self.tipping.sort()

    def betal(self):
        tempCoin = self.coin
        self.coin = None
        return tempCoin

    def __str__(self):
        return 'Guess: {}\tCoin:\t{} {}'.format(self.tipping, self.coin.value, self.coin.currency)
