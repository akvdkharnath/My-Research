import math
s="jjsbldv lsbhlb ljlb lbshdbv uh dhbv jvcvn"
s=s.replace(" ","")
l=len(s)
n=math.sqrt(l)
nf=math.floor(n)
nc=math.ceil(n)
lt=list(s)
lt=[lt[i:i+n] for i in xrange(0, len(lt), n)]
print(lt)
#%%
import re
s=re.findall('.{1,2}', '1234567890')
z="SOSSPSSQSSOR"
count=0
s=re.findall('...',z)
print(s)
for i in s:
    if(i!='SOS'):
        count+=1
print(count)
print(s[0])