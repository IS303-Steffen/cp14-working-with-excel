# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

from openpyxl.styles import Font # if you want to adjust the fonts
from openpyxl import Workbook

# code
myWorkbook = Workbook() #Make a new Workbook by calling the Workbook() constructor=
myWorkbook.active.title = "Classes" # change the title of the default sheet to "Students"

# Add something to the first row, like Name and then Grade.
myWorkbook.active["A1"] = "Class Name" 
myWorkbook.active["B1"] = "Department"

# add stuff to the second row
myWorkbook.active["A2"] = "IS 303" 
myWorkbook.active["B2"] = "Information Systems"
myWorkbook.active["A3"] = "ACC 200" 
myWorkbook.active["B3"] = "Accounting"

'''
See section 19.7 for lots of examples.
For your project you just need to know bolding and adjusting the width so I'll focus on those
'''

# bolding:
# any font options (like bold) has to be done on a per cell basis:

# you can do it directly by accessing the sheet and then give it a range
# then use .font and add a font object.


# or this is the exact same thing:
cellExample = myWorkbook.active["A1"]

cellExample.font = Font(bold = True)

# let's say you want to do it to A1:B2.
# you'd either hard code it one by one, or loop through the range:
rangeOfCells = myWorkbook.active["A1:B2"]

for row in rangeOfCells:
    for cell in row:
        cell.font = Font(bold = True)
   


# Notice how when you bold something you're creating a Font class and setting that equal to the .font variable of the cell?
# if you want, you can just create a Font object with all the font specifics you want and apply it to whatever you want

# here, I'm using italic, the font name, size, color, and underline.
# if you want details on these, look at 19.7 in your textbook, or look it up online. We won't spend much time going into the specifics.
exampleFont = Font(italic=True, name = "Times New Roman", size=20, color='FF0000', underline='single')

# apply this font to A3:B3
rangeOfCells = myWorkbook.active["A3:B3"]

for row in rangeOfCells:
    for cell in row:
        cell.font = exampleFont



# width of the cells:

# column width
'''
The column width is set with an integer. The integer represents the number of characters of the standard font.
The standard font in excel is usually Calibri size 11.

Change it like this:
# workbookName.sheetName.column_dimensions['columnLetterHere'].width = #ofCharactersWidth
'''

# set the width of column A to 30:
myWorkbook.active.column_dimensions["A"].width = 30

# set the width of column B equal to the number of characters in cell B2 + 10
B2Cell = myWorkbook.active["B2"]
B2CellValue = B2Cell.value
lengthOfB3 = len(B2CellValue)

myWorkbook.active.column_dimensions["B"].width = lengthOfB3 + 10

'''
You can also adjust the height of the rows. 1 unit is = to 1/72 of an inch

myWorkbook.active.row_dimensions[1].height = 20

'''

# saving the workbook
myWorkbook.save(filename="example3.xlsx")
myWorkbook.close()