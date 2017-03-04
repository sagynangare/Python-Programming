import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_hieght = {'meters':[10.26,10.31,10.27,10.22,10.23,6212.42, 10.28,10.25,10.31]}
df = pd.DataFrame(bridge_hieght)
df['STD'] = pd.rolling_std(df['meters'],2)
print(df)

df_std = df.describe()
print(df_std)
df.plot()
plt.show()