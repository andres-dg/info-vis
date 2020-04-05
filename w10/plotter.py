import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')
df = df.rename(columns={'Survey Year': 'year'})
print(df.columns)
df = df[df['Question'] == '... for at least one specific reason']
df = df[df['Gender'] == 'M']
df = df[df['Demographics Question'] == 'Age']

for i, row in df.iterrows():
    val = row.year
    df.at[i, 'year'] = val.split('/')[2]

df.rename(columns={"Demographics Response": "age"}, inplace=True)

df = df.groupby(['year', 'age']).mean()
df.columns = ['RecordID', 'value']
df = df.reset_index()
df.dropna(inplace=True)
df.drop(columns=['RecordID'], inplace=True)
df = df.set_index(['year', 'age']).value

df.unstack().plot(kind='bar')
plt.ylabel("% who agree")
plt.xlabel("Year")
plt.title("Evolution over time of males who believe it's ok to hit women for at least one specific reason")
plt.show()