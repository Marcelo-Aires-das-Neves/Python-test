import pandas as pd

df = pd.read_csv('C:/Users/USER/Downloads/archive/athlete_events.csv')
a = df.head(6)

total = len(df)
m = (len(df['Sex'].loc[df['Sex'] == 'M'])) / total
f =(len(df['Sex'].loc[df['Sex'] == 'F'])) / total
#in this part we calculate the percentage of men and women in the dataset, using the :.2f to round the percentage to 2 decimal places
print(f'The percentage of men is {m * 100:.2f}%')
print(f'The percentage of women is {f * 100:.2f}%')

"""
In this part define the round function to round the percentage to 2 decimal places
print(f'The percentage of men is {round(m * 100)}%')
print(f'The percentage of women is {round(f * 100)}%')
"""


