import numpy as np 
import cv2
img=cv2.imread('harnath.jpg')
cv2.imshow('mage0',img)
cv2.line(img,(100,20),(50,60),(255,0,0),1)
cv2.rectangle(img,(10,20),(500,60),(0,255,0),1)
#        image,starting position,ending position,colour code bgr,width
cv2.circle(img,(10,20),44,(0,255,0),2)
#        image,center of circle,radius length,colour code bgr, +ve number for width for only out line
#                                                              -ve number for full colour in circle
# to draw a polygon we need a set of points for this we are using numpy array to plot
array=np.array([[10,20],[10,30],[20,40],[40,50],[50,60]])
cv2.polylines(img,[array],True,(255,57,34),2)
#           image,array,true to join last and first points False to not to join, colour,width
cv2.imshow('mage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
