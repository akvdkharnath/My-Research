import cv2
#import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('harnath.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(221),plt.imshow(img,cmap = 'pink')
plt.subplot(223),plt.imshow(img,cmap = 'gray')
plt.subplot(224),plt.imshow(img,cmap = 'Dark2')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
