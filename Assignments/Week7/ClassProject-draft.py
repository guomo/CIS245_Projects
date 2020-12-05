'''
    Program     :   Assignment Class project
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Provides a command line interface to the open weather web service.
'''
import requests
import re
import argparse
import locale

def main_prompt():
    ''' Asks the user for a city or zip code and validates the nature of the input.

    '''
    pass

def open_weather_connect(options):
    '''
        Given a location as a zip or a city, connect to the open weather service API
        and fetch the current weather. Reults are returned as a JSON object.
        @param location - options dictionary { zip : '', city : ''}
    '''
    
    pass