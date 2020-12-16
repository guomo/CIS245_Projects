'''
    Program     :   Assignment Class project - final
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Provides a command line interface to the open weather web service.
'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ IMPORTS ~~~~~~~~~~~~~~~~~~~
from os import system
import requests


#~~~~~~~~~~~~~~~~~~~~~~~~~~~ HELPER FUNCS ~~~~~~~~~~~~~~~~

def splash_screen():
    ''' Prints the application banner.'''
    print('''
__    __   ___  ____ ______ __ __   ___ ____        ___  ____       ____   ___  ______ 
|  |__|  | /  _]/    |      |  |  | /  _|    \      /   \|    \     |    \ /   \|      |
|  |  |  |/  [_|  o  |      |  |  |/  [_|  D  )    |     |  D  )    |  _  |     |      |
|  |  |  |    _|     |_|  |_|  _  |    _|    /     |  O  |    /     |  |  |  O  |_|  |_|
|  `  '  |   [_|  _  | |  | |  |  |   [_|    \     |     |    \     |  |  |     | |  |  
 \      /|     |  |  | |  | |  |  |     |  .  \    |     |  .  \    |  |  |     | |  |  
  \_/\_/ |_____|__|__| |__| |__|__|_____|__|\_|     \___/|__|\_|    |__|__|\___/  |__|  
                                                                                        
--------------------------------------------------------------------------------------------''')
    print("Welcome to Weather or Not, the real-time weather service tool.\n\n")


def usage():
    print("\nEnter your location in one of the following ways:\nCity, Country e.g. Milan, Italy\nCity, State, Country e.g. Cupertino, CA, US\n or a US zipcode e.g. 95050")
    print("type [Q]uit to exit.\n")

def ask_location():
    ''' Prompts the user for either a city, state, country combo or a zip code.
        @return dict - Dictionary with an openWeather API safe location.
    '''
    ret_location, good = {}, False

    while not good:
        response = input("Get weather for: ")
        loc = response.lower()
        if response.isnumeric():
            # Check if it likely a US zipcode (OpenWeather doesn't support Candian postal codes) and zips are a certain range
            zip = int(response)
            if zip > 500 and zip < 99902: 
                # Fixed bug where conversion to int stripped leading zero, so couldn't fetch weather for New England!
                ret_location['zip'] = response
            else:
                print(f"Sorry {zip} is not a valid US zipcode. Try again.\n")
                continue
            good = True
        elif response.lower() in ['q', 'quit']:
            exit("Goodbye!")
        elif len(response) > 0:
            ret_location['city'] = response
            good = True
        else:
            usage()

    return ret_location

def display_results(wd):
    ''' Pretty prints the results of a weather service query.
        @param dict - Dictionary of weather data form openweather service.
    '''
    if wd:
        print(f"The weather for {wd['name']},{wd['sys']['country']} is:")
        print(f"Temperature of {wd['main']['temp']}° with {wd['weather'][0]['description']}, with winds at {wd['wind']['speed']}mph and {wd['main']['humidity']}% humidity.\n")

def open_weather_connect(options):
    '''
        Given a location as a zip or a city, connect to the open weather service API
        and fetch the current weather data.
        @param location - options dictionary with key of city or zip
        @return weather_data - Dictionary with the weather data
    '''

    # These are the service's base URLs and the params that go with every requests
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    query = {'units' : "imperial", 'appid' : "ff43c714e495ecf805410d0660a6475a"}
    weather_data = None

    print("\tConnecting to weather service", end ="..." )

    # Datermine if the request is for city or zip
    if options.get('zip'):
        # Add the request zip to the query str
        query['zip'] = options['zip']
    elif options.get('city'):
        # Add the request city to the query str
        query['q'] = options.get('city')

    try:
        # Make the request, if it fails due to network issues the except claue handles it
        resp = requests.get(BASE_URL, params = query)
        if(resp.status_code == 200):
            # Good stuff, it liked our city or zip
            # Get the JSON response as a pythong dict
            print("connection successful.")
            weather_data = resp.json()
        else:
            # Possibly no city or zip found, check status for more details
            if resp.status_code == 404:
                # zip or city not found
                print(f"Sorry, no data for requested location. Are you sure that location is on planet Earth?\n")

            elif resp.status_code == 400:  # HTTP status bad request
                # The URL was malformed, maybe user put crappy data?
                print(f"{resp.status_code} - {resp.reason}")
                print(f"Sorry, no data for requested location. Did you forget the state or country?")
                usage()

    except requests.exceptions.RequestException as reqEx:
        exit('Unable to connect to the weather service, try again later.')

    # Stuff the user's location request into the return object for later display
    return weather_data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    system('clear')
    done = False
    splash_screen()
    usage()
    while not done:
        display_results(open_weather_connect(ask_location()))
        

