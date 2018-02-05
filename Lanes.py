# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 07:43:49 2018

@author: Krishna mohan
"""

import cv2, numpy as np, math

def resize(image):
    return cv2.resize(image, (700, 500))
image = resize(cv2.imread("road.jpg"))

def show_img(image):
    #print_size(image)
    cv2.imshow('my_pic', image)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()
    
HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

show_img(image)
show_img(HSV_image)


def maskHSV(img):
    lower_red = np.array([0,0,180])
    upper_red = np.array([150,200,255])
    
    mask = cv2.inRange(img, lower_red, upper_red)
    return cv2.bitwise_and(img, img, mask = mask)
    

def getLanes(HSV_image, image):
    lanes = maskHSV(HSV_image)
    return lanes;

lanes = getLanes(HSV_image, image)
show_img(lanes)


gray = cv2.cvtColor(lanes, cv2.COLOR_RGB2GRAY)

show_img(gray)

#roi = gray[220:, :]
#roi = cv2.setImageROI(gray, [220:, :])











def selectROI(image):
    rows, cols = image.shape[:2]
    lower_left = [680, 220]
    lower_right = [680, 500]
    top_left = [5, 220]
    top_right = [5, 500]
    
    
    vertices = np.array([[lower_left, top_left, top_right, lower_right]], dtype=np.int32)
    
    mask = np.zeros_like(image)
    
    if len(mask.shape) == 2:
        cv2.fillPoly(mask, vertices, 255)
    else:
        cv2.fillPoly(mask, vertices, (255,)*mask.shape[2]) # in case, the input image has a channel dimension        
    return cv2.bitwise_or(image, mask)
    
    
roi = selectROI(image)
#roi = image[250:500, 0:700]
print("ROI")
show_img(roi)
rows, cols = roi.shape[:2]
src = np.float32([[0, cols], [cols, rows], [0, 0], [rows, 0]])
dst = np.float32([[250, 300], [250, 500], [0, 0], [0, 700]])
#dst = src

M = cv2.getPerspectiveTransform(src, dst)
warped_img = cv2.warpPerspective(roi, M, (cols, rows))
show_img(warped_img)











#blur = cv2.GaussianBlur(roi, (5,5),0)

#show_img(blur)

'''

edges = cv2.Canny(roi, 50, 150)
show_img(edges)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=150, maxLineGap=250)



for i in lines:
    x1, y1, x2, y2 = i[0]
    
    #if (x1 < 20 and x2 > 689) or (x1 > 140 and x2 > 600) and (x2-x1 > 50 or y2-y1 > 120):
    if y1 != y2:
        if y1-y2 > 40 or y2-y1 > 40:
            print(i)
            print(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
            show_img(image)
'''



rows, cols = roi.shape[:2]

