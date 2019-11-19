# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:20:21 2019

@author: AshKing
"""

import cv2 as cv
import numpy as np


img = cv.imread('E:\\Tutorials\\DIP_nptel\\notes\\fourier analysis\\horizontal_lines_blurred.jpg',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)  #23.4 ms ± 1.16 ms per loop 
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum=np.array(magnitude_spectrum,dtype=np.uint8)

cv.imshow("original",img)
cv.imshow("magnitude",magnitude_spectrum)
cv.waitKey(0)
cv.destroyAllWindows()

