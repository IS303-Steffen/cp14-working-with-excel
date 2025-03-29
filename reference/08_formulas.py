from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ========
# FORMULAS
# ========

'''
OVERVIEW
--------
To add formulas in openpyxl, just manually type out what you would type out
in the Excel Workbook, like: =SUM(A1:A10)
'''

import openpyxl
import random

'''
STARTER CODE
------------
The code here is just generating random numbers to fill up columns A to F
with 10 numbers
'''
#Create a new Workbook
my_workbook = openpyxl.Workbook()
current_ws = my_workbook.active
current_ws.title = "Customers"
cols = ["A", "B", "C", "D", "E", "F"]

for col_letter in cols: 
    for i_row in range(1, 11):
        # add a random number to a specific cell, like A1, B2, etc.
        current_ws[f"{col_letter}{i_row}"] = random.randint(0,100)

'''
To put in formulas, just type them like you would in Excel, no difference.
I recommend you use ' instead of " to start your strings, because in the excel
formulas you MUST use "
'''

# sum up A1:A10 and put it in A13
current_ws["A12"] = 'SUM'
current_ws["A13"] = '=SUM(A1:A10)'

# find min of B1:B10 and put it in B13
current_ws["B12"] = 'MIN'
current_ws["B13"] = '=MIN(B1:B10)'

# find max of C1:C10 and put it in C13
current_ws["C12"] = 'MAX'
current_ws["C13"] = '=MAX(C1:C10)'

# count D1:D10 and put it in D13
current_ws["D12"] = 'COUNT'
current_ws["D13"] = '=COUNT(D1:D10)'

# use COUNTIF to see the number of numbers above 50 in E1:E10 and put it in E13
current_ws["E12"] = 'COUNTIF'
current_ws["E13"] = '=COUNTIF(E1:E10, "> 50")'

current_ws["F12"] = 'AVERAGE'
current_ws["F13"] = '=AVERAGE(F1:F10)'

my_workbook.save(filename="example_08.xlsx")      
my_workbook.close()

# 1. ADD AN AVERAGE FUNCTION
# Before the lines of code that save the workbook, find average of F1:F10 and
# by using the AVERAGE function. Put the result in cell F13

''' See solution above '''