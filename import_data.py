# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:17:34 2013

@author: Adah
"""

import openpyxl
#from pprint import pprint
    
def user_input():
    
    file_name =  raw_input ("Enter the complete file name (xlsx): ")
    ws_name = raw_input ("Enter the worksheet name: ")
    input_xrange = raw_input("Enter your x range (e.g. A1:A6): ")
    input_yrange = raw_input("Enter your y range (e.g. B1:B6): ")
    print "Please wait."

    wb = openpyxl.reader.excel.load_workbook(file_name)
    s = wb.get_sheet_by_name(name= ws_name)
    c = s.range(input_xrange) 
    d = s.range(input_yrange)
    xvalues=[]
    yvalues=[]
    
    for row in c:
        for cell in row:
            xvalues.append(cell.value)

    for row in d:
        for cell in row:
            yvalues.append(cell.value)
            
    return xvalues, yvalues
