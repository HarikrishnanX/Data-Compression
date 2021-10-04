# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:55:33 2020

@author: krish
"""

import numpy

from PIL import Image

im=Image.open("img.jpg")

pixelMap=im.load()

img=Image.new(im.mode,im.size)
pixelNew=img.load()

"""
2^8 -> 2^3
2^5 = 32
0-31=0
32-63=1
64-95=2
96-127=3
128-159=4
160-191=5
192-223=6
224-255=7
"""

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if((pixelMap[i,j]>=0)and(pixelMap[i,j]<=31)):
            pixelNew[i,j]=0
        elif((pixelMap[i,j]>=32)and(pixelMap[i,j]<=63)):
            pixelNew[i,j]=1
        elif((pixelMap[i,j]>=64)and(pixelMap[i,j]<=95)):
            pixelNew[i,j]=2
        elif((pixelMap[i,j]>=96)and(pixelMap[i,j]<=127)):
            pixelNew[i,j]=3
        elif((pixelMap[i,j]>=128)and(pixelMap[i,j]<=159)):
            pixelNew[i,j]=4
        elif((pixelMap[i,j]>=160)and(pixelMap[i,j]<=191)):
            pixelNew[i,j]=5
        elif((pixelMap[i,j]>=192)and(pixelMap[i,j]<=223)):
            pixelNew[i,j]=6
        elif((pixelMap[i,j]>=224)and(pixelMap[i,j]<=255)):
            pixelNew[i,j]=7
            
img.save("img_2.jpg")
J=numpy.asanyarray(Image.open("img_2.jpg"))            