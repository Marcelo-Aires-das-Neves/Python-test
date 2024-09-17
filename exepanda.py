import pandas as pd

dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')

b = dados.describe()
print(b)