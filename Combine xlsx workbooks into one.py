# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:57:05 2013

@author: Adah
"""

from xlsxwriter.workbook import Workbook

# Create an new Excel file and add a worksheet.
workbook = Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to highlight cell text.
bold = workbook.add_format({'bold': 1})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

workbook.close()