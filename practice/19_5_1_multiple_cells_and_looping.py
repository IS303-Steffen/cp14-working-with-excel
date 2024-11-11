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

import openpyxl

# load in mock_grades again
external_workbook = openpyxl.load_workbook("mock_grades.xlsx")

# optionally store the active worksheet in a new variable

# use .iter_rows() in a for loop to get all the rows. print out the row object (not useful yet)


# use values_only = True to only return the values of the row. print out the whole row


# now print out each individual cell. Use values_only = true. Remember in each row, there are multiple cells


# Do the same thing, but now do not use values_only = True.
# For every cell, print out the coordinate (use .coordinate on the cell) and the value (use .value)


# you can use min_row, min_col, max_col, max_row to only go through a section of the worksheet
# only get the first 10 rows of the 2nd and 3rd columns


# Could also get the specific cells you want with a coordinate range like curentSheet["A1:B51"] and loop through that.

