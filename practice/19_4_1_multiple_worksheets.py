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

# importing openpyxl


#Make a new Workbook by calling the Workbook() constructor. Workbook is a class inside the openpyxl library


# you can use .title to get the title of a sheet. What is the title of the active sheet?
# remember my_workbook.active


# change the title of the default sheet to "Students"


# create another sheet called "Classes" using .create_sheet("Sheet name")


# note: you can also remove a sheet using .remove, but I won't do that now.

#change the active sheet to classes. Access a specific sheet using my_workbook["Sheet Name"]


# Add something to the first row, like Class Name and then Department.
# Use square brackets to access a position in the sheet, like ["A1"]


# add stuff to the second row


# put the cell A2 in a variable called cell


# for any cell, you can access its value, row, column, and coordinate (column and row)
# print out each of those (use .value to get the value, etc.)


# you can use the .cell(row_number, column number) if you don't know the exact letter of the column you want
# unlike Pandas, this starts with 1 instead of 0.
# try printing the value of the 1st row, 2nd column.


# note you can also access sheets that aren't the active sheet
# by using my_workbook["Sheet Name"]["Coordinate (like A1, etc.)"]
# Try changing the "Students" sheet so that the A1 value says "Name"


# other useful things, on a worksheet, you can use .max_row to get the furthest row with data, same with .max_col

# use .save(filename = "filename.xlsx") to actually create a file
# create an excel file named example2
