from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ===============
# ADDING A FILTER
# ===============

'''
OVERVIEW
--------
Filters on Excel sheets make it easier to rearrange data. You can add a filter
to a range with one line of code. Just note that you won't see filters on 
Workbooks inside VS Code, you'll need to open the workbook in Excel to see the
effects.
'''

import openpyxl

external_workbook = openpyxl.load_workbook("mock_grades.xlsx")

# 1. ADD A FILTER TO A RANGE
# Using the workbook imported above, add a filter to the active sheet on range
# A1:B11. Use auto_filter.ref = 'A1:B11'
# Then save the workbook as example_09.xlsx

external_workbook.active.auto_filter.ref = 'A1:B11'

external_workbook.save(filename="example_09.xlsx")
external_workbook.close()