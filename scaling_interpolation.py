# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:59:35 2019

@author: AshKing
"""
import cv2



img = cv2.imread('Images\\perspective transform\\example_01.png',1)


height, width = img.shape[:2]
res = cv2.resize(img,(200,200), interpolation = cv2.INTER_NEAREST)
res1 = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img,(200,200), interpolation = cv2.INTER_AREA)
res3 = cv2.resize(img,(200,200), interpolation = cv2.INTER_LANCZOS4)

cv2.imshow("original",img)
cv2.imshow("NEAREST",res)
cv2.imshow("CUBIC",res1)
cv2.imshow("AREA",res2)
cv2.imshow("LANCZOS4",res3)
cv2.waitKey(0)
cv2.destroyAllWindows()
