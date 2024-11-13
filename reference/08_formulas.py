import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ========
# FORMULAS
# ========

'''
OVERVIEW
--------
To add formulas in openpyxl, just manually type them out.
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
myWorkbook = openpyxl.Workbook()

#Return the active worksheet and store it to currWS
currWS = myWorkbook.active

#Change the worksheet title
currWS.title = "Customers"

cols = ["A", "B", "C", "D", "E", "F"]

#Create random data for 6 columns and 10 rows
for iRow in range(1, 11):
    for iCol in range(6):     
        #Use the cols array and the iCol counter to return the column (i.e. "A")
        #Then concatenate it to the counter to create a column row value (i.e. "A1")          
        currWS[cols[iCol] + str(iRow)] = random.randint(0,100)

'''
To put in formulas, just type them like you would in Excel, no difference.
Recommended to use ' instead of " because in the excel formulas you MUST use "
'''

# sum up A1:A10 and put it in A13
currWS["A12"] = 'SUM'
currWS["A13"] = '=SUM(A1:A10)'

# find min of B1:B10 and put it in B13
currWS["B12"] = 'MIN'
currWS["B13"] = '=MIN(B1:B10)'

# find max of C1:C10 and put it in C13
currWS["C12"] = 'MAX'
currWS["C13"] = '=MAX(C1:C10)'

# count D1:D10 and put it in D13
currWS["D12"] = 'COUNT'
currWS["D13"] = '=COUNT(D1:D10)'

# find average of E1:E10 and put it in E13
currWS["E12"] = 'AVERAGE'
currWS["E13"] = '=AVERAGE(E1:E10)'

# use COUNTIF to see the number of numbers above 50 in F1:F10 and put it in F13
currWS["F12"] = 'COUNTIF'
currWS["F13"] = '=COUNTIF(F1:F10, "> 50")'

myWorkbook.save(filename="example4.xlsx")      
myWorkbook.close()