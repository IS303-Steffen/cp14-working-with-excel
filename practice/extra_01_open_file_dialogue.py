import tkinter as tk
from tkinter import filedialog

# Create the Tk root widget
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file dialog and store the selected file path
file_path = filedialog.askopenfilename(title="Select a file")

# Print the selected file path (or use it as needed)
print("Selected file path:", file_path)