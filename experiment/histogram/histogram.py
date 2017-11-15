# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:17:03 2017

@author: susha
"""

import matplotlib.pyplot as plt

yLabel = "Number of Students"
xLabel = "Time Spend for Correction"
title = "Histogram Students Correction"
bins=35

x = (16,11,6,6,5,5,5,5,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,
     2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
plt.hist(x,bins)
plt.title(title)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.show()