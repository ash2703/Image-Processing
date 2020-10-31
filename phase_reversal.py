# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:52:34 2019

@author: AshKing
phase reversal practical
take 2 images and find their magnitude and phase spectrum
then swap the phase and magnitude information and observe reconstruct the image
observation: phase information is more dominant
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos

def plot(img,title="Image"):
    plt.figure()
    plt.imshow(img,cmap="gray")
    plt.title(title)

def inverse(mag,phase):
    '''takes in 2 input matrices and retruns the inverse shifted fourier transform by iterating over the 2 arrays'''
    copy=np.zeros_like(mag,np.complex64)
    for i in range(mag.shape[0]):
        for k in range(mag.shape[1]):
            copy[i][k]=mag[i][k]*cos(phase[i][k])+mag[i][k]*sin(phase[i][k])*1j
    f_ishift = np.fft.ifftshift(copy)
    img_b=np.fft.ifft2(f_ishift)
    return np.abs(img_b)


def inverse1(mag,phase):  #using lambda function
    '''takes in 2 input matrices and retruns the inverse shifted fourier transform by using lambda function'''
    copy=np.reshape(list((map(lambda mag,phase:mag*cos(phase)+mag*sin(phase)*1j,mag.flatten(),phase.flatten()))),(mag.shape))
#    copy=copy.reshape(mag.shape)
    f_ishift = np.fft.ifftshift(copy)
    img_b=np.fft.ifft2(f_ishift)
    return np.abs(img_b)



img1 = cv.imread('images/fourier analysis/messi5.jpg',0)
img2 = cv.imread('images/fourier analysis/lena.png',0)

img1=cv.resize(img1,(img2.shape[0],img2.shape[1]))
fft1=np.fft.fft2(img1)
fft2=np.fft.fft2(img2)

fft1=np.fft.fftshift(fft1)
fft2=np.fft.fftshift(fft2)

mag1= 20*np.log(np.abs(fft1))
mag2= 20*np.log(np.abs(fft2))

phase1=np.angle(fft1)
phase2=np.angle(fft2)

first=inverse1(mag1,phase2)
second=inverse1(mag2,phase1)
plot(img1,"messi")
plot(img2,"lena")
plot(first,"messi")
plot(second,"lena")
plt.show()