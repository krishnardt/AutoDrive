# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 17:16:50 2018

@author: Krishna mohan
"""

import cv2, numpy as np

def show_img(image):
    #print_size(image)
    cv2.imshow('my_pic', image)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()
    


def ROI(imimg, vertices):
    mask = np.zeros_like(img);
    
    if len(img.shape)> 2:
        no = img.shape[2];
        mask_color = (255,)*no
    else:
        mask_color = 255
    
    
    #vertices = [200:500, 0:700]
    cv2.fillPoly(mask, [vertices], mask_color)
    return cv2.bitwise_and(img, mask)

#show_img(out)

if __name__ == "__main__":
    img = cv2.imread("download7.jpg")
    img = cv2.resize(img, (700,500))
    vertices = np.array([[200, 250],[500, 250],[670, 450],[100,450]], np.int32)
    roi = ROI(img, vertices)
    show_img(roi)

