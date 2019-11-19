# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:55:36 2019

@author: AshKing
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images\\fourier analysis\\messi5.jpg',0)

dft=cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)  #2.53 ms ± 459 µs per loop 
dft_s=np.fft.fftshift(dft)

#mag,angle=cv.cartToPolar(dft_s[:,:,0],dft_s[:,:,1])

magnitude_spectrum = 20*np.log(cv.magnitude(dft_s[:,:,0],dft_s[:,:,1]))
mag=np.array(magnitude_spectrum,dtype=np.float32)


rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)  # create a mask first, center square is 1, remaining all zeros

mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fshift = dft_s*mask
#
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.figure(1)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.figure(2)
plt.imshow(mag, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
