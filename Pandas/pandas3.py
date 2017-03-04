import pandas as pd

##df = pd.read_csv('ZILL-Z77006_4B.csv')
##
##print(df.head())
##
##df.set_index('Date', inplace = True)
##df.to_csv('newcsv2.csv')
##df.to_csv('newcsv3.csv', header = False)
##df = pd.read_csv('newcsv3.csv', names = ['Data', 'Austin_HPI'], index_col=0)
##print(df.head())

df = pd.read_csv('newcsv3.csv', names= ['Date','Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'},inplace = True)
print(df.head())
