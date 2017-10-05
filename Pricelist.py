from Pris import Pris


class Prisliste:
    def __init__(self, priseneStr):
        self.prisene = []
        self.antallPriser = 0
        self.antallPriserSize = priseneStr

    def settPris(self, currencyName, price):
        self.prisene.append(Pris(currencyName, price))
        self.antallPriser += 1

    def finnAntallTippetall(self, currencyName, value):
        for pris in self.prisene:
            if pris.currencyName == currencyName:
                return pris.finnAntallTippetall(value)

    def finnPrisEttTall(self, currencyName):
        for pris in self.prisene:
            if pris.currencyName == currencyName:
                return pris.price
        return -1

    def finnPrislisten(self):
        answer = '~ Pricelist:\n'
        for pris in self.prisene:
            answer += '{}\t{}\n'.format(pris.currencyName, "{0:.2f}".format(pris.price))
            # if pris.currencyName == 'DONG':
            #     # answer += '\t( ͡° ͜ʖ ͡°)\n'
            # else:
            #     answer += '\n'
        return answer
