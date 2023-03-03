
class Card:
    def __init__(self, cardNames, cardCost):
        self.cardNames = cardNames
        self.cardCost = cardCost

    @property
    def getName(self):
        return self.cardNames
    @property
    def getCost(self):
        return self.cardCost