'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   This program uses the inheritance diagram from this week in order to create a parent class and two child classes.
                    It prompts the user to create at least one object of each type (Car and Pickup). Using a menu system and 
                    capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's 
                    attributes. The program will use user input to define the vehicle's attributes. The options attribute in the parent class 
                    must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, power locks, 
                    remote start, backup camera, bluetooth, cruise control, etc). The user will choose from a list of options to add to the 
                    vehicle's options list and can must choose a minimum of one vehicle option per vehicle. When the user is finished adding 
                    vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~ IMPORTS ~~~~~~~~~~~~~~~~~~~
from os import system

import utils
from Vehicles import Car
from Vehicles import Pickup
from Vehicles import Vehicle
from Vehicles import VirtualGarage

#~~~~~~~~~~~~~~~~~~~~~~ PROGRAM FUNCTIONS ~~~~~~~~~~~~~~~~~~

def prompt_garage_size():
    the_garage = VirtualGarage()
    print("Welcome to Virtual Garage, where you can fill your dream garage with your dream cars!")
    done = False
    while not done:
        capacity = input("How many vehicles do you want in your garage (press return for default of 2)? ")
        try:
            if capacity == '':
                the_garage = VirtualGarage()
                done = True
            else:
                slots = round(int(utils.str_as_number(capacity)),0)
                if slots < 2:
                    print("Oh, sorry gotta have a least 2 vehicles. Try again.")
                    continue
                the_garage = VirtualGarage(slots)
                done = True
        except:
            print("You must enter a valid integer...Try again.")
    return the_garage

def configure_new_vehicle(vehicleClazz):
    ''' This is a Factory method to configure and return any object in the Vehicle Hierarchy.
        @Args vehicleClazz - A Vehicle class type
        @returns An configured instance of the 
    '''
    make = input("What make is the make of the vehicle? ")
    model = input("What is the model of the vehicle? ")
    color = input("What color? ")

    # Contruct the class
    vehicle = vehicleClazz(make, model, color)

    # Configure the options
    opts = vehicle.prompt_options(f"\nOptions time for your {model}!", vehicle.getBaseEquipOpts())
    print(f"Great! Your {vehicle.getModel()} has the following options:\n{opts}\n")
    return(vehicle)

if __name__ == "__main__":
    system('clear')
    # Prompt for garage size
    the_garage = prompt_garage_size()
    
    # Minimum of one of each vehicle type is required, so just satsify that up front
    print("\nSince everyone needs a car let's start with your first car.")
    car = configure_new_vehicle(Car)
    the_garage.parkVehicle(car)
    print("\nYou always need a pickup for doing the dirty work, tell me about your Pickup truck.")
    pickup = configure_new_vehicle(Pickup)
    the_garage.parkVehicle(pickup)

    # Loop until the garage is full
    while not the_garage.atCapacity():
        clazz = None
        while not clazz:
            vehicle_type = input("\nWould you like to add a [C]ar or [P]ickup? ")
            if vehicle_type.lower().startswith('c'):
                clazz = Car
            elif vehicle_type.lower().startswith('p'):
                clazz = Pickup
            else:
                print("Please enter either C for a car or P for a pickup.")

        new_vehicle = configure_new_vehicle(clazz)
        the_garage.parkVehicle(new_vehicle)
    
    # Print out the vehicles in the garage
    print(f"Congratulations! You've filled your {the_garage.getCapacity()} car garage. Let's see what's inside:\n")
    print(the_garage)