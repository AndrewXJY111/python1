# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:43:01 2022

@author: 85798
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(6)
y1=np.array([1,4,3,5,6,7])
y2=np.array([1,3,4,2,7,6])
y3=np.array([3,4,3,6,5,5])

plt.stackplot(x,y1,y2,y3)
plt.show()