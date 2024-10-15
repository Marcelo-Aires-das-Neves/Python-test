import pandas as pd
from sklearn.model_selection import train_test_split

arquivo = pd.read_csv("C:/Users/USER/Downloads/wine_dataset.csv")
arquivo.head()

arquivo['style'] = arquivo['style'].replace('red',0)
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)