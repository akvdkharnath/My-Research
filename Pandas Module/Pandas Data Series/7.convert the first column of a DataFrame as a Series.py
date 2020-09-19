import pandas as pd

dataframe  = pd.DataFrame([[1,2,3,4],[11,22,33,44],[111,222,333,444]])
print(dataframe)

series = pd.Series(list(dataframe[0]))
print(series)

# or 
series = dataframe.ix[:,0]
print(series)