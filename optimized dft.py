# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:13:06 2019

@author: AshKing
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\\Tutorials\\DIP_nptel\\notes\\fourier analysis\\messi5.jpg',0)
rows,cols=img.shape

nrows = cv.getOptimalDFTSize(rows)
ncols = cv.getOptimalDFTSize(cols)

right = ncols - cols
bottom = nrows - rows
bordertype = cv.BORDER_CONSTANT

#creating a new big zero array and copy the image data to it
#nimg[:rows,:cols] = img   #takes 106 µs 
nimg = cv.copyMakeBorder(img,0,bottom,0,right,bordertype, value = 0) #takes 14 µs 10 times faster than numpy

#take fft of new padded image
fft_np = np.fft.fft2(nimg)   #9.28 ms ± 253 µs per loop 
fft_cv=cv.dft(np.float32(nimg),flags=cv.DFT_COMPLEX_OUTPUT)   #1.57 ms ± 103 µs per loop

dft_scv=np.fft.fftshift(fft_cv)
dft_snp=np.fft.fftshift(fft_np)

angle=np.angle(dft_scv)


mag_cv = 20*np.log(cv.magnitude(dft_scv[:,:,0],dft_scv[:,:,1]))  #1.32 ms ± 27.7 µs per loop
mag_np= 20*np.log(np.abs(dft_snp)) #3.92 ms ± 23.9 µs per loop


plt.figure(1)
plt.imshow(img, cmap = 'gray')
plt.figure(2)
plt.subplot(121),plt.imshow(mag_cv, cmap = 'gray'),plt.title('openCV')
plt.subplot(122),plt.imshow(mag_np, cmap = 'gray'),plt.title('Numpy')
plt.show()