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
        working_dir = input("What directory would you like to store you data? ")
        # on unix systems users can specify their home dir with alias ~, expand if need be
        p = Path(working_dir).expanduser()
        # Check for existance and write permissions 
        if os.path.exists(p) and os.access(p, os.R_OK | os.W_OK | os.X_OK ) and os.path.isdir(p):
            while True:
                fp = Path(p, input ("Enter a filename to store your data: "))
                if fp.exists() and not os.access(fp, os.W_OK):
                    print("That file already exists and you don't have access to overwrite, pick another name.")
                else:
                    p = fp
                    break
        else:
            os._exists(p)
            print("That directory not exists")
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
