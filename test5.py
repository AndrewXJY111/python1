# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:19:46 2022

@author: 85798
"""

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(5)
x1=np.array([10,8,7,11,13])
bar_height=0.3
error=[1,1,1,1,1]
plt.barh(y,x1,tick_label=['a','b','c','d','e'],height=bar_height,xerr=error)
plt.show()