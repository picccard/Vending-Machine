from Mynt import Mynt
from Spiller import Spiller
from Boesse import Boesse
from Pris import Pris
from Prisliste import Prisliste
from Trekning import Trekning
from Automat import Automat
import os, sys
#import Mynt, Spiller, Boesse, Pris, Prisliste, Trekning, Automat, os, sys

class Automattest:
    @staticmethod
    def somethingWrong():
        print('You typed something illegal...')
        input('Press enter to try again. ')
        Automattest.clear()

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def main():
        print('Round is starting')
        print('-----------------')
        # Creates a vending machine
        automaten = Automat(200, 5)

        # Sets the price for these currencys: EUR, USD, NOK, DONG
        CHOISES = ['EUR', 'USD', 'NOK', 'DONG']
        PRICES = [0.12, 0.16, 1.00, 0.08]
        for i in range(len(CHOISES)):
            automaten.settPris(CHOISES[i], PRICES[i])

        # Runs until the box is full
        while not automaten.erBoessenFull():
            # Reads your coin
            # Loop until acceptable valuta chosen
            valuta = ''
            while valuta not in CHOISES:
                valuta = input('\n' + automaten.finnPrislisten() +
                               '\n\n' + 'What currency is your coin? ').upper()
                if valuta not in CHOISES:
                    Automattest.somethingWrong()
            # Loop until verdi is a float
            verdi = ''
            while not isinstance(verdi, float):
                verdiStr = input('Each number you guess will cost ' + str(automaten.finnPrisEttTall(valuta))
                                 + ' {}'.format(str(valuta)) + '\n\nYour coins value in ' + valuta + ': ')
                try:
                    verdi = float(verdiStr)
                except ValueError as ex:
                    Automattest.somethingWrong()

            # Reads your selected numbers to guess
            antallTippetall = automaten.finnAntallTippetall(valuta, verdi)
            tippingen = [0] * antallTippetall
            for i in range(antallTippetall):
                while tippingen[i] not in range(1, 10):
                    try:
                        tippingen[i] = int(input('Chose a number between 1 and 9: '))
                        if tippingen[i] not in range(1, 10):
                            Automattest.somethingWrong()
                    except ValueError as ex:
                        Automattest.somethingWrong()

            # Gets ready to display results
            Automattest.clear()
            print('--------------------')
            print('|  Round summmary  |')
            print('--------------------')

            # Creates a player and displays player info
            spilleren = Spiller(tippingen, valuta, verdi)
            print('Player-Info:')
            print(str(spilleren) + '\n')

            # Plays and displays results
            trekningen = automaten.spill(spilleren)
            tallene = trekningen.getTrekningen()
            print('The following numbers was chosen: ' + str(tallene))
            print('You have {} correct numbers'.format(
                automaten.finnAntallRette(trekningen, spilleren)))

            # Displays the coins inside the machine
            print()
            print(automaten.finnBoessen())

            # Finishes of this round
            print('-----------------')
            print('|  Round ended  |')
            print('-----------------')
            print('Press enter to start a new round... ')
            again = input('Type \'exit\' to quit: ')
            if again == 'exit':
                sys.exit()
            Automattest.clear()


if __name__ == '__main__':
    Automattest.main()
