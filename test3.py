# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:40:56 2022

@author: 85798
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(5)
y1=np.array([10,8,7,11,13])
y2=np.array([9,6,5,10,12])
bar_width=0.3
error=[2,1,2.5,2,1.5]

plt.bar(x,y1,tick_label=['a','b','c','d','e'],width=bar_width)
plt.bar(x+bar_width,y2,width=bar_width)
plt.bar(x,y2,bottom=y1,width=0.5,yerr=error)

plt.show()