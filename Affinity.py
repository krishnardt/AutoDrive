# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:11:40 2018

@author: Krishna mohan
"""
import time
start = time.time();
import pandas as pd
import numpy as np

data = pd.read_table("data.tsv", header = None)

input = 'Avataar'
names = data[data[1] == 'Avataar'].iloc[:,0]

movies = set()

for i in names:
    movies = movies | set(data[data[0] == i].iloc[:,1])

#movies = list(movies)

movies.remove(input)
for i in movies:
    print(i)

end = time.time()
print(end-start)