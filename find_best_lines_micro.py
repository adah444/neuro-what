# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:06:12 2013

@author: Adah
"""
#import import_data
from import_data import user_input

values = user_input()
position = values

values = user_input()
load = values

max_position = max(position)
max_load = max(load)

from numpy import arange, array, ones, linalg
from pylab import plot, show

xi = arange(0, len(position))
A = array([xi, ones(len(position))])
lin_reg = linalg.lstsq(A.T, load)[0]

line = lin_reg[0] * xi + lin_reg[1] #regression line
plot(xi, line, 'r-', xi, load, 'o')
show()

import numpy as np

A = np.vstack((position, np.ones(len(position)))).T
model, resid = np.linalg.lstsq(A, load)[:2]
r2 = 1-resid/(load.size * load.var)
print r2