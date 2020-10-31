import numpy as np
import cv2
from matplotlib import pyplot as plt 

def get_hist(img):
    histogram = np.zeros(256)
    for pixel in img:
        histogram[pixel] += 1
    return histogram

img = cv2.imread('images/lena.jpeg',0)

mean = np.sum(img)/(img.shape[0] * img.shape[1])
variance = np.sum(np.square(img - mean))/(img.shape[0] * img.shape[1])
energy = np.sum(np.square(img))/(img.shape[0] * img.shape[1])

print("calculated  mean: {}, variance: {}, energy: {}".format(mean,variance,energy))

print("check numpy mean: {}, variance: {}, energy: {}".format(np.mean(img),np.var(img),energy))

hist = get_hist(img.flat)
p_x = hist/np.sum(hist)  #calculate probability
hist_mean = 0
for i in range(len(p_x)):
    hist_mean = hist_mean + i*p_x[i]   #x*p(x)
print(hist_mean)
plt.plot(hist)
plt.show()