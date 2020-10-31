# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:20:21 2019

@author: AshKing
"""

import cv2 as cv
import numpy as np


img = cv.imread('images/fourier analysis/horizontal_lines.jpg',0)

f = np.fft.fft2(img)   #2d fast fourier transform
fshift = np.fft.fftshift(f)  #shift the high frequency component in the centre
magnitude_spectrum = 20*np.log(np.abs(fshift))  #magnitude spectrum
magnitude_spectrum=np.array(magnitude_spectrum,dtype=np.uint8)
angle=20*np.log(np.angle(fshift))   #calculate phase
angle=np.array(angle,dtype=np.uint8)  #convert array to uint8

cv.imshow("original",img)
cv.imshow("magnitude",magnitude_spectrum)
cv.imshow("inverse",angle)
cv.waitKey(0)
cv.destroyAllWindows()

