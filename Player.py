from Coin import Coin


class Player:
    def __init__(self, guess, currency, value):
        self.coin = Mynt(currency, value)
        self.guess = guess
        self.guess.sort()

    def pay(self):
        tempCoin = self.coin
        self.coin = None
        return tempCoin

    def __str__(self):
        return 'Guess: {}\tCoin:\t{} {}'.format(self.guess, self.coin.value, self.coin.currency)
