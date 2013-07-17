# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:55:18 2013

@author: Adah
"""

from import_data import user_input

from numpy import arange
from pylab import plot, show, ylim, xlim
from scipy import stats

import math

values = user_input()
xvalues = values[0] 
yvalues = values[1]

max_load = max(yvalues)
min_load = min(yvalues)
if abs(max(yvalues)) > abs(min(yvalues)): #determines if the peak is a max or a min
    peak_load = max(yvalues)
    index_anchor = yvalues.index(peak_load)
else:
    peak_load = min(yvalues)
    index_anchor = yvalues.index(peak_load)
     
line_num = 0
all_lines = []

desired_rsqval = 0.998 #input your desired r value
least_numpts = 4 #input the desired least number of points required in a linear regression

length = 6.0 #input the scaffold length
pi = math.pi
#outer_diam = 3.0 #input the outer diameter of the scaffold
#inner_diam = 2.5 #input the inner diameter of the scaffold
#area = pi * ((outer_diam/2/1000)**2 - (inner_diam/2/1000)**2) #if there is an inner and outer diameter
diam = 3.8 #input the diameter if there is no inner/outer diameter
area = pi * (diam/2/1000)**2 #if there is only one diameter

for iterate in range(0, len(xvalues)):
    if index_anchor > least_numpts - 1:

        stop = 0
        for next_anchor in range(index_anchor, -1, -1):
            count = 0
            if stop == 1:
                break
            
            if next_anchor == index_anchor:
                r_value1 = 0
                
            if r_value1**2 >= desired_rsqval:
                break
        
            if next_anchor < least_numpts and iterate == len(xvalues):
                print 'Found all possible lines with the given r value'
                break
            
            if next_anchor == yvalues.index(peak_load):
                anchor = yvalues[yvalues.index(peak_load)]
                anchor_pos = xvalues[0]
                group_pos = [anchor_pos] # first group of points to check in linear regression
                group_load = [anchor]
            else:
                group_pos = [next_anchor]
                group_load = [yvalues[next_anchor]]
            
            for index in range(0, next_anchor + 1, 1):
                group_pos.append(xvalues[index])
                group_load.append(yvalues[index])
            
            lengroup = len(group_pos)
        
            for point in range(0, lengroup - least_numpts, 1):
                if stop == 1:
                    break
        
                count = count + 1
                del group_pos[0:count] #deletes a value from the beginning of the array to check to see if the anchor point still works
                del group_load[0:count]
        
                if (len(group_load) - least_numpts < 0):
                    group_pos = []
                    group_load = []
                    for index in range(0, next_anchor+2, 1): #adds all the desired values to evaluate into an array
                        group_pos.append(xvalues[index])
                        group_load.append(yvalues[index])
                        break
                else:
                    xi = arange(min(group_pos), max(group_pos)+(max(group_pos)-min(group_pos))/(len(group_pos)), (max(group_pos)-min(group_pos))/(len(group_pos)))
                    slope, intercept, r_value, p_value, std_err = stats.linregress(group_pos,group_load)
                    r_value = abs(r_value)
                    rsq_value = r_value ** 2
                    
                    if rsq_value >= desired_rsqval: #checks to see if the rsq value is sufficient for the desired rsq value
                        line_num = line_num + 1 #keeps track of how many linear regressions have a sufficient rsq value
                        if line_num == 1:
                            print '\n Line 1 (closest to the peak): '
                        else:
                            print '\n Line %s: ' %(line_num)
                        print 'rsq value: ', rsq_value
                        print 'slope: %s (N/mm), or %s (N/m)' %(str(slope), str(slope*0.001))
                        print 'intercept: ', intercept
                        print 'y = %s * x + %s' %(str(slope), str(intercept))
                        print "Young's Modulus: %s" %(slope*length/area/10**6)
                        print 'Anchor index: ', next_anchor
                        print 'Number of points included: ', len(group_pos)
                        line = slope * xi + intercept #regression line
                        all_lines.append(xi) 
                        all_lines.append(line) #puts all the liner regressions into one array to prepare to be plotted
                        stop = 1
                        break
                    else:
                        group_pos = []
                        group_load = []
                        for index in range(0, next_anchor+1, 1): #remakes the arrays of values for a different anchor point since rsq value is not satisfied
                            group_pos.append(xvalues[index])
                            group_load.append(yvalues[index])
                 
                    if rsq_value < desired_rsqval and  point == lengroup - least_numpts:
                        if next_anchor < least_numpts:
                            print "Please rerun the program with a lower r value"
        index_anchor = next_anchor + 1 -len(group_pos)
 
print 'Found all possible lines with the given rsq value'

xi_all = arange(0, len(xvalues), 1)
plot(xvalues, yvalues, 'o') #plots all the points in the given ranges
        
for thing in range(0, line_num * 2, 2):
    plot(all_lines[thing], all_lines[thing+1], 'r-') #plots all the linear regressions
ylim ([min(yvalues), max(yvalues)]) #sets the y range of graph
xlim ([min(xvalues), max(xvalues)]) #sets the x range of graph
show()