import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split    # used to split for train and test data
from sklearn.linear_model import LinearRegression       # used to do regression analysis

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,1].values

#making the training and testing data set 
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0) # x,y are input data test size is the persentage of the test data and always random_state will be zero

# Simple Linear Regression set
regression=LinearRegression()
regression.fit(X_train,Y_train)

#result 
Y_pred=regression.predict(X_test)
print('real values are :')
print(Y_test)
print('generated values are :')
print(Y_pred)

# ploting the results for best analysis:
# results for training data
plt.figure(1)
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regression.predict(X_train))
plt.title('Salary Vs Experience(Training Data)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
# results for test data
plt.figure(2)
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_test,regression.predict(X_test))
plt.title('Salary Vs Experience(Testing Data)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

plt.show()