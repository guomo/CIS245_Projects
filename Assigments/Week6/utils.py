'''
    Module      :   utils
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Classes to support generic vehicle abstraction.

'''
import re


#~~~~~~~~~~~~~~~~~~~~~~~~~~ UTILITY METHODS  ~~~~~~~~~~~~~~
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
    return retNum


def menufy(optName, optTup):
    ''' Simple menu interfrace that enumerates a tuple and returns the chosen option #
        @param optName - Name of option to appear in the propmpt
        @param optTup - A tuple of option names to choose from

        @return tuple - Chosen # and option
    '''

    choice = 0
    print(f"Select one of the following {optName}:")
    # Display a menu of options
    for i, opt in enumerate(optTup):
        print(f"{i+1}. {opt}")
    try:
        choice = str_as_number(input("choice:")) - 1
    except TypeError as ex:
        # bad input, use first choice as default
        choice = 0
        print("That wasn't an option, so let's go with the default of {}")
    return (choice, optTup[choice])