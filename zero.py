# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:33:16 2022

@author: Beautiful Mishika
"""
from tkinter import *
import matplotlib.pyplot as plt

data = [[0,0,0,0,0,0,0,0],
       [0, 0, 1, 1, 1, 1,0,0],
       [0, 0, 1,0,0,1,0,0],
       [0, 0, 1,0, 0, 1,0,0],
       [0, 0, 1, 0, 0, 1, 0,0],
       [0, 0, 1,0,0, 1,0,0],
       [0, 0, 1, 1, 1, 1, 0,0],
       [0, 0,0,0,0,0,0,0]]

plt.imshow(data, cmap = 'gray')
plt.show()

root.mainloop()
