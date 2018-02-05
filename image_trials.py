# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:56:01 2018

@author: Krishna mohan
"""

import cv2
import numpy as np


def show_img(image):
    #print_size(image)
    cv2.imshow('my_pic', image)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()

image = cv2.imread("road.jpg")
image = cv2.resize(image, (700, 500))
show_img(image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)

show_img(gray)

low_left = [0, 500]
low_right = [700, 500]
top_left = [0,250]
top_right = [700,250]

vertices = np.array([[low_left,low_right,top_left, top_right]], dtype=np.int32)

mask = np.zeros_like(gray)

cv2.fillPoly(mask, vertices, 255)

roi = cv2.bitwise_or(gray, mask)
show_img(roi)
