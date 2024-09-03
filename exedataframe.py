import pandas as pd
import numpy as np

alunos = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
          'Nota': [7.5, 9, 6.5, 10],
          'Aprovado': [True, False, True, True]}

df = pd.DataFrame(alunos, columns=['Nome', 'Nota', 'Aprovado'])
print(df)
df2 = df.head()
print(df2)
df3 = df.describe()
print(df3)