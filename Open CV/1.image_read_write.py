import cv2

# 1 for colour image 
# 0 for black and white image
# -1 for image with alpha scale 


img=cv2.imread('C:\\Users\\Admin\\Desktop\\python masters\\opencv-master\\samples\\data\\lena.jpg',-1)  # reading an image
print(img)
cv2.imshow('Image',img)   # showing an image 
cv2.waitKey(5000)         # wait time to show the image 
cv2.destroyAllWindows()   #commend to destroy the images shown 

cv2.imwrite('write.jpg',img)
