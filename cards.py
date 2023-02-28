import pandas as pd

class Cards():
    def __init__(self,cardNames,cardCost):
        self.cardNames=cardNames
        self.cardCost=cardCost



cardsFromExcel = pd.read_excel('HearthstoneCardsList.xlsx', sheet_name='Sheet1')
for i in range(0,10):
    cardNames = cardsFromExcel.iloc[:, 3][i]
    cardCost = cardsFromExcel.iloc[:, 4][i]
    obj=Cards(cardNames,cardCost)
    print(f"{obj.cardNames} {obj.cardCost}")
