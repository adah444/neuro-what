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
    input_range = raw_input("Enter your range (e.g. A1:A6): ")
    print "Please wait."

#def file_import():
    wb = openpyxl.reader.excel.load_workbook(file_name)
    s = wb.get_sheet_by_name(name= ws_name)
    c = s.range(input_range) 
    values=[]
    for row in c:
        for cell in row:
            values.append(cell.value)
    return values
    #pprint(values)
