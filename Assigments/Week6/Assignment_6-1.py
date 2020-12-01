'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   THis program uses the inheritance diagram from this week in order to create a parent class and two child classes.
                    It prompts the user to create at least one object of each type (Car and Pickup). Using a menu system and 
                    capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's 
                    attributes. The program will use user input to define the vehicle's attributes. The options attribute in the parent class 
                    must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, power locks, 
                    remote start, backup camera, bluetooth, cruise control, etc). The user will choose from a list of options to add to the 
                    vehicle's options list and can must choose a minimum of one vehicle option per vehicle. When the user is finished adding 
                    vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~ IMPORTS ~~~~~~~~~~~~~~~~~~~
import re
from os import system

from Vehicles import Car
from Vehicles import Pickup
from Vehicles import Vehicle
from Vehicles import VirtualGarage

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

    return(retNum)

def prompt_options(prompt, optionsDict, vehicleClass):
    answers = {}
    for keys, value in optionsDict:
        answers[key] = input("{prompt}")


def configure_new_vehicle(vehicleClazz):
    make = input("What make is the make of the vehicle? ")
    model = input("What is the model of the vehicle? ")
    color = input("What color? ")
    vehicle = vehicleClazz(make, model, color)

    if vehicleClazz == Car:
        print("Let's pick some options for you car...")
    if vehicleClazz == Pickup:
        print("Let's pick some options for you Pickup...")
    
    return(vehicle)


if __name__ == "__main__":
    system('clear')

    # State Variables
    the_garage = VirtualGarage()

    # Prompt for garage size
    print("Welcome to Virtual Garage, where you can fill your dream garage with your dream cars!")
    dataOK = False
    while not dataOK:
        capacity = input("How many vehicles do you want in your garage (press return for default of 2)? ")
        try:
            if capacity == '':
                the_garage = VirtualGarage()
                dataOK = True
            else:
                slots = round(int(str_as_number(capacity)),0)
                if slots < 2:
                    print("Oh, sorry gotta have a least 2 vehicles. Try again.")
                    continue
                the_garage = VirtualGarage(slots)
                dataOK = True
        except:
            print("You must enter a valid integer...Try again.")
    
    # Minimum of one of each vehicle type is required, so just satsify that up front
    print("Since everyone needs a pickup and car let's start with your first car.")
    car = configure_new_vehicle(Car)
    the_garage.parkVehicle(car)
    print("You always need a pickup for doing the dirty work, tell me about your Pickup truck.")
    pickup = configure_new_vehicle(Pickup)
    the_garage.parkVehicle(pickup)

    #Loop until the garage is full
    while not the_garage.atCapacity():
        clazz = None
        while not clazz:
            vehicle_type = input("Would you like to add a [C]ar or [P]ickup? ")
            if vehicle_type.lower().startswith('c'):
                clazz = Car
            elif vehicle_type.lower().startswith('p'):
                clazz = Pickup
            else:
                print("Please enter either C for a car or P for a pickup.")

        new_vehicle = configure_new_vehicle(clazz)
        the_garage.parkVehicle(pickup)
    
    # Print out the vehicle sin the garage
