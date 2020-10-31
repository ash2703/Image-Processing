import numpy as np
import cv2

img = cv2.imread('images/lena.jpeg',0)

gamma=0.3# Gamma < 1 ~ Dark ; Gamma > 1 ~ Bright

gamma_correction=((img/255)**(1/gamma))
negative_img = 255 - img

constant = 255/np.log(1+np.max(img))
log_image = constant * (np.log(img + 1)) 
log_image = np.array(log_image, dtype = np.uint8) 


cv2.imshow('Negative transformation',negative_img)
cv2.imshow('Logarithmic transformation',log_image)
cv2.imshow('Exponential transformation',gamma_correction)
cv2.waitKey(0) 
cv2.destroyAllWindows()