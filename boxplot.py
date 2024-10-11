import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')

# Criar o box plot
boxplot = dados.boxplot(column='Age', by='Sex', patch_artist=True)

# Customizar o box plot
plt.title('Distribuição de Idade por Sexo')
plt.suptitle('')  # Remove o título padrão gerado pelo 'by'
plt.xlabel('Sexo')
plt.ylabel('Idade')

# Customizar as cores das caixas
colors = ['#FF9999', '#66B2FF']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customizar a cor e o estilo das medianas
for median in boxplot['medians']:
    median.set(color='red', linewidth=2)

# Customizar a cor e o estilo dos bigodes
for whisker in boxplot['whiskers']:
    whisker.set(color='blue', linestyle='--')

# Adicionar grid
plt.grid(True)

# Mostrar o gráfico
plt.show()