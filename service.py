from Object.deck import Deck
from Object.cards import Card

class Service:
    def choseOfPlayer(self, hand):
        Deck().showHand(hand)
        choose=int(input('Wybierz karte z talii '))-1
        return hand[choose]

    def cheeck(self,choseA, choseB):
        if choseA.getCost > choseB.getCost:
            print('Wygral gracz A')
        elif choseB.getCost > choseA.getCost:
            print('Wygral gracz B')
        else:
            print('Remis')