# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:06:59 2018

@author: Krishna mohan
"""

import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
def show_img(image):
    #print_size(image)
    cv2.imshow('my_pic', image)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()

 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)



#Calirating the camera after getting the object and image points
def calibrate(obj, img, gray):
    return cv2.calibrateCamera(obj, img, gray.shape[::-1], None, None)

#creating object points i.e., real object coordinates in 3D form
def corners():
    objp = np.zeros((6*9,3), np.float32);
    objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)
    #creating the list for object points and image points i.e., the coordinates of image
    objpts = []
    imgpts = []
    #location of images using for calibraiton of camera
    images = glob.glob("Caliberation/*.jpg");
    
    
    #Looping through every image to get the corner cordinates of the image.
     #If the corners are found, then boolean will return as True.
    for i in images:
        img = cv2.imread(i)
        img = cv2.resize(img, (700,500))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        
        boolean, corners = cv2.findChessboardCorners(gray,(9,6), None);
        
        if boolean == True:
            objpts.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners,(11,11),(-1,-1),criteria)
            imgpts.append(corners2)
            
            img = cv2.drawChessboardCorners(img,(9,6), corners2, boolean)
            
    return calibrate(objpts, imgpts, gray)


#ret, mtx, dist, rvecs, tvecs = 


img = cv2.imread("road.jpg")
img = cv2.resize(img, (700,500))
h,w = img.shape[:2]

def displaying_original_and_undistorted_images(original, un_distorted):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax[1].imshow(cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB))
    plt.show()
ret, mtx, dist, rvecs, tvecs = corners()
undistorted_img = cv2.undistort(img, mtx, dist, mtx);


show_img(undistorted_img)
displaying_original_and_undistorted_images(img, undistorted_img);
