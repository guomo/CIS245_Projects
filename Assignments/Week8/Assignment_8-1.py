'''
    Program     :   Assignment 8.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Allows the user to specify a working directory, asks for input, and saves the data out and verifies it.
'''

import os
from pathlib import Path

def prompt_data_out():
    p = None

    while not p:
        # Get the directory to store the file in
        working_dir = input("What directory would you like to store your data? ")
        # on unix systems users can specify their home dir with alias ~, expand if need be; resolve is in case there are symlinks
        p = Path(working_dir).expanduser().resolve() 
        # Check for existance and write permissions 
        if not os.path.exists(p):
            print("That directory does not exist.")
            mkdir = input("Would you like to to create it [y/n]?")
            if mkdir.lower().startswith('y'):
                try:
                    os.makedirs(p, exist_ok=True)
                except PermissionError as permEx:
                    print("Sorry, You don't have permsisions in one or more of the directories to create that directory. Try Again.")
                    p = None
                except FileExistsError as fileEx:
                    print("Sorry, the path specified is actually an existing file not directory. Try Again.")
                    p = None
            else:
                p = None
        elif os.path.isdir(p):
            print("Sorry, a file already exists with that directory name. Try again.")
            p = None

    # Now get the filename to store the data in
    while True:
        fp = Path(p, input ("Enter a filename to store your data: "))
        if fp.exists() and not os.access(fp, os.W_OK):
            print("That file already exists and you don't have access to overwrite, pick another name.")
        else:
            p = fp
            break

    return p

def prompt_data_in(dest_file):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone= input("Enter your phone #: ")
    with open(dest_file, 'a') as fh:
        fh.write(f"{name}, {address}, {phone}\n")
        print("Data saved...\n")


def cat_file(file_path):
    print(f"{file_path} contents are :\n\n")
    with open(file_path, 'r') as fh:
        for line in fh:
            print(line.strip())


if __name__ == "__main__":
    out_file = prompt_data_out()
    prompt_data_in(out_file)
    cat_file(out_file)
