# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:51:55 2018

@author: Krishna mohan
"""

data = open("data.tsv", "r");
val = data.read()
copy = open("data.txt", "w");
for i in range(0, 200000):
     #for i in data.readlines():
      #   copy.write(i)
     copy.write(val)
     copy.write("\n")

data.close()
copy.close()