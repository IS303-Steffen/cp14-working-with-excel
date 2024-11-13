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

# ===============================
# LOOPING THROUGH SHEETS PRACTICE
# ===============================

# 1. PRACTICE LOOPING
'''
Import the mock_grades file.

PART 1:
    Change the grade of anyone with a "C-" to be an "F" on the active sheet.
    Save the results as a new workbook called "mock_grades_altered.xlsx"

PART 2:
    If you can successfully do that, then alter your code to change "C-" to "F"
    on ALL of the sheets in mock_grades. Save the results to
    "mock_grades_altered.xlsx"

'''
