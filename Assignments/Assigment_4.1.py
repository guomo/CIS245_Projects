'''
    Program     :   Assignment 4.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Convert miles to kilometers and do using a function call i.e., not inline
'''

import re

KM_PER_MILE_MULTIPLIER = 1.609344

def str_as_number(aStr, neg_ok = False):
    ''' Converts a string to the appropriate number type either float or int.
        @param (required) aStr - The number as a string to convert
        @param neg_ok - Set to true to keep negative values, otherwise default is to strip 
                        sign and return a postive num
        @raises TypeError if input wasn't a string or no numbers were in the string
    '''
    if type(aStr) is not str:
        raise TypeError("Expected str type got ${type(aStr)")

    retNum = None 
    if(neg_ok):
        cleaned = re.sub("[^\d.-]*",'',aStr)  # strip everything not sign, digits, and decimal
    else:
        cleaned = re.sub("[^\d.]*",'',aStr)  # strip everything not digits or decimal

    # Throw an exception if the string had no numbers, otherwise convert
    if len(cleaned):
        retNum = int(cleaned) if float(cleaned).is_integer() else float(cleaned)
    else:
        raise TypeError(f"No numerals found in string for conversion: {aStr}")

    return(retNum)

def miles_to_klicks(inMiles = None):
    ''' Converts imperial miles to metric kilometers .
        @param inMiles - int or float; will try type coercion if it is a string
    '''
    converted = str_as_number(inMiles)
    return(converted * KM_PER_MILE_MULTIPLIER)

try:
    miles = input("Enter any number of Miles driven to convert to Kilometers: ")
    print(f"{miles} miles is approximately {round(miles_to_klicks(miles),2) } Kilometers.")
except:
    print("Bad input, try again later...\n")


