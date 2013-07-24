# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:55:18 2013

@author: Adah
"""

from import_data import user_input


from numpy import arange
from pylab import plot, show, ylim, xlim, xlabel, ylabel, grid, title
from scipy import stats

import math

desired_rsqval = 0.998 #input your desired r value
least_numpts = 4 #input the desired least number of points required in a linear regression

length = 6.0 #input the scaffold length (in mm)
pi = math.pi
outer_diam = 2.47 #input the outer diameter of the scaffold (in mm)
inner_diam = 1.806 #input the inner diameter of the scaffold (in mm)
area = pi * ((outer_diam/2/1000)**2 - (inner_diam/2/1000)**2) #if there is an inner and outer diameter
#diam = 3.8 #input the diameter if there is no inner/outer diameter (in mm)
#area = pi * (diam/2/1000)**2 #if there is only one diameter (in mm)

print '\nTo define: '
print '\nrsq value is the coefficient of determination. It indicates how well the data fits to the linear regressions. The closer the rsq value is to 1, the better the linear fit is.'
print '\np-value is the probability of obtaining a result that is more extreme. The closer the p-value is to zero, the better the linear fit is.'
print '\nstandard error is the estimate of sampling errors affecting the linear regression. Larger standard errors indicate lower significance of the linear regression.' 

values = user_input() #prompts the user for the file name and ranges over which to analyze
xval = values[0] 
yval = values[1]
numworksheets = values[2]
wksheetnames = values[3]

sheetnum = 0

iterated = len(xval)/numworksheets
for num in range(0, len(xval) - iterated, iterated):
    xvalues = []
    yvalues = []
    for num1 in range (num, num + iterated):
        xvalues.append(xval[num1])
        yvalues.append(yval[num1])

    max_load = max(yvalues)
    min_load = min(yvalues)
    if abs(max(yvalues)) > abs(min(yvalues)): #determines if the peak is a max or a min
        peak_load = max(yvalues)
        index_anchor = yvalues.index(peak_load)
    else:
        peak_load = min(yvalues)
        index_anchor = yvalues.index(peak_load)
         
    line_num = 0 #keeps track of how many linear regressions have a sufficient rsq value
    all_lines = [] #initializes the array that will contain all the linear regressions
    
    for iterate in range(0, len(xvalues)):
        if index_anchor > least_numpts - 1:
            stop = 0
            for next_anchor in range(index_anchor, -1, -1): #checks each anchor to see if the values are sufficient for the rsq value in the linear regression
                count = 0
                if stop == 1:
                    break
                
                if next_anchor == index_anchor: #initializes r_value so that the one can break out of the oop when the desire rsq value is achieved
                    r_value = 0
                    
                if r_value**2 >= desired_rsqval: #break out of the oop when the desired rsq value is achieved
                    break
            
                if next_anchor < least_numpts and iterate == len(xvalues): #lets the user know that the loop has terminated and all the possibe regression lines have been found
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
                                print '\n', wksheetnames[sheetnum]
                                print '\n Line 1 (closest to the peak): '
                            else:
                                print '\n Line %s: ' %(line_num)
                            print 'y = %s * x + %s' %(str(slope), str(intercept))                        
                            print 'rsq value: ', rsq_value     
                            print 'p-value: ', p_value
                            print 'standard error: ', std_err
                            print 'slope: %s (N/mm), or %s (N/m)' %(str(slope), str(slope*0.001))
                            print 'intercept: ', intercept
                            print "Young's Modulus: %s MPa" %(slope*length/area/10**6)
                            print "Peak value at: %s Newtons, %s mm" %(peak_load, xvalues[index_anchor])
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
     
    print '\nFound all possible lines with the given rsq value.'
    
    xi_all = arange(0, len(xvalues), 1)
    plot(xvalues, yvalues, 'o') #plots all the points in the given ranges
            
    for thing in range(0, line_num * 2, 2):
        plot(all_lines[thing], all_lines[thing+1], 'r-') #plots all the linear regressions
    title(wksheetnames[sheetnum])
    ylim ([min(yvalues), max(yvalues)]) #sets the y range of graph
    xlim ([min(xvalues), max(xvalues)]) #sets the x range of graph
    xlabel("Millimeters")
    ylabel("Newtons")
    grid(True)
    show()
    sheetnum = sheetnum + 1