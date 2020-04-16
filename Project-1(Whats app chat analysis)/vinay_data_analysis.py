import os
import re
import pandas as pd
import numpy as np

watsup_file = 'WhatsApp Chat with Klu Vinay.txt'


# Read WhatsApp file
if os.path.exists(watsup_file):
        file_data = open(watsup_file,'r', encoding="utf8")
        watsup_content = file_data.read()

# Get date
date_regex=re.compile(r'(\d+/\d+/\d+)')
date=date_regex.findall(watsup_content)

# Get time
time_regex=re.compile(r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])')
time=time_regex.findall(watsup_content)

# Get Users
user_regex=re.compile(r'-(.*?):')
user=user_regex.findall(watsup_content)

# Get Message
message_regex=re.compile(r"(\n)(?<=)(\d+/\d+/\d+)(.*)")
message=message_regex.findall(watsup_content)

data=[]
for w,x,y,z in zip(date,time,user,message):
    data.append([str(w),str(x),str(y),str(z)])
    
# Create DataFrame from WhatsApp content
df=pd.DataFrame(data,columns=("Date","Time","User","Message"))
message_data=list(df['Message'])
#print(message_data)
for message in range(len(message_data)):
	message_data[message]=re.sub(r'.*:', ':',str(message_data[message])).replace(':','').replace('\')','')
#print(message_data)
df=df.drop('Message',axis=1)
df['Message']=np.array(message_data)
print(df)