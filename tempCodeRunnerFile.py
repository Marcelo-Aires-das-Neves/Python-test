import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
dados.head()
dados.shape
enulo = dados.isnull()
enulo.head()
faltantes = dados.isnull().sum()
faltantes.head()
print(faltantes)
faltantes_percentual = (dados.isnull().sum() / len(dados['ID'])) * 100
print(faltantes_percentual)