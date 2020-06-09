import pandas as pd
from dataExtract import getResponse, extractData

data = getResponse()
df = extractData(data)

#print(df.head())
print('Null Values:')
print(df.isna().count())



