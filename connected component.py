# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:20:54 2019

@author: AshKing
"""

import cv2 as cv
import numpy as np

img=cv.imread("images/connected component/scan.jpg",0)
ret,img = cv.threshold(img,200,255,cv.THRESH_BINARY)
count=0
same=set() 
#store=list()
connect=np.zeros(img.shape,dtype=np.uint16)
a=1
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        
        if img[i][j]==255 :
#            store.append(0)
            if img[i][j-1]==0 and img[i-1][j]==0:
                connect[i][j]=a
                a+=1
#                print("1",connect[i][j],i,j,a)
#                store.append(1)
            elif img[i][j-1]==255 and img[i-1][j]==0:
                connect[i][j]=connect[i][j-1]
#                print("2",connect[i][j],i,j,a)
#                store.append(2)
            elif img[i][j-1]==0 and img[i-1][j]==255:
                connect[i][j]=connect[i-1][j]
#                print("3",connect[i][j],i,j,a)
#                store.append(3)
            elif img[i][j-1]==255 and img[i-1][j]==255:
                if connect[i][j-1]==connect[i-1][j]:
                    connect[i][j]=connect[i][j-1]
#                    print("4",connect[i][j],i,j,a)
#                    store.append(4)
                elif connect[i][j-1]!=connect[i-1][j]:
                    same.add((min(connect[i-1][j],connect[i][j-1]),max(connect[i-1][j],connect[i][j-1])))
                    connect[i][j]=connect[i][j-1]
#                    print("5",connect[i][j],i,j,a)
#                    store.append(5)
            
    
            
        

cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()