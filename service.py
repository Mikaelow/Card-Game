from Object.deck import Deck
import random

class Service:
    def __init__(self,handA, handB):
        self.handA = handA
        self.handB = handB
    def choseOfPlayerA(self):
        Deck().showHand(self.handA)
        choose = int(input('Chose card from your hand '))-1
        card = self.handA[choose]
        self.handA.pop(choose)
        return card
    def choseOfPlayerB(self):
        Deck().showHand(self.handB)
        choose = int(input('Chose card from your hand '))-1
        card = self.handB[choose]
        self.handB.pop(choose)
        return card

    def cheeck(self,choseA, choseB):
        if choseA.getCost > choseB.getCost:
            self.handA.append(choseA)
            self.handA.append(choseB)
            print('\nPlayer A win this brawl!!')
        elif choseB.getCost > choseA.getCost:
            self.handB.append(choseA)
            self.handB.append(choseB)
            print('\nPlayer B win this brawl!!')
        else:
            self.handA.append(choseA)
            self.handB.append(choseB)
            print('\nRemis')

    def addCard(self, deckA, deckB):
        randomIntA = random.randint(0, len(deckA) - 1)
        randomIntB = random.randint(0, len(deckB) - 1)
        self.handA.append(deckA[randomIntA])
        self.handB.append(deckA[randomIntB])

    def resoults(self):
        if len(self.handA)==0:
            print("Player B won")
            return False
        elif len(self.handB)==0:
            print("Player A won")
            return False
        else:
            pass