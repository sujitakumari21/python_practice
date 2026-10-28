# write a python program to print the contents of  a directory using the Os module. Search online for the function which does that.

import os

# Path of the directory
directory = "."

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)