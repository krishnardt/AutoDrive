# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:11:40 2018

@author: Krishna mohan
"""
# pandas is Python library that will work over numpy.
import pandas as pd                                                 
#It will store data in dataframe type for faster calculation purpose.
# It will convert the unstructural data into structured data computationally.

def getMovieNames():
    data = pd.read_table("data.txt", header = None, delimiter = '\t', chunksize = 100000)    # storing the data in varable "data" as dataframe
    # now the data contains 12 records as per example
    data = pd.concat(data, ignore_index = True)
    #Here input variable takes Avataar as input as per example
    input = 'Avataar'                                                    
    #filtering the names that contains Avataar as movie 
    names = set(data[data[1] == input][0])                                    
    #filtering the data from records with Avataar
    data = data[data[1] != input]                                        
    #now data will contain only 9 records
    movies = set()                                                       
    #create a set with variable "movie". Set will be helpful for getting unique values among 
    # different viewers. It is helpful in performing union and intersection operations.
    
    for i in names:                                                     
        #Iterating over each name
        movies |= set(data[data[0] == i][1])                            
        #performing union operation on 2 sets and storing output in movies variable
    
    
    for i in movies:
        print(i)
    

if __name__ == "__main__":
    getMovieNames();