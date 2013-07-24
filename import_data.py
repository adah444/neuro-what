# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:17:34 2013

@author: Adah
"""

import openpyxl

def user_input():
    
    file_name =  raw_input ("Enter the complete file name (xlsx): ")
    print "Please wait."

    wb = openpyxl.reader.excel.load_workbook(file_name)
    wksheets = wb.worksheets
    for index in range(0, len(wksheets)):
        c = wksheets[index].range("J2:J400")
        d = wksheets[index].range("I2:I400")
        if index == 0:
            xvalues=[]
            yvalues=[]
        
        for row in c:
            for cell in row:
                xvalues.append(cell.value)
    
        for row in d:
            for cell in row:
                yvalues.append(cell.value)
                
    return xvalues, yvalues, len(wksheets), wksheets
