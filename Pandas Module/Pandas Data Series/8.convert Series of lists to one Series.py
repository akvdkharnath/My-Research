import pandas as pd 

l1 = [['Red', 'Green', 'White'],['Red', 'Black'],['Yellow']]
d = [j for i in l1 for j in i]
print(d)
series = pd.Series(d)
print(series)