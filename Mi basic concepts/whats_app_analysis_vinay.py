import pandas as pd
import numpy as np
from collections import Counter



def main():
	file_data=open('WhatsApp Chat with Klu Vinay.txt', encoding="utf8")
	file_content=file_data.read()
	#file_content=list(file_content)
	file_content=str(file_content)
	file_content=file_content.replace(', ','@1').replace(' - ','@2').replace(': ','@3').replace('@1','\\').replace('@2','\\').replace('@3','\\')
	file=open('converted_data.txt','w',encoding="utf8")
	file.write(file_content)
	file.close
	#print('-----------------------------------')
	#print(file_content)
	data_base=pd.read_csv('converted_data.txt',delimiter='\t')
	print(data_base)

	
if __name__=='__main__':
	main()