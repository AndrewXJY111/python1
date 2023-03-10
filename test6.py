# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:23:49 2022

@author: 85798
"""

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(5)
x1=np.array([10,8,7,11,13])
x2=np.array([9,6,5,10,12])
error=[1,1,1,1,1]
bar_height=0.3

plt.barh(y,x1,tick_label=['a','b','c','d','e'],height=bar_height)
plt.barh(y+bar_height,x2,height=bar_height)
plt.barh(y,x2,left=x1,height=bar_height,xerr=error)

plt.show()