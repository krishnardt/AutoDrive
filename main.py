# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:57:50 2018

@author: Krishna mohan
"""

import cv2
import numpy as np
import functions as fn






roads = fn.read_img("download3.jpg")
roads = fn.resize(roads)
#road = fn.img_bw(roads)
road = cv2.cvtColor(roads, cv2.COLOR_BGR2GRAY)
road = cv2.medianBlur(road, 1)
fn.show_img(road)


cont = cv2.Canny(road, 300, 450)

lines = cv2.HoughLinesP(cont, 1, np.pi/180, 100, minLineLength=10, maxLineGap=20)







#lines = cv2.HoughLines(cont, 1, np.pi/180, 200)
'''
for i in lines:
    rho, theta = i[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    
    cv2.line(roads,(x1,y1),(x2,y2),(0,0,255),2)

fn.show_img(roads)

'''
midX = roads.shape[1]
midY = roads.shape[0]
for i in lines:
    x1, y1, x2, y2 = i[0]
    
    if (x2-x1 > 50 or y2-y1 > 120):
        print(i)
        cv2.line(roads,(x1,y1),(x2,y2),(0,255,0),2)
        fn.show_img(roads)

    
