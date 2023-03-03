from Object.cards import Card
from Object.deck import Deck
import random
import pandas as pd

class deckService():
    def getCardsToDeck(self):
        listOfCard = []
        cardsFromDataBase = pd.read_excel('HearthstoneCardsList.xlsx', sheet_name='Sheet1')
        for i in range(0, 10):
            cardName = cardsFromDataBase.iloc[:, 3][random.randint(1, 1000)]
            cardCost = cardsFromDataBase.iloc[:, 4][random.randint(1, 1000)]
            newCard = Card(cardName, cardCost)
            listOfCard.append(newCard)
            print(f'{listOfCard[i].cardNames}     {listOfCard[i].cardCost}')
        return Deck(listOfCard)
