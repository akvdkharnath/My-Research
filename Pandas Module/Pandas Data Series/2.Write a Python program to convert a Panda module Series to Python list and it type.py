import pandas as pd 

series  = pd.Series([1,2,3,4,5,6,7,8,9])
print('Series:')
print(series)

l1 = series.tolist()
print('Sries as list:')
print(l1)
print(type(l1))