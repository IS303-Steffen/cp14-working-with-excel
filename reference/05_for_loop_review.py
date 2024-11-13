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

# ===============
# FOR LOOP REVIEW
# ===============

'''
OVERVIEW
--------
Workbooks are easier to work with if you remember looping through nested lists.
This is a review

'''

# 1. PRINT OUT EACH ELEMENT IN LIST
# Print out each element in the example_list variable
example_list = ["Hello", "this", "is", "a", "list"]

for element in example_list:
    print(element)

# 2. PRINT OUT EACH ELEMENT IN LIST 2
# Print out each element in example_list_2. What is each element?
example_list_2 = [["first", "list", "inside", "list"], ["second", "list", "inside", "list"], ["third", "list", "inside", "list"]]

for element in example_list_2:
    print(element)

# 3. PRINT OUT THE FIRST ELEMENT OF EACH INNER ELEMENT:
# Using example_list_2, print out the first element of each inner list:
for element in example_list_2:
    print(element[0])

# 4. PRINT OUT EACH INDIVIDUAL ELEMENT OF EACH INNER ELEMENT
for element in example_list_2:
    for inner_element in element:
        print(inner_element)