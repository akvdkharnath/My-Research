import pandas as pd
import numpy as np

dic = {'apple':[1,2,3],'orange':[4,5,6]}
DF = pd.DataFrame(dic)
# print data frame 
print('\nDic as Data frame:')
print(DF)
 
# print perticular column of DF :
print("\nperticular column in data frame for example apple:")
print(DF["apple"])

# reading csv files
Dataset = pd.read_csv(".\\Data\\nba.csv")
print("\nData set is:")
print(Dataset)

# setting index column 
Dataset = pd.read_csv(".\\Data\\nba.csv",index_col='Name')
print("\ndata set having Name as column:")
print(Dataset)

print("\nInfo of data set:")
print(Dataset.info())

print("\nShape of Dataframe:")
print(Dataset.shape)

# append data frame to dataframe 

Dataset = Dataset.append(Dataset)
print("\nShape of Appned Dataframe:")
print(Dataset.shape)

# droping duplicate rows in data frame 

Dataset = Dataset.drop_duplicates()
print("\nShape of removed duplicate Dataframe:")
print(Dataset.shape)

# column description 
print("\nDataset Description:")
print(Dataset.describe())

# finding null values in dataframe
print("\nNumber of Null values per column:")
print(Dataset.isnull().sum()) # method-1
print(Dataset.isna().sum()) # method-2

# fill NULL values with some value

Dataset = Dataset.fillna(0)
 
# corelation

print(Dataset.corr())

