import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
dados.hist(column='Height')
plt.show()