# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:39:30 2019

@author: AshKing
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def plot(img,title="Image"):
    plt.figure()
    plt.imshow(img,cmap="gray")
    plt.title(title)

img = cv.imread('Images\\fourier analysis\\messi5.jpg',0)


imf = np.float32(img)/255.0  # float conversion/scale
dst = cv.dct(imf)           # the dct
inv=cv.dct(dst,flags=cv.DCT_INVERSE)  #inverse discrete cosine transform

img1 = np.uint8(dst)*255.0 

dst2=cv.dct(inv)
inv2=cv.dct(dst2,cv.DCT_INVERSE)

dst3=cv.dct(inv)
inv3=cv.dct(dst2,cv.DCT_INVERSE)

dst4=cv.dct(inv)
inv4=cv.dct(dst2,cv.DCT_INVERSE)

plot(img,"original")
plot(img1,"dct")
plot(inv,"inverse")
plot(inv2,"dst")
plot(inv3,"dst")
plot(inv4,"dst")
plt.show()
