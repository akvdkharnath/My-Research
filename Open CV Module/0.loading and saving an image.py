import cv2
image_path="E:\python blog\Open cp files\Image_data_base\lena_color_256.tif"
output_path="E:\python blog\Open cp files\Image_data_base\generated from python.tif"
image=cv2.imread(image_path)
#to create a named window 
cv2.namedWindow('first image',cv2.WINDOW_AUTOSIZE)
#cv2.imshow("first imagee",image)
cv2.waitKey(0)
cv2.imwrite(output_path,image)
#cv2.destroyAllWindows()
#this for delete a pertukular window  
cv2.destroyAllWindows('first image')