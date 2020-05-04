import pandas as pd
import numpy as np 
# 1. How to import pandas and check the version?
print("\n1. How to import pandas and check the version?")
print("Pandas Version: {}".format(pd.__version__))

# 2. How to create a series from a list, numpy array and dict?
print("\n2. How to create a series from a list, numpy array and dict?")
data_list = [1,2,3,4,5,6,7,8,9,10]
data_numpy = np.arange(1,11)
data_dic = dict(zip(data_list,data_numpy))
df1 = pd.Series(data_list)
df2 = pd.Series(data_numpy)
df3 = pd.Series(data_dic)
print(df1)
print(df2)
print(df3)

# 3. How to convert the index of a series into a column of a dataframe?
print("\n3. How to convert the index of a series into a column of a dataframe?")
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(1,27)
mydict = dict(zip(mylist, myarr))
df1 = pd.Series(mydict)
print(df1)