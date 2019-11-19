# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:03:54 2019

@author: AshKing
"""

import numpy as np
from math import sin,cos,radians
import cv2 as cv


img = cv.imread('Images\\perspective transform\\example_01.png',1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB  )
centre=(img.shape[0]//2,img.shape[1]//2)  #centre of the image

shape=int((img.shape[0]**2+img.shape[1]**2)**0.5)   #create a copy of image but size along diagonals

copy=np.zeros((shape,shape))


def mul(*args):
    matrices=iter(args)   #store first matrix in matrices
    mul=next(matrices)   #iterator
    for i in matrices:
        mul=np.matmul(mul,i)
    return mul

def shift(x=0,y=0):
    return np.array([[1,0,x],[0,1,y],[0,0,1]])

def rot(theta=0):
    theta=radians(theta)
    return np.array([[cos(theta),
                   -sin(theta),0],[sin(theta),cos(theta),0]
                    ,[0,0,1]])
def mat(img):
    return np.array([[x,y,1] 
                     for x in range(img.shape[0]) 
                     for y in range(img.shape[1])]).transpose()  #creates an array of size 3*img.size

    

image=mat(img)  
#def scale(x=1,y=1):
#    return np.array([[x,0,0],[0,y,0],[0,0,1]]) 
x=1
y=0

a=0
b=1

rx,ry=(50,50)

#sx=0.3
#sy=0.3
theta=0
final=mul(shift(rx,ry)
        ,rot(theta)
        ,shift(-rx,-ry)
        ,image)
#shift=mul(shift(rx,ry),image)
#a=[shift[0],shift[1]]
#a=np.array(a,dtype=np.uint8)

cv.imshow("ik",img)
cv.waitKey(0)
cv.destroyAllWindows()