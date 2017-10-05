from lib.Coin import Coin
from lib.Player import Player
from lib.CoinBox import CoinBox
from lib.Price import Price
from lib.Pricelist import Pricelist
from lib.Raffle import Raffle
from lib.VendingMachine import VendingMachine
import os, sys
#import Coin, Player, CoinBox, Price, Pricelist, Raffle, VendingMachine, os, sys

class VendingMachineTest:
    @staticmethod
    def somethingWrong():
        print('You typed something illegal...')
        input('Press enter to try again. ')
        VendingMachineTest.clear()

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def main():
        print('Round is starting')
        print('-----------------')
        # Creates a vending machine
        vendingMachine = VendingMachine(200, 5)

        # Sets the price for these currencys: EUR, USD, NOK, DONG
        CHOISES = ['EUR', 'USD', 'NOK', 'DONG']
        PRICES = [0.12, 0.16, 1.00, 0.08]
        for i in range(len(CHOISES)):
            vendingMachine.setPrice(CHOISES[i], PRICES[i])

        # Runs until the box is full
        while not vendingMachine.isCoinBoxFull():
            # Reads your coin
            # Loop until acceptable valuta chosen
            currency = ''
            while currency not in CHOISES:
                currency = input('\n' + vendingMachine.getPricelist() +
                               '\n\n' + 'What currency is your coin? ').upper()
                if currency not in CHOISES:
                    VendingMachineTest.somethingWrong()
            # Loop until verdi is a float
            value = ''
            while not isinstance(value, float):
                valueStr = input('Each number you guess will cost ' + str(vendingMachine.getPriceForAGuess(currency))
                                 + ' {}'.format(str(currency)) + '\n\nYour coins value in ' + currency + ': ')
                try:
                    value = float(valueStr)
                except ValueError as ex:
                    VendingMachineTest.somethingWrong()

            # Reads your selected numbers to guess
            numGuesses = vendingMachine.getAllowedGuesses(currency, value)
            guesses = [0] * numGuesses
            for i in range(numGuesses):
                while guesses[i] not in range(1, 10):
                    try:
                        guesses[i] = int(input('Chose a number between 1 and 9: '))
                        if guesses[i] not in range(1, 10):
                            VendingMachineTest.somethingWrong()
                    except ValueError as ex:
                        VendingMachineTest.somethingWrong()

            # Gets ready to display results
            VendingMachineTest.clear()
            print('--------------------')
            print('|  Round summmary  |')
            print('--------------------')

            # Creates a player and displays player info
            player = Player(guesses, currency, value)
            print('Player-Info:')
            print(str(player) + '\n')

            # Plays and displays results
            raffle = vendingMachine.play(player)
            draw = raffle.getDraw()
            print('The following numbers was chosen: ' + str(draw))
            print('You have {} correct numbers'.format(
                vendingMachine.getMatches(raffle, player)))

            # Displays the coins inside the machine
            print()
            print(vendingMachine.getCoinBox())

            # Finishes of this round
            print('-----------------')
            print('|  Round ended  |')
            print('-----------------')
            print('Press enter to start a new round... ')
            again = input('Type \'exit\' to quit: ')
            if again == 'exit':
                sys.exit()
            VendingMachineTest.clear()

        # Once the coinbox is full, quit loop, display message and quit
        VendingMachineTest.clear()
        input('The vending machine\'s coinbox needs emptying, ' +
              'please contact staff... ')


if __name__ == '__main__':
    VendingMachineTest.main()
