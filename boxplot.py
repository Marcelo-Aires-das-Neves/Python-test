import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
dados.boxplot(column='Height')
plt.show()