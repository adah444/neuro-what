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

desired_rsqval = 0.998 #desired r value
least_numpts = 4 #at least this number of points in each linear regression

for iterate in range(0, len(position)):
    if index_anchor > least_numpts - 1:
        print 'index anchor', index_anchor
        stop = 0
        for next_anchor in range(index_anchor, -1, -1):
            count = 0
            anchor_num = anchor_num + 1
            if stop == 1:
                break
            
            if next_anchor == index_anchor:
                r_value1 = 0
                
            if r_value1**2 >= desired_rsqval:
                break
        
            if next_anchor < least_numpts and iterate == len(position):
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
                    xi = arange(position[position.index(group_pos[0])], position[position.index(group_pos[len(group_pos)-1]) - 1], (position[position.index(group_pos[len(group_pos)-1]) -1]-position[position.index(group_pos[0])])/len(group_pos))
                    #xi = arange(position.index(group_pos[0]), position.index(group_pos[len(group_pos)-1]) + 1, 1)
                    hold_count = count
        
                    slope, intercept, r_value, p_value, std_err = stats.linregress(group_pos,group_load)
                    #group_load_m = map(lambda x: x*0.001, group_load) #all thegroup_load values in meters
                    #slope, intercept, r_value, p_value, std_err = stats.linregress(group_pos,group_load_m)
                    r_value = abs(r_value)
                    rsq_value = r_value ** 2
                    
                    if rsq_value >= desired_rsqval:
                        line_num = line_num + 1
                        if line_num == 1:
                            print 'Line 1 (closest to the peak)'
                        else:
                            print 'Line', line_num
                        print 'rsq value: ', rsq_value
                        print 'slope: (N/mm)', slope
                        print 'slope: (N/m)', slope*0.001
                        print 'intercept: ', intercept
                        print 'Anchor location: ', next_anchor
                        print 'Number of points included: ', len(group_pos)
                        line = slope * xi + intercept #regression line
                        all_lines.append(group_pos)
                        all_lines.append(group_load)
                        all_lines.append(xi)
                        all_lines.append(line)
#                        all_lines.append(xi)
#                        all_lines.append(group_load)
#                        all_lines.append(xi)
#                        all_lines.append(line)
                        stop = 1
                        break
                    else:
                        group_pos = []
                        group_load = []
                        for index in range(0, next_anchor+1, 1):
                            group_pos.append(position[index])
                            group_load.append(load[index])
                 
                    if rsq_value < desired_rsqval and  point == lengroup - least_numpts:
                        if next_anchor < least_numpts:
                            print "Please rerun the program with a lower r value"
        index_anchor = next_anchor + 1 -len(group_pos)
 
print 'Found all possible lines with the given r value'

xi_all = arange(0, len(position), 1)
plot(position, load, 'o')
        
for thing in range(0, line_num * 4, 4):
    #xi_all = arange(0, len(position), 1)
    #plot(xi_all, load, 'o')
    plot(all_lines[thing+2], all_lines[thing+3],'r-') #all_lines[thing], all_lines[thing+1], 'o',
ylim ([min(load), max(load)])
#xlim ([0, load.index(peak_load)])
xlim ([min(position), max(position)])
show()