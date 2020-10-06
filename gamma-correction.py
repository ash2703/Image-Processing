import numpy as np
import cv2

img = cv2.imread('Images/lena.jpeg',0)

gamma=0.3# Gamma < 1 ~ Dark ; Gamma > 1 ~ Bright

gamma_correction=((img/255)**(1/gamma))


cv2.imshow('a',gamma_correction)
cv2.waitKey(0) 
cv2.destroyAllWindows()