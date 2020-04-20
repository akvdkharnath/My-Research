import pandas as pd
dic = {'apple':[1,2,3],'orange':[4,5,6]}
DF = pd.DataFrame(dic)
# print data frame 
print(DF)
 
# print perticular column of DF :
print(DF["apple"])
