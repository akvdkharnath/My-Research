import pandas as pd
import numpy  as np
import math 
from collections import Counter


def entropy(parameters):
	entropy_val=0
	count=Counter(parameters)
	#print(count)
	count_keys=list(count.keys())
	count_values=list(count.values())
	#print(count_keys)
	#print(count_values)
	values_sum=sum(count_values)
	for i in count_values:
		entropy_val-=(i/values_sum)*math.log(i/values_sum,2)
	return(entropy_val)

def information_gain(data_frame,str1,str2,play_golf_entropy):
	count_passed_attridute=[]
	list1=data_frame[str1].tolist()
	numlist=[]
	divided_entropy=[]
	#print(list1)
	non_dup=list(set(data_frame[str1]))
	#print(non_dup)
	for i in non_dup:
		count_passed_attridute.append(list1.count(i))
	#print(count_passed_attridute)
	for i in non_dup:
		part1=data_frame[str2]=="Yes"
		part2=data_frame[str2]=="No"
		part3=data_frame[str1]==i
		#print (data_frame[part1 & part3].shape[0])
		#print (data_frame[part3 & part2].shape[0])
		numlist.append(data_frame[part1 & part3].shape[0])
		numlist.append(data_frame[part3 & part2].shape[0])
	#print(numlist)
	numlist=[ numlist[i:i+2] for i in range(0, len(numlist), 2) ]
	#print(numlist)
	for i in range(len(count_passed_attridute)):
		temp=0
		for j in numlist[i]:
			if j==0:j=4
			temp-=(j/count_passed_attridute[i])*math.log(j/count_passed_attridute[i],2)
		divided_entropy.append(temp)
	#print(divided_entropy)
	#print(count_passed_attridute)
	count_passed_attridute_sum=sum(count_passed_attridute)
	temp1=0
	for i in range(len(count_passed_attridute)):
		temp1-=(count_passed_attridute[i]/count_passed_attridute_sum)*divided_entropy[i]
	ans_information_gain=play_golf_entropy+temp1
	return(ans_information_gain)

def main():
	block_wise=[]
	phase_one=[]
	data_base={'Day':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],'Temperature':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],'Humidity':['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],'Play_Golf':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']}
	data_frame=pd.DataFrame(data_base,columns=['Day','Outlook','Temperature','Humidity','Wind','Play_Golf'])
	print(data_frame)
	varibles=data_frame.columns.tolist()
	del varibles[0]
	del varibles[-1]
	print(varibles)
	play_golf_entropy=entropy(data_frame['Play_Golf'])
	for i in varibles:
		phase_one.append(information_gain(data_frame,i,'Play_Golf',play_golf_entropy))

	print(phase_one)
	block_wise.append(varibles[phase_one.index(max(phase_one))])
	print(block_wise)
	


if __name__=='__main__':
	main()