# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:08:03 2019

@author: AshKing
"""
import cv2
import numpy as np


img = cv2.imread('E:\\Tutorials\\DIP_nptel\\notes\\perspective transform\\example_01.png',1)
rows,cols,ch = img.shape

pts1 = np.float32([(73, 239), (356, 117), (475, 265), (187, 443)])
pts2 = np.float32([[0,200],[561,200],[561,430],[0,430]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,img.shape[:2])

cv2.imshow("persp",dst)
cv2.imshow("og",img)
cv2.waitKey()
cv2.destroyAllWindows()