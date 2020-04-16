import numpy as np
b=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(b) #creating 2d arrays
d1=a.diagonal()
print(d1)
d2=np.fliplr(a).diagonal()
print(d2)
d1=sum(d1)
d2=sum(d2)
print(abs(d1-d2))