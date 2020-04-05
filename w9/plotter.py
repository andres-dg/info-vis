import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

plt.plot(df['grade'], df['hours_needed'], marker='x', label = 'Hours needed')
plt.plot(df['grade'], df['hours_averaged'], marker='x', label = 'Hours averaged')

for i,j in zip(range(13), df['hours_needed']):
    plt.annotate(str(j),xy=(i,j + 0.05))

for i,j in zip(range(13), df['hours_averaged']):
    plt.annotate(str(j),xy=(i,j + 0.05))

plt.xlabel('Grade')
plt.ylabel('Hours')
plt.title('Sleeping hours per grade')

plt.legend()
plt.show()