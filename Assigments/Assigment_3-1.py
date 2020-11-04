'''
    Program     :   Assignment 3.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   determine how long it takes for an investment to double at a given interest rate. 
                    The input is an annualized interest rate and the initial investment amount, and 
                    the output is the number of years it takes an investment to double.
'''

import locale
import re

# Set the locale for currency formatting the order amount
locale.setlocale(locale.LC_ALL, '')
    
# prompt for the balance and rate
valid, balance, rate = False, 0, 0

print("\nWelcome to the double your money Investment Calulator.\n")
# Keep asking for input until they give us a legit number
while not valid:
    open_bal=input("What is your opening balance? ")
    cleanNum = re.sub("[^\d.]*",'',open_bal)  # strip everything not but digits and decimals
    if len(cleanNum):
        open_bal = float(cleanNum)
        break
    else: 
        print("\tPlease enter a postive number for your starting balance.\n\n")
        valid = None # bad input, try again        

# Keep asking for input until they give us a legit number
while not valid:
    rate = input("What is the interest rate? ")
    cleanNum = re.sub("[^\d.]*",'',rate)  # strip everything not but digits and decimals
    if len(cleanNum):
        rate = float(cleanNum)
        break
    else:
        print("\tNot interesting. The interest rate must be a non-negative number!\n\n")
        rate = None # bad input, try again          

# Calculate the number of years until it doubles
years, balance, target, durationStr = 0, open_bal, open_bal * 2, None
if rate > 100: # Don't bother calculating over 100% interest
    durationStr = "less than a year"
    balance += balance * (rate/100)
else:
    while balance < target:
        balance += balance * (rate/100)
        years += 1
    # Respond with proper english dammit!
    if years == 1:
        durationStr = "a year"
    else:
        durationStr = str(f"about {years} years")

print(f"Your investment of {locale.currency(round(open_bal,2))} will double in {durationStr}, at which time the balance will be {locale.currency(round(balance,2))}.")


