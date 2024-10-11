import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')

# Filtrar dados para atletas masculinos
masculinos = dados[dados['Sex'] == 'M']

# Extrair altura e peso
altura = masculinos['Height']
peso = masculinos['Weight']

# Criar o gráfico de dispersão
plt.scatter(altura, peso, alpha=0.5, c='red', edgecolors='w', linewidth=0.5)

# Adicionar título e rótulos aos eixos
plt.title('Altura vs Peso de Atletas Masculinos')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
