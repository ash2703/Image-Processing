# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:52:39 2019

@author: AshKing
"""

import numpy as np
import cv2 as cv
img = cv.imread('E:\\Tutorials\\DIP_nptel\\notes\\google.jpg',-1)
kernel=np.ones((3,3),np.uint8)



#k_x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
#k_y=k_x.T

def filter(img,kernel):
    """same as cv.filter2d() time:171 ms ± 641 µs per loop
        odd kernels allowed only"""
    l,b=kernel.shape
    l=l//2
    b=b//2
    img=cv.copyMakeBorder(img,b,b,l,l,cv.BORDER_CONSTANT,value=[0,0,0])
    x,y=img.shape
    dst=np.zeros_like(img,dtype=np.uint16)
    for h in range(l,x-l):
        for w in range(b,y-b):
            dst[h][w]=cv.sumElems(img[h-l:h+l+1,w-b:w+b+1]*kernel)[0]
        
    return np.array(dst,dtype=np.uint8)
#k_gabor=cv.getGaborKernel((3,3),100,radians(90),2*np.pi,5,0)
#dst=cv.filter2D(img,-1,k_gabor/cv.sumElems(k_gabor)[0])
#median=cv.bilateralFilter(img,d=9,sigmaColor =80,sigmaSpace =80)
#dst=filter(img,kernel)
#dst1=cv.blur(img,(3,3))
#dst=cv.GaussianBlur(img,ksize =(3,3),sigmaX =50,sigmaY =50)
#dst1=cv.Laplacian(dst,-1,scale=2)
#dst=cv.morphologyEx(dst,cv.MORPH_OPEN,kernel=kernel)
#ds=cv.medianBlur(dst,3)
#dst=cv.sepFilter2D(img,-1,k_x.flatten(),np.ones((1,9),np.int32))
dst2=cv.Sobel(img,-1,2,2,(3,3))
#cv.imshow("image",img)
#cv.imshow("dst",dst)
cv.imshow("dst1",dst2)
cv.imshow("median",img)
cv.waitKey(0)
cv.destroyAllWindows()