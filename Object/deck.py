import random
import pandas as pd
from Object.cards import Card

class Deck:
    def getCardsToDeck(self):
        listOfCard = []
        cardsFromDataBase = pd.read_excel('HearthstoneCardsList.xlsx', sheet_name='Sheet1')
        for i in range(0, 10):
            cardName = cardsFromDataBase.iloc[:, 3][random.randint(1, 1000)]
            cardCost = cardsFromDataBase.iloc[:, 4][random.randint(1, 1000)]
            newCard = Card(cardName, cardCost)
            listOfCard.append(newCard)
        return listOfCard
    def showDeck(self, deck):
        for i in range(0, 10):
            print(f'{i} {deck[i].cardNames}     {deck[i].cardCost}')
    def getHand(self, deck):
        hand = []
        while len(hand) != 5:
            randomCardFromDeck = deck[random.randint(0, 9)]
            if randomCardFromDeck in hand:
                continue
            else:
                hand.append(randomCardFromDeck)
        return hand

    def showHand(self, hand):
        for i in range(0, 5):
            print(f'{hand[i].cardNames}     {hand[i].cardCost}')