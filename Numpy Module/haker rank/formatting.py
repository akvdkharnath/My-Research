arr=[4,5,2,-1,0,-4,-7,-8]
l=len(arr)
p=n=z=0
for i in range(l):
        if(arr[i]>0):p+=1
        elif(arr[i]<0):n+=1
        else:z+=1
p,n,z=p/l,n/l,z/l
print("{:.6f}".format(p))
print("{:.6f}".format(n))
print("{:.6f}".format(z))