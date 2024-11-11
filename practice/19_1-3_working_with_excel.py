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


'''
openpyxl lets you create Workbook objects
A workbook is just like an excel document. Workbook is the name of the whole document.
A Workbook can have many different "worksheets" (like the tabs of different sheets in excel)

Columns are named A, B, C, D, E, etc.
Rows are named 1, 2, 3, 4, 5

When you make a Workbook, you get a default Worksheet called "Sheet"
In excel, the sheet you are currently viewing is called the "active sheet". You can also access
the active sheet in openpyxl by doing .active

'''

# make sure to import openpyxl


#Make a new Workbook by calling the Workbook() constructor through openpyxl


# you can get the active worksheet through .active
# you can also store the .active worksheet in another variable if you want



# Add something to the first row of the active sheet, like Name and then Grade.
# Use square brackets to access a position in the sheet, like ["A1"]

# add stuff to the second row


# use .save(filename = "filename.xlsx") to actually create a file
# create an excel file named example1
# it will save in whatever folder you have open in VS Code / where you are running your code.
# unless you specify a different location on your computer.

'''IMPORTANT!!'''
# If you save a workbook, open it up, and then save a new version of the workbook,
# you won't see the changes until you close the workbook you opened up.

# use .close() on the workbook to free up memory for your computer,
# helps prevent problems like the file getting corrupted
