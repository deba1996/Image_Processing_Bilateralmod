import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image 6.JPG')#read the image

blur = cv2.bilateralFilter(img,9,150,100)#apply filter

plt.subplot(121),plt.imshow(img),plt.title('Original')#show original image
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')#show blurred image
plt.xticks([]), plt.yticks([])
plt.show()
