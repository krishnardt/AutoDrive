# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:02:31 2018

@author: Krishna mohan
"""

import cv2
import numpy as np


def read_img(image):
    return cv2.imread(image, 1)


def resize(image):
    return cv2.resize(image, (700, 500))

def img_bw(image):
    img = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)[1]
    return img;


def show_img(image):
    #print_size(image)
    cv2.imshow('my_pic', image)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()