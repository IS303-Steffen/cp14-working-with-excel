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
Practice:

Import the mock_grades file.

PART 1:
    Change the grade of anyone with a "C-" to be an "F" on the active sheet.
    Save the results as a new workbook called "mock_grades_altered"

PART 2:
    If you can successfully do that, then alter your code to change "C-" to "F" on all of the sheets
    in mock_grades. Save the results as a new workbook called "mock_grades_altered"

'''
