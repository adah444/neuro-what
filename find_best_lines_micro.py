# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:55:18 2013

@author: Adah
"""
#import import_data
from import_data import user_input

from numpy import arange #, array, ones
from pylab import plot, show, ylim, xlim
from scipy import stats

values = user_input()
position = values

values = user_input()
load = values

minmax = raw_input ("Is the peak at a min or a max?: ")
if minmax == 'max':
    peak_load = max(load)
    index_anchor = load.index(peak_load)
else:  
    peak_load = min(load)
    index_anchor = load.index(peak_load)
    
anchor_num = 0
line_num = 0
all_lines = []

desired_rval = 0.996 #desired r value
least_numpts = 3 #at least this number of points in each linear regression

for iterate in range(0, len(position)):
    if index_anchor > least_numpts - 1:
        stop = 0
        for next_anchor in range(index_anchor, -1, -1):
            count = 0
            anchor_num = anchor_num + 1
            if stop == 1:
                break
            
            if next_anchor == index_anchor:
                r_value1 = 0
                
            if r_value1 > desired_rval:
                break
        
            if next_anchor < least_numpts: #and r_value1 > desired_rval:
                print 'Found all possible lines with the given r value'
                break
            
            if next_anchor == load.index(peak_load):
                anchor = load[0]
                anchor_pos = position[0]
                group_pos = [anchor_pos] # first group of points in best linear regression (xvalues, position)
                group_load = [anchor]
            else:
                group_pos = [next_anchor]
                group_load = [load[next_anchor]]
        
            for index in range(1, next_anchor + 1, 1):
                group_pos.append(position[index])
                group_load.append(load[index])
            
            lengroup = len(group_pos)
        
            for point in range(0, lengroup - least_numpts, 1):
                if stop == 1:
                    break
        
                count = count + 1
                del group_pos[0:count]
                del group_load[0:count]
        
                if (len(group_load) - least_numpts <= 0):# and (next_anchor == least_numpts - 1):
                    group_pos = []
                    group_load = []
                    for index in range(0, next_anchor+1, 1):
                        group_pos.append(position[index])
                        group_load.append(load[index])
                        break
                else:
                    xi = arange(position.index(group_pos[0]), position.index(group_pos[len(group_pos)-1]) + 1, 1)
                    hold_count = count
        
                    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,group_load)
                    r_value = abs(r_value)
                    
                    if r_value > desired_rval:
                        line_num = line_num + 1
                        print 'Line', line_num
                        print 'r value: ', r_value
                        print 'slope: ', slope
                        print 'intercept: ', intercept
                        print 'Anchor location: ', next_anchor
                        print 'Number of points included: ', len(group_pos)
                        line = slope * xi + intercept #regression line
                        all_lines.append(xi)
                        all_lines.append(group_load)
                        all_lines.append(xi)
                        all_lines.append(line)
                        stop = 1
                        break
                    else:
                        group_pos = []
                        group_load = []
                        for index in range(0, next_anchor+1, 1):
                            group_pos.append(position[index])
                            group_load.append(load[index])
                 
                    if r_value < desired_rval and  point == lengroup - least_numpts:
                        if next_anchor < least_numpts:
                            print "Please rerun the program with a lower r value"
        index_anchor = next_anchor + 1 -len(group_pos)
 
print 'Found all possible lines with the given r value'
        
for thing in range(0, line_num * 4, 4):
    plot(all_lines[thing], all_lines[thing+1], 'o', all_lines[thing+2], all_lines[thing+3],'r-')
ylim ([0, peak_load])
xlim ([0, load.index(peak_load)])
show()

#if index_anchor2 < least_numpts:
#    plot(xi, line, 'r-', xi, group_load, 'o') #group1_pos
#    show()
#    print 'Only one linear regression required for the r value requirement'
#else:
#    for next_anchor2 in range(index_anchor2, -1, -1):
#        count2 = 0
#        anchor_num2 = anchor_num2 + 1
#    
#        if next_anchor2 == index_anchor2:
#            r_value2 = 0
#            
#        if r_value2 > desired_rval:
#            break
#    
#        if next_anchor2 < least_numpts: #and r_value1 > desired_rval:
#            print 'Please rerun the program with a lower r value or with a smaller number of minumum points'
#            break
#        
#        anchor2 = load[0]
#        anchor_pos2 = position[0]
#        group2_pos = [anchor_pos2] # second group of points in best linear regression (xvalues, position)
#        group2_load = [anchor2]
#        
#        for index2 in range(1, next_anchor2 + 1, 1):
#            group2_pos.append(position[index2])
#            group2_load.append(load[index2])
#        
#        lengroup2 = len(group2_pos)
#        
#        for point2 in range(0, lengroup2 - least_numpts, 1):
#
#            count2 = count2 + 1
#            del group2_pos[0:count2]
#            del group2_load[0:count2]
#
#            if (len(group2_load)-least_numpts <=0 ): #and (next_anchor == least_numpts - 1):
#                group2_pos = []
#                group2_load = []
#                for index2 in range(0, next_anchor2+1, 1):
#                    group2_pos.append(position[index2])
#                    group2_load.append(load[index2])            
#                break
#            else:
#            
#                xi2 = arange(count2 + 1, index_anchor2 + 3 - anchor_num2, 1)
#                hold_count2 = index_anchor2 + 3 - anchor_num2
#                
#                slope, intercept, r_value, p_value, std_err = stats.linregress(xi2, group2_load)
#                r_value2 = abs(r_value)
#                slope2 = slope
#                intercept2 = intercept
#                
#                if r_value2 > desired_rval:
#                    print 'Line 2'
#                    print 'r value: ', r_value2
#                    print 'slope: ', slope2
#                    print 'intercept: ', intercept2 
#                    print 'Anchor location: ', next_anchor2
#                    print 'Number of points included: ', len(group2_pos)
#                    line2 = slope2 * xi2 + intercept2 #regression line
#                    
#                    if position.index(group2_pos[0]) < index_anchor2:
#                        xi3 = arange(0, position.index(group2_pos[0]) + 1)
#                        xi4 = arange(hold_count2, hold_count + 1)
#                        plot(xi, group1_load, 'o', xi2, group2_load, 'o', xi3, load[0:position.index(group2_pos[0]) + 1], 'o', xi4, load[hold_count2: hold_count + 1], 'o', xi, line1, 'r-', xi2, line2, 'r-')
#                        show()
#                        break
#                    elif position.index(group2_pos[0])>least_numpts: 
#                        xi3 = arange(0, position.index(group2_pos[0]) + 1)
#                        plot(xi, group1_load, 'o', xi, line1, 'r-', xi2, group2_load, 'o', xi2, line2, 'r-', xi3, load[0:position.index(group2_pos[0]) + 1], 'o')
#                        show()
#                        break
#                    else:
#                        plot(xi, group1_load, 'o', xi, line1, 'r-', xi2, group2_load, 'o', xi2, line2, 'r-')
#                        show()
#                        break
#                else:
#                    group2_pos = []
#                    group2_load = []
#                    for index2 in range(0, next_anchor2+1, 1):
#                        group2_pos.append(position[index2])
#                        group2_load.append(load[index2])
#                if r_value2 < desired_rval and  point2 == 0:
#                    if next_anchor2 < least_numpts:
#                        print "Please rerun the program with a lower r value"