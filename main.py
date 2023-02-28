import pandas as pd

cardsFromExcel = pd.read_excel('HearthstoneCardsList.xlsx', sheet_name='Sheet1')
print(cardsFromExcel.head())