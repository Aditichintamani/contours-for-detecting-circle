# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 17:48:34 2015

@author: Johnny

Illustrate the tutorial contour demo.
"""

'''import numpy as np
import cv2


img = cv2.imread('IMG_20190325_102353.jpg')
img_bak = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(imgray, 110, 240, cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(imgray,250,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_list = []#print(contours)
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
cv2.imshow("Countour Mask", image)
cv2.imshow("Countor Plotter", img)
cv2.imwrite("tcon.jpg",img)
cv2.imwrite("countor Mask.jpg",image)
cv2.waitKey()
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()'''

import numpy as np
import cv2


img = cv2.imread('circle.png')
img_bak = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 110, 240, cv2.THRESH_BINARY)
#thresh = cv2.adaptiveThreshold(imgray,250,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)
        print(area)
#print(contours)
img = cv2.drawContours(img, contour_list, -1, (0, 255, 0), 1)
cv2.imshow("Countour", image)
cv2.imshow("Countor Plotter", img)
cv2.imwrite("tcon.jpg",img)
cv2.imwrite("countor Mask.jpg",image)
cv2.waitKey()
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

