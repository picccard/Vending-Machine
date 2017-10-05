import random
# https://stackoverflow.com/questions/24108417/simple-way-of-creating-a-2d-array-with-random-numbers-python

class Raffle:
    def __init__(self):
        self.draw = [random.randint(1,9) for i in range(5)]
        self.draw.sort()

    def getDraw(self):
        tempDraw = []
        for num in self.draw:
            tempDraw.append(num)
        return tempDraw

    def getMatches(self, guess):
        myDict = dict((x,self.draw.count(x)) for x in self.draw)
        yourDict = dict((x,guess.count(x)) for x in guess)
        matches = 0
        for key in myDict.keys():
            if key in yourDict.keys():
                matches += min(myDict[key], yourDict[key])
        return matches
