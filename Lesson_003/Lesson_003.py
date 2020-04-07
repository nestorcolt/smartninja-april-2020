# Reading and Writing file sin Python

"""
Resources:
https://stackabuse.com/read-a-file-line-by-line-in-python/
https://docs.python.org/3/library/os.html
https://www.programiz.com/python-programming/operators
"""
import os

##############################################################################################
# Read

current_directory = os.getcwd()
full_path_to_file = os.path.join(current_directory, "ninja.txt")  # Try not to parse strings into commands

if os.path.exists(full_path_to_file):
    #
    with open(full_path_to_file, "r") as ninja_file:
        contents = ninja_file.read()
        # print(contents)

else:
    print("Sorry, {} doesn't exist.".format(full_path_to_file))

# Write
file_name = "ninja_002.txt"
full_path_to_file = os.path.join(current_directory, file_name)

with open(full_path_to_file, "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file!\nThis piece of code is created with Python\n\n\t\tPython is aweeesome!!! ")
