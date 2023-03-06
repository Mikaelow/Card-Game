from Object.deck import Deck
from service import Service
import os

class main:
    def startGame(self):
        os.system('cls')
        deckPlayerA = Deck().getCardsToDeck()
        handPlayerA = Deck().getHand(deckPlayerA)
        deckPlayerB = Deck().getCardsToDeck()
        handPlayerB = Deck().getHand(deckPlayerB)
        service = Service(handPlayerA, handPlayerB)
        print('Welcome in my card game')
        while True:
            service.resoults()
            if service.resoults() == False:
                break
            print('\nPlayer A')
            choosePlayerA = service.choseOfPlayerA()
            print('\nPlayer B')
            choosePlayerB = service.choseOfPlayerB()
            service.cheeck(choosePlayerA, choosePlayerB)
            while True:
                if input('To continue click ENTER')=='':
                    service.addCard(deckPlayerA, deckPlayerB)
                    os.system('cls')
                    break

main().startGame()