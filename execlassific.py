import pandas as pd

df = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
a = df.head(6)

total = len(df)
m = (len(df['Sex'].loc[df['Sex'] == 'M'])) / total
f =(len(df['Sex'].loc[df['Sex'] == 'F'])) / total

print(f'The percentage of men is {m * 100:.2f}%')
print(f'The percentage of women is {f * 100:.2f}%')



