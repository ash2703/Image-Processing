# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:28:54 2019

@author: AshKing
"""

import numpy as np
import cv2 as cv
    

img = cv.imread('Images\\Slicing\\messi5.jpg',1)
img_r=np.zeros_like(img)   #create a 3D matrix of zeroes
img_b=np.zeros_like(img)
img_g=np.zeros_like(img)

img_b[:,:,0]=img[:,:,0]    #Change ith plane to R G or B value of image
img_g[:,:,1]=img[:,:,1]
img_r[:,:,2]=img[:,:,2]


cv.imshow("original",img)
cv.imshow("Red Plane",img_r)
cv.imshow("Green Plane",img_g)
cv.imshow("Blue Plane",img_b)
cv.waitKey(0)
cv.destroyAllWindows()
