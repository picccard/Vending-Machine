from Mynt import Mynt
class Boesse:
    def __init__(self, tabellSize):
        self.myntene = []
        self.antallMynter = 0
        self.tabellSize = tabellSize

    def erFull(self):
        if self.antallMynter >= self.tabellSize:
            return True
        return False

    def addCoin(self, coin):
        if not self.erFull():
            self.myntene.append(coin)
            self.antallMynter += 1
            return True
        return False

    def finnBoessen(self):
        answer = 'The box contains: '
        for mynt in self.myntene:
            answer += '\n{} {}'.format(mynt.currency, mynt.value)
        return answer
