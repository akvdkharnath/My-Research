import pandas as pd
import numpy as np
from collections import Counter



def main():
	file_data=open('WhatsApp Chat.txt', encoding="utf8")
	file_content=file_data.read()
	#file_content=list(file_content)
	print(file_content)
	file_content.replace(', ','\\t')
	print





if __name__=='__main__':
	main()