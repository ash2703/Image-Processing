# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:49:20 2019

@author: AshKing
"""
import cv2 as cv
import numpy as np


def fft(mat):
    mat=np.array(mat,np.float32)
    res=np.zeros(mat.shape,np.complex64)
    
    for i in range(res.shape[0]): #perform 1d fourier transform in x
        res[i]=np.fft.fft(mat[i])
        
    for i in range(res.shape[1]): #perform 1d fourier transform in y
        res[0:,i]=np.fft.fft(res[0:,i])
    return res


img = cv.imread('E:\\Tutorials\\DIP_nptel\\notes\\fourier analysis\\horizontal_lines_blurred.jpg',0)

f = fft(img)
fshift = np.fft.fftshift(f)  #23.4 ms ± 1.16 ms per loop 
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum=np.array(magnitude_spectrum,dtype=np.uint8)

cv.imshow("original",img)
cv.imshow("magnitude",magnitude_spectrum)
cv.waitKey(0)
cv.destroyAllWindows()
