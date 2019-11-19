# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:52:12 2019

@author: AshKing
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('E:\\Tutorials\\DIP\\notes\\eq_img.jpg',0)
new_img=np.zeros(img.shape,dtype=np.uint8)
new=np.zeros((255,1),dtype=np.uint8)
hist=np.zeros(256,dtype=np.uint8)
low=100
high=200
L=255
for i,j in enumerate(img.flat):
    hist[j]+=1
    j=int(L*(j-low)/high)
    if j>L:
        j=L
    elif j<0:
        j=0
    new[j]=new[j]+1
    new_img.flat[i]=j

plt.plot(hist)
plt.show()
plt.plot(new)

new_img=np.reshape(new_img,img.shape)
cv2.imshow("original",img)
cv2.imshow("contrast equalised",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()