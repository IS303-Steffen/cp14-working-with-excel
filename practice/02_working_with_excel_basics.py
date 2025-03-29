from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ===========================
# WORKING WITH EXCEL - BASICS
# ===========================

'''
OVERVIEW
--------
openpyxl lets you create Workbook objects.
A workbook is just like an Excel document. A "Workbook" is the name of the
whole document. A Workbook can have many different "Worksheets" (like the tabs
of different sheets in excel)

Columns are named A, B, C, D, E, etc.
Rows are named 1, 2, 3, 4, 5

When you make a Workbook, you get a default Worksheet called "Sheet"
In Excel, the sheet you are currently viewing is called the "active sheet". You
can also access the active sheet in openpyxl by doing .active

VIEWING EXCEL IN VS CODE
------------------------
You might find it useful to install the "Excel Viewer" extension in VS Code
so that you can open up .xlsx files directly in VS Code. Just BEWARE: You'll
need to close the file each time you make changes in order to see the changes.
You also will NOT see formatting changes there. To see formatting changes, open
up the file in Excel.
'''

# 1. IMPORT openpyxl
# Import openpyxl so we can make Workbook objects


# 2. CALL THE WORKBOOK CONSTRUCTOR
# Using openpyxl, call the Workbook() constructor to make a Workbook object.
# Store the Workbook object in a variable


# 3. STORE THE ACTIVE WORKSHEET
# You can get the active Worksheet through .active
# Store the active Worksheet in a variable


# 4. EDIT CELL VALUES IN YOUR WORKSHEET
# Using the variable holding the active Worksheet, use square brackets with
# a column letter and row number to edit a specific cell, like ["A1"]
# Add something to the first row of the active sheet, like Name and then Grade.
# Then something to the second row.


# 5. SAVE YOUR WORKBOOK
# Use .save("filename.xlsx") to actually create an Excel file.
# Create an Excel file named example_02. It will save in whatever folder you
# have open in VS Code / where you are running your code, unless you specify a
# different location on your computer.



'''
IMPORTANT
---------
If you save a workbook, open it up, and then save a new version of the workbook,
you won't see the changes until you close the workbook you opened up.
'''

# 6. CLOSE THE WORKBOOK
# Use .close() on the Workbook to free up memory for your computer if you are
# running more code after you save the Workbook. It also helps prevent problems
# like the file getting corrupted
