# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:29:10 2019

@author: AshKing
"""
from math import sin,cos
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Images\\fourier analysis\\messi5.jpg',0)

def plot(img,title="Image"):
    plt.figure()
    plt.imshow(img,cmap="gray")
    plt.title(title)
    
def inverse(a,b):
    angle=np.angle(b[:,:,0]+b[:,:,1])
    copy=np.zeros_like(a,np.complex64)
    for i in range(a.shape[0]):
        for k in range(a.shape[1]):
            copy[i][k]=a[i][k]*cos(angle[i][k])+a[i][k]*sin(angle[i][k])*1j
    f_ishift = np.fft.ifftshift(copy)
    img_b=np.fft.ifft2(f_ishift)
    return np.abs(img_b)

    
dft=cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)  #2.53 ms ± 459 µs per loop 
dft_s=np.fft.fftshift(dft)

#mag,angle=cv.cartToPolar(dft_s[:,:,0],dft_s[:,:,1])

magnitude_spectrum = 20*np.log(cv.magnitude(dft_s[:,:,0],dft_s[:,:,1]))
mag=np.array(magnitude_spectrum,dtype=np.float32)

mag_c=np.array(mag)
mag_c[mag_c<100]=1
im_back=inverse(mag_c,dft_s)
plot(img)
plot(im_back)