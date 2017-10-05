from Prisliste import Prisliste
from Boesse import Boesse
from Trekning import Trekning
class Automat:
    def __init__(self, prislisteSize, boesseSize):
        self.prisliste = Prisliste(prislisteSize)
        self.boesse = Boesse(boesseSize)

    def spill(self, player):
        self.boesse.addCoin(player.betal())
        return Trekning()

    def settPris(self, currencyName, price):
        self.prisliste.settPris(currencyName, price)

    def erBoessenFull(self):
        return self.boesse.erFull()

    def finnPrisEttTall(self, currencyName):
        return self.prisliste.finnPrisEttTall(currencyName)

    def finnAntallTippetall(self, currencyName, value):
        return self.prisliste.finnAntallTippetall(currencyName, value)

    def finnPrislisten(self):
        return self.prisliste.finnPrislisten()

    def finnBoessen(self):
        return self.boesse.finnBoessen()

    def finnAntallRette(self, trekking, spiller):
        return trekking.finnAntallRette(spiller.tipping)
