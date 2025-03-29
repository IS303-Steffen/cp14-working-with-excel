from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ====================
# FORMATTING AND FONTS
# ====================

'''
OVERVIEW
--------
There's a lot that you can do with formatting your Worksheet. This will just
show some basic font styling (bold) and adjusting the width of columns.
'''
import openpyxl
from openpyxl.styles import Font # if you want to adjust the fonts


'''
STARTER WORKBOOK CODE:
'''
my_workbook = openpyxl.Workbook() #Make a new Workbook by calling the Workbook() constructor=
my_workbook.active.title = "Classes" # change the title of the default sheet to "Students"

# Add something to the first row, like Name and then Grade.
my_workbook.active["A1"] = "Class Name" 
my_workbook.active["B1"] = "Department"

# add stuff to the second row
my_workbook.active["A2"] = "IS 303" 
my_workbook.active["B2"] = "Information Systems"
my_workbook.active["A3"] = "ACC 200" 
my_workbook.active["B3"] = "Accounting"


# ==============
# ALTERING FONTS
# ==============


# 1. BOLDING A CELL
# Get access to a cell, access it's .font attribute, and then set it
# equal to a Font object with the parameter bold=True.


'''
Because .font is an attribute of cell objects, you can only change it by
accessing individual cells. If you want to do it to multiple cells, that means
using a loop.
'''

# 2. BOLDING A RANGE OF CELLS
# Use a loop to bold the range of A1 to B2

   
'''
Notice how when you bold something you're creating a Font class and setting
that equal to the .font variable of the cell? If you want, you can just create
a Font object with all the font specifics you want and apply it to whatever
you want.

Below, is an example using italic, the font name, size, color, and underline.
Look up more in your textbook or online if this interests you.
'''
# 3. FANCIER FONTS (EXAMPLE PROVIDED TO YOU)
# example_fancy_font = Font(italic=True, name = "Times New Roman", size=20,
#                           color='FF0000', underline='single')

# # apply this font to A3:B3
# range_of_cells = my_workbook.active["A3:B3"]
# for row in range_of_cells:
#     for cell in row:
#         cell.font = example_fancy_font


# =====================
# CHANGING COLUMN WIDTH
# =====================
'''
OVERVIEW
--------
The column width is set with an integer. The integer represents the number of
characters of the standard font. The standard font in excel is usually Calibri
size 11.

SYNTAX
------
sheet.column_dimensions['column letter'].width = <integer>
'''

# 4. CHANGE THE WIDTH OF A COLUMN
# set the width of column A of the active sheet to 30:


# 5. CHANGE THE WIDTH TO DYNAMICALLY MATCH THE LENGTH
# Set the width of column B equal to the number of characters in cell B2 + 10


'''
TIP
---
You can also adjust the height of the rows. 1 unit is = to 1/72 of an inch
my_workbook.active.row_dimensions[1].height = 20
'''

# SAVE THE WORKBOOK AS example_07.xlsx
my_workbook.save(filename="example_07.xlsx")
my_workbook.close()