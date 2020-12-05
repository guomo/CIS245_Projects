'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Create a program that includes a dictionary of stocks. Your dictionary should
                    include at least 10 ticker symbols. The key should be the stock ticker symbol and 
                    the value should be the current price of the stock (the values can be fictional). 
                    Ask the user to enter a ticker symbol. Your program will search the dictionary for 
                    the ticker symbol and then print the ticker symbol and the stock price. If the ticker
                    symbol isn’t located print a message indicating that the ticker symbol wasn’t found.

                    This version is capable of giving actual quotes when connected to the net, or make
                    fictional values 
'''
import random
import requests

# Dictionary of 26 stocks in the S&P 500
STOCKS = {'AAPL': {'price': 0, 'info': ('Apple Inc.', 'Information Technology')},
        'BAC': {'price': 0, 'info': ('Bank of America Corp', 'Financials')},
        'C': {'price': 0, 'info': ('Citigroup Inc.', 'Financials')},
        'DIS': {'price': 0, 'info': ('The Walt Disney Company', 'Communication Services')},
        'EBAY': {'price': 0, 'info': ('eBay Inc.', 'Consumer Discretionary')},
        'F': {'price': 0, 'info': ('Ford Motor Company', 'Consumer Discretionary')},
        'GOOG': {'price': 0, 'info': ('Alphabet Inc.\xa0(Class C)', 'Communication Services')},
        'HD': {'price': 0, 'info': ('Home Depot', 'Consumer Discretionary')},
        'INTC': {'price': 0, 'info': ('Intel Corp.', 'Information Technology')},
        'JNJ': {'price': 0, 'info': ('Johnson & Johnson', 'Health Care')},
        'KO': {'price': 0, 'info': ('Coca-Cola Company', 'Consumer Staples')}, 
        'LOW': {'price': 0, 'info': ("Lowe's Cos.", 'Consumer Discretionary')},
        'MMM': {'price': 0, 'info': ('3M Company', 'Industrials')},
        'NKE': {'price': 0, 'info': ('Nike, Inc.', 'Consumer Discretionary')},
        'ORCL': {'price': 0, 'info': ('Oracle Corp.', 'Information Technology')},
        'PG': {'price': 0, 'info': ('Procter & Gamble', 'Consumer Staples')},
        'QCOM': {'price': 0, 'info': ('QUALCOMM Inc.', 'Information Technology')},
        'RL': {'price': 0, 'info': ('Ralph Lauren Corporation', 'Consumer Discretionary')},
        'SBUX': {'price': 0, 'info': ('Starbucks Corp.', 'Consumer Discretionary')},
        'T': {'price': 0, 'info': ('AT&T Inc.', 'Communication Services')},
        'UPS': {'price': 0, 'info': ('United Parcel Service', 'Industrials')},
        'V': {'price': 0, 'info': ('Visa Inc.', 'Information Technology')},
        'WMT': {'price': 0, 'info': ('Walmart', 'Consumer Staples')},
        'XRX': {'price': 0, 'info': ('Xerox', 'Information Technology')},
        'YUM': {'price': 0, 'info': ('Yum! Brands Inc', 'Consumer Discretionary')},
        'ZTS': {'price': 0, 'info': ('Zoetis', 'Health Care')}}

def fetchPrice(symbol):
    ''' Hits the finhub free API to get near-realtime quotes. If not net or an error occurs
        due to some network or account issue it makes up a price.'''

    try:
        resp = requests.get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=Bup13m748v6sg76blf7g")
        return(resp.json()['c'])
    except requests.exceptions.RequestException as rex:
        print(f"\033[1;31mError connecting to stock service:\n{rex}\n\033[0;0mSorry, this quote is fictional.\n")
        # fallback if no net connection or something is wrong with the service
        return(round(random.random() * 100, 2))

def print_quote(symbol):
    ''' Displays a quoted price for a given stock symbol '''

    if symbol in STOCKS:
        # Technically we could use any ticker and let it fail at the service call, but the
        # assignment wants a dictionary, so choices are necessarily limited.
        if STOCKS[symbol]['price'] == 0: # poor man's caching :-)
            STOCKS[symbol]['price'] = fetchPrice(symbol)
    else:
        raise TypeError(f"Symbol {symbol} is not in data set")
    info = STOCKS[symbol]['info']
    #print(f"The price for a share of {info[0]} in the {info[1]} sector is ${STOCKS[symbol]['price']}")
    print(f"{info[0]} in the {info[1]} sector last traded at ${STOCKS[symbol]['price']}\n\n")


if __name__ == "__main__":
    print("\n\nWelcome to Ticker Roullete! Pick a stock in the S&P 500 and see if you win you will get a quoten")
    done = False
    while not done:
        symbol = input("Enter a stock symbol to get a quote, or 'Q' to exit: \n").upper()
        if symbol != "Q":
            try:
                print_quote(symbol)
            except:
                print(f"Sorry, the symbol {symbol} is not in my data bank. Try again\n\n")
        else:
            print("Happy trading!")
            done = True