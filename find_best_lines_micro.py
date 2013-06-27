# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:06:12 2013

@author: Adah
"""
#import import_data
from import_data import user_input

from numpy import arange #, array, ones
from pylab import plot, show
from scipy import stats

#def find_best_lines_micro():
values = user_input()
position = values

values = user_input()
load = values

max_load = max(load)
index_anchor = load.index(max_load)
anchor_num = 0
anchor_num2 = 0
count2 = 1

desired_rval = 0.98 #desired r value
least_numpts = 5 #at least this number of points in each linear regression

for next_anchor in range(index_anchor, -1, -1):
    count = 0
    anchor_num = anchor_num + 1
    
    if next_anchor == index_anchor:
        r_value1 = 0
        
    if r_value1 > desired_rval:
        break

    if next_anchor < least_numpts: #and r_value1 > desired_rval:
        print 'Please rerun the program with a lower r value or with a smaller number of minumum points'
        break
 
    anchor = load[0]
    anchor_pos = position[0]
    group1_pos = [anchor_pos] # first group of points in best linear regression (xvalues, position)
    group1_load = [anchor]

    for index in range(1, next_anchor + 1, 1):
        group1_pos.append(position[index])
        group1_load.append(load[index])
    
    lengroup1 = len(group1_pos)
#    print "group1_pos 1:"
#    print group1_pos
#    print "group1_load 1:"
#    print group1_load

    for point in range(0, lengroup1 - least_numpts, 1):

            
#        print "point: "
#        print point
#        print "next_anchor"
#        print next_anchor

        count = count + 1
        del group1_pos[0:count]
        del group1_load[0:count]
        
#        print "group1_pos del:"
#        print group1_pos 
#        print "group1_load del:"
#        print group1_load
#        else:
#            break

        
        if (len(group1_load) - least_numpts <= 0):# and (next_anchor == least_numpts - 1):
            group1_pos = []
            group1_load = []
            for index in range(0, next_anchor+1, 1):
                group1_pos.append(position[index])
                group1_load.append(load[index])
                break
        else:
            xi = arange(count + 1, index_anchor + 3 - anchor_num, 1)
            hold_count = count
    #        xi = arange(1, len(group1_pos)+1, 1)
#            print "xi"
#            print xi
            
            slope, intercept, r_value, p_value, std_err = stats.linregress(xi,group1_load)
            r_value1 = abs(r_value)
            slope1 = slope
            intercept1 = intercept
            
            if r_value1 > desired_rval:
                print 'Line 1'
                print 'r value: ', r_value1
                print 'slope: ', slope1
                print 'intercept: ', intercept1    
                print 'Anchor location: ', next_anchor
                print 'Number of points included: ', len(group1_pos)
                line1 = slope1 * xi + intercept1 #regression line
                #plot(xi, line1, 'r-', xi, group1_load, 'o') #group1_pos
                show()
                break
            else:
                group1_pos = []
                group1_load = []
                for index in range(0, next_anchor+1, 1):
                    group1_pos.append(position[index])
                    group1_load.append(load[index])
         
            if r_value1 < desired_rval and  point == lengroup1 - least_numpts:
                if next_anchor < least_numpts:
                    print "Please rerun the program with a lower r value"

index_anchor2 = next_anchor + 1 -len(group1_pos)

if index_anchor2 < least_numpts:
    plot(xi, line1, 'r-', xi, group1_load, 'o') #group1_pos
    show()
    print 'Only one linear regression required for the r value requirement'
else:
    for next_anchor2 in range(index_anchor2, -1, -1):
        count2 = 0
        anchor_num2 = anchor_num2 + 1
#        if len(position) - index_anchor2 < least_numpts:
#            print 'Only one linear regression required for the r value requirement'
#            break
    
        if next_anchor2 == index_anchor2:
            r_value2 = 0
            
        if r_value2 > desired_rval:
            break
    
        if next_anchor2 < least_numpts: #and r_value1 > desired_rval:
            print 'Please rerun the program with a lower r value or with a smaller number of minumum points'
            break
        
        anchor2 = load[0]
        anchor_pos2 = position[0]
        group2_pos = [anchor_pos2] # second group of points in best linear regression (xvalues, position)
        group2_load = [anchor2]
        
        for index2 in range(1, next_anchor2 + 1, 1):
            group2_pos.append(position[index2])
            group2_load.append(load[index2])
        
        lengroup2 = len(group2_pos)
        
        for point2 in range(0, lengroup2 - least_numpts, 1):
            
#            if point2 != (next_anchor2 - least_numpts):
            count2 = count2 + 1
            del group2_pos[0:count2]
            del group2_load[0:count2]
            
#            print "group2_pos del:"
#            print group2_pos 
#            print "group2_load del:"
#            print group2_load
                
            if (len(group2_load)-least_numpts <=0 ): #and (next_anchor == least_numpts - 1):
                group2_pos = []
                group2_load = []
                for index2 in range(0, next_anchor2+1, 1):
                    group2_pos.append(position[index2])
                    group2_load.append(load[index2])            
                break
            else:
            
                xi2 = arange(count2 + 1, index_anchor2 + 3 - anchor_num2, 1)
                hold_count2 = index_anchor2 + 3 - anchor_num2
#                print "xi2"
#                print xi2

                
                slope, intercept, r_value, p_value, std_err = stats.linregress(xi2, group2_load)
                r_value2 = abs(r_value)
                slope2 = slope
                intercept2 = intercept
                
                if r_value2 > desired_rval:
                    print 'Line 2'
                    print 'r value: ', r_value2
                    print 'slope: ', slope2
                    print 'intercept: ', intercept2 
                    print 'Anchor location: ', next_anchor2
                    print 'Number of points included: ', len(group2_pos)
                    line2 = slope2 * xi2 + intercept2 #regression line
                    #plot(xi2, line2, 'r-', xi2, group2_load, 'o') #group1_pos
#                    xi3 = arange(point2 - 2, 0, -1) 
                    
                    
                    if position.index(group2_pos[0]) < index_anchor2:
                        xi3 = arange(0, position.index(group2_pos[0]) + 1)
                        xi4 = arange(hold_count2, hold_count + 1)
                        plot(xi, group1_load, 'o', xi2, group2_load, 'o', xi3, load[0:position.index(group2_pos[0]) + 1], 'o', xi4, load[hold_count2: hold_count + 1], 'o', xi, line1, 'r-', xi2, line2, 'r-')
                        show()
                        break
                    elif position.index(group2_pos[0])>least_numpts: 
                        xi3 = arange(0, position.index(group2_pos[0]) + 1)
                        plot(xi, group1_load, 'o', xi, line1, 'r-', xi2, group2_load, 'o', xi2, line2, 'r-', xi3, load[0:position.index(group2_pos[0]) + 1], 'o')
                        show()
                        break
                    else:
                        plot(xi, group1_load, 'o', xi, line1, 'r-', xi2, group2_load, 'o', xi2, line2, 'r-')
                        show()
                        break
                else:
                    group2_pos = []
                    group2_load = []
                    for index2 in range(0, next_anchor2+1, 1):
                        group2_pos.append(position[index2])
                        group2_load.append(load[index2])
                if r_value2 < desired_rval and  point2 == 0:
                    if next_anchor2 < least_numpts:
                        print "Please rerun the program with a lower r value"
    
            
