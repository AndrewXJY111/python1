# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:32:25 2022

@author: 85798
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x=np.array([0.959,0.951,0.935,0.924,0.893,0.892,0.865,0.863,0.860,0.856,
            0.854,0.835,0.826,0.816,0.798,0.765,0.763,0.67])
y=np.arange(1,19)
labels=["一","二","三","四","五","六","七","八","九","十","十一","十二","十三","十四","十五","十六","十七","十八"]

plt.barh(y,x,tick_label=labels,align="center",height=0.6)
plt.show()