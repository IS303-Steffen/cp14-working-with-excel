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


# review of for loops:

exList = ["Hello", "this", "is", "a", "list"]

# write a for loop that prints out everything in the list
for thing in exList:
    print(thing)

# this is a list, with a list stored in each slot:
exList2 = [["first", "list", "inside", "list"], ["second", "list", "inside", "list"], ["third", "list", "inside", "list"]]

# write a for loop that prints out the first list (all at once), then the second list (all at once), etc.
for thing in exList2:
    print(thing)

# now write a for loop that prints out each individual element of the inner lists (e.g. print "first". then print "list", then "inside", etc.)
for thing in exList2:
    for inner_thing in thing:
        print(inner_thing)