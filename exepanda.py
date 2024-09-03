import pandas as pd

dados = pd.read_excel('C:/Users/USER/Documents/dditatech/arquivo1.xlsx')
a = dados.head(6)
b = dados.columns.tolist()     # mostra as colunas 
print(b)