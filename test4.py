# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:48:14 2022

@author: 85798
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,8)
y=np.array([10770,16780,24440,30920,37670,48200,57270])
plt.bar(x,y,tick_label=["FY2013","FY2014","FY2015","FY2016","FY2017","FY2018","FY2019"],width=0.5)
plt.show()