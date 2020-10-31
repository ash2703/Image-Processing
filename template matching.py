# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:12:54 2019

@author: AshKing
"""
import cv2 as cv
import numpy as np

img = cv.imread('images/filters/lena.png',0)

def template(img,match):
    l,b=match.shape
    l=l//2
    b=b//2
    norm=np.zeros_like(img,np.float32)
    dst=np.zeros_like(img,np.float32)
    img_c=cv.copyMakeBorder(img,b,b,l,l,cv.BORDER_CONSTANT,value=[0,0,0])
    x,y=img_c.shape
    
    for h in range(l,x-l):
        for w in range(b,y-b):
            a=img_c[h-l:h+l+1,w-b:w+b+1]
            norm[h-1][w-1]=np.sqrt(cv.sumElems(np.square(a))[0])
            dst[h-1][w-1]=cv.sumElems(a*match)[0]
    mat=dst/norm
    p,q=np.where(mat==mat.max())
    print(p,q)
    return img[int(p)-l:int(p)+l+1,int(q)-b:int(q)+b+1]
img=template(img,img[0:11,0:11])