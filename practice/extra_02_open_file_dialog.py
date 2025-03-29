from helper_functions import clear_screen
clear_screen() # This just clears the terminal window each time we run code

# ===============================
# EXTRA - USE AN OPEN FILE DIALOG
# ===============================

'''
OVERVIEW
--------
If you wanted to choose an Excel file more like a traditional program,
instead of writing out the path to the file, you could also launch a file
dialog (a window to choose a file or option) and get the file path that way.

To do this, you can use tkinter ("tee-kay inter") which is a GUI (graphical
user interface) library built into Python in the standard library. Building
GUIs is a whole rabbit hole that we won't get into in this class, but feel
free to look at the example below.
'''

import tkinter as tk
from tkinter import filedialog

# Create the Tk root widget
root = tk.Tk()
root.withdraw() # Hide the root window

# Open the file dialog and store the selected file path
file_path = filedialog.askopenfilename(title="Select a file")


# Print the selected file path (or use it as needed, like
# importing it into openpyxl, etc.
print("Selected file path:", file_path)

# Let's say you want to to save a file as something, this lets you choose
# the file path where it should save.
file_path_to_save_to = filedialog.asksaveasfilename(
    title="Where to save to?",
    filetypes=[("Excel files", "*.xlsx")])

print("Selected file path to save to:", file_path_to_save_to)