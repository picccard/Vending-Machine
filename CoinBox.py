from Coin import Coin
class CoinBox:
    def __init__(self, tableSize):
        self.coins = []
        self.numberOfCoins = 0
        self.maximumCoins = tableSize

    def isFull(self):
        if self.numberOfCoins >= self.maximumCoins:
            return True
        return False

    def addCoin(self, coin):
        if not self.isFull():
            self.coins.append(coin)
            self.numberOfCoins += 1
            return True
        return False

    def getCoinBox(self):
        answer = 'The box contains: '
        for coin in self.coins:
            answer += '\n{} {}'.format(coin.currency, coin.value)
        return answer
