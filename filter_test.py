# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:42:54 2019

@author: AshKing
"""
import numpy as np
import cv2 as cv
img = cv.imread('E:\\Tutorials\\DIP_nptel\\notes\\fourier analysis\\lena.png',0)

def cplot(**kwargs):
    for title,img in kwargs.items():
        cv.imshow(title,img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def filter(img,kernel):
    """same as cv.filter2d() time:171 ms ± 641 µs per loop
        odd kernels allowed only"""
    l,b=kernel.shape
    l=l//2
    b=b//2
    img=cv.copyMakeBorder(img,b,b,l,l,cv.BORDER_CONSTANT,value=[0,0,0])
    x,y=img.shape
    dst=np.zeros_like(img,dtype=np.uint16)
    for h in range(l,x-l):
        for w in range(b,y-b):
            dst[h][w]=cv.sumElems(img[h-l:h+l+1,w-b:w+b+1]*kernel)[0]
    return np.array(dst,dtype=np.int8)


h=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]],np.int8)

v=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]],np.int8)

ph=np.array([[-1,-1,-1],[0,0,0],[-1,-1,-1]],np.int8)

pv=np.array([[-1,0,-1],[-1,0,-1],[-1,0,-1]],np.int8)

sx=np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.int8)

sy=sx.T


flh=cv.filter2D(img,-1,h)

flv=cv.filter2D(img,-1,v)


s_x=cv.Sobel(img,-1,1,0,(3,3))

s_y=cv.Sobel(img,-1,0,1,(3,3))


sobelx=cv.filter2D(img,-1,sx)

sobely=cv.filter2D(img,-1,sy)


kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(img, -1, kernelx)
img_prewitty = cv.filter2D(img, -1, kernely)


cplot(img=img,
      sobx=sobelx,soby=sobely,
      sox=s_x,soy=s_y,
      tot_line=flh+flv,
      totssobel=s_x+s_y,
      prewitt=img_prewittx+img_prewitty,
      pxx=img_prewittx,pyy=img_prewitty)