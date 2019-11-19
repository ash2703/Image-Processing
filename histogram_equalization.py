# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:07:18 2019

@author: AshKing
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 
img = cv2.imread('E:\Codes\Python\Person_Counting\images\\work.png',0)
flat=img.flatten()
def get_hist(img):
    histogram = np.zeros(256)
    for pixel in img:
        histogram[pixel] += 1
    return histogram

hist = get_hist(img.flat)
plt.plot(hist)
plt.show()
def cum_sum(a):      #cummulative sum
    a=iter(a)
    b=[next(a)]  #store 1st value of a in b
    for i in a:
        b.append(b[-1]+i)
    return np.array(b)
cs=cum_sum(hist)
plt.plot(cs)
plt.show()
def scale(val):
    new_val=(val-val.min())*255
    total_vals=val.max()-val.min()
    return (new_val/total_vals)
cs=np.uint8(scale(cs))
plt.plot(cs)
plt.show()
img_new=cs[flat]   #replace pixels by their cummulative values
print(img_new.shape)
plt.hist(img_new)
img_new=np.reshape(img_new,img.shape)
cv2.imshow("original",img)
cv2.imshow("histogram equalised",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()