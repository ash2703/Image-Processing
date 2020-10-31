# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:03:54 2019

@author: AshKing
"""

import numpy as np
from math import sin,cos,radians
import cv2 as cv


img = cv.imread('images/perspective transform/example_01.png')

centre=(img.shape[0]//2,img.shape[1]//2)

shape=int((img.shape[0]**2+img.shape[1]**2)**0.5)

copy=np.zeros((shape,shape))


def mul(*args):
    """Function takes multiple matrices as arguements
       and multiplies them together in the given order"""
    matrices=iter(args)
    mul=next(matrices)
    for i in matrices:
        mul=np.matmul(mul,i)
    return mul

def shift(x=0,y=0):
    """perform a shifting operations on the image with respect to x and y"""
    return np.array([[1,0,x],[0,1,y],[0,0,1]])

def rot(theta=0):
    """rotate the image by theta angle"""
    theta=radians(theta)
    return np.array([[cos(theta),
                   -sin(theta),0],[sin(theta),cos(theta),0]
                    ,[0,0,1]])
def mat(img):
    """create a matrix from the given matrix of the form
       --       --
       |  x1 x2  |
       |  y1 y2  |
       |  1  1   |
       --       --
    """
    return np.array([[x,y,1] for x in range(img.shape[0]) for y in range(img.shape[1])]).transpose()

image=mat(img)  

final=np.array(mul(shift(50,50)  #shift the image by 50 pixels in x and y
        ,rot(30)  #rotate by 30 radians
        ,shift(-50,-50)     #shift the image by 50 pixels in -x and -y
        ,image),np.uint8).reshape(img.shape)   #reshape the image in a 3d vector of uint8
#shift=mul(shift(rx,ry),image)
