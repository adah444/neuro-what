# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:53:54 2013

@author: Adah
"""

from import_data import user_input

from numpy import arange, array, ones #, linalg
from pylab import plot, show
from scipy import stats

#import numpy as np #####
#import pylab as pl
#import matplotlib

values = user_input()
position = values

values = user_input()
load = values

xi = arange(0,len(position))  
A = array([ xi, ones(len(position))])

slope, intercept, r_value, p_value, std_err = stats.linregress(xi,load)

print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err
print 'slope: ', slope
print 'intercept: ', intercept

line = slope*xi+intercept
plot(position,line,'r-',position,load,'o')
show()

