import numpy as np
import cv2

img = cv2.imread('Images/lena.jpeg',0)

mean = np.sum(img)/(img.shape[0] * img.shape[1])
variance = np.sum(np.square(img - mean))/(img.shape[0] * img.shape[1])
energy = np.sum(np.square(img))/(img.shape[0] * img.shape[1])

print("calculated  mean: {}, variance: {}, energy: {}".format(mean,variance,energy))

print("check numpy mean: {}, variance: {}, energy: {}".format(np.mean(img),np.var(img),energy))