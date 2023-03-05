from Object.deck import Deck
from service import Service

class main:
    def startGame(self):
        deckPlayerA = Deck().getCardsToDeck()
        handPlayerA = Deck().getHand(deckPlayerA)
        deckPlayerB = Deck().getCardsToDeck()
        handPlayerB = Deck().getHand(deckPlayerB)
        print('Witaj w grze karcianej')
        print('\nGracz A')
        choosePlayerA = Service().choseOfPlayer(handPlayerA)
        print('\nGracz B')
        choosePlayerB = Service().choseOfPlayer(handPlayerB)
        Service().cheeck(choosePlayerA, choosePlayerB)

main().startGame()