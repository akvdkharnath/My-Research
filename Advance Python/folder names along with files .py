import time
start = time.time()
from xlwt import Workbook
import os
folder_count,file_count,k=1,1,0
folder_location="E:\\ALGONOX\\final master sorted(232)"
output_path="E:\\harnathgenerated.xls"
template_name_list=os.listdir(folder_location)
file_list=[["Null"]]*len(template_name_list)
#print(template_name_list)
for i in range(len(template_name_list)):
    newpath=folder_location+'\\'+template_name_list[i]
    file_list[i]=os.listdir(newpath)
#print(file_list)
wb=Workbook()
sheet1=wb.add_sheet('sheet 1')
for i in range(len(file_list)):
    for j in  range(len(file_list[i])):
        sheet1.write(file_count,0,file_count)
        sheet1.write(file_count,2,file_list[i][j])
        sheet1.write(file_count,1,template_name_list[k])
        file_count+=1
    k+=1
wb.save(output_path)
end = time.time()
print(end - start)   
