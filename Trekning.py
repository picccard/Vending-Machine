import random
# https://stackoverflow.com/questions/24108417/simple-way-of-creating-a-2d-array-with-random-numbers-python

class Trekning:
    def __init__(self):
        self.trekningen = [random.randint(1,9) for i in range(5)]
        self.trekningen.sort()

    def getTrekningen(self):
        tempTrekning = []
        for num in self.trekningen:
            tempTrekning.append(num)
        return tempTrekning

    def finnAntallRette(self, tipping):
        myDict = dict((x,self.trekningen.count(x)) for x in self.trekningen)
        yourDict = dict((x,tipping.count(x)) for x in tipping)
        matches = 0
        for key in myDict.keys():
            if key in yourDict.keys():
                matches += min(myDict[key], yourDict[key])
        return matches
