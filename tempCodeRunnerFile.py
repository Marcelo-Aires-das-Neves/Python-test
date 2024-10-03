import pandas as pd

dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
b = dados.groupby('Team').agg({'Name': 'nunique', 
                           'Medal': 'count',
                           'Games': 'nunique'}).sort_values('Medal')

print(b)