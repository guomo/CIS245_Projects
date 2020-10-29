'''
    Program     :   Assignment 2.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Part 1: Calculates the cost of installing fiber optic cable at a cost of $0.87 per foot for a company. 
                    And displays the company name and the total cost. 
                    
                    Part 2: Run with -t option to use a tiered pricing table
'''

import argparse
import locale

def orderPrompt():
    ''' Prompts for company name and order qty and returns. A compnay of quit exits the program. '''
    company_name, qty = None, None

    # Get the company name
    while not company_name :
        company_name = input("What is your Company's name? ")
        if not company_name:
            print("\tYou must supply a Company name to place an order.\n\n")

        if company_name.lower() == "quit":
            exit()
 
    
    # Prompt them for the qty
    while not qty:
        ''' '''
        qty = input("What is the total number of feet required? ")
        
        if qty.startswith('-') or not qty.isnumeric: # Check for bogus values
            print("\tPlease enter a postive numeric value for number of feet.\n\n")
            qty = None # bad input, try again          
        else:
            qty = int(qty)
            return {'company' : company_name, 'qty' : qty}




def calc_order(order, priceList = None):
    ''' Calculates the cost of an order.
        @param order - dictionary with company and qty keys
        @param priceList - set to true to use tiered pricing
    '''
    cost = None

    if priceList:
        if order['qty'] > 500:
            cost = .50 * order['qty']
        elif order['qty'] > 250:
            cost = .70 * order['qty']
        elif order['qty'] > 100:
            cost = .80 * order['qty']
        else:
            cost = .87 * order['qty']
    else:
        cost = .87 * order['qty']
    
    print(f"Thank you {order['company']}, your order for {round(order['qty'],2)} feet of fiber cable has been placed; please remit {locale.currency(round(cost,2))}\n\n")

if __name__ == "__main__":
    # Set the locale for currency formatting the order amount
    locale.setlocale(locale.LC_ALL, '')

    # Configure a parser to allow tiered or single price ordering
    parser = argparse.ArgumentParser(prog='CableCalc', description="Cable ordering application.")
    parser.add_argument('-t', action='store_const', const=True, help='Use built-in tiered pricing table')
    args = parser.parse_args()

    # Display the splash prompt and loop forever - or until someone types quit as the company prompt
    print("Welcome to FiberNet's CableCalc order system. To exit type 'Quit'.\n")
    while True:
        calc_order(orderPrompt(), args.t)

