# import 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

# data set 
boston = load_boston()

print('boston data set Keys:')
print(boston.keys())

data = boston.data

print("boston data type: {}".format(type(data)))
print("boston data shape: {}".format(data.shape))
  
dataframe = pd.DataFrame(data = data,columns = boston.feature_names)

# print(dataframe.head())

dataframe['price'] = boston.target

print("Data set is:")
print(dataframe.head())

print("Data description: ")
print(dataframe.describe())
