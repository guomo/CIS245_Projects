'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Your program will use the inheritance diagram from this week in order to create a parent class and two child classes.
                    Your program will prompt the user to create at least one object of each type (Car and Pickup). Using a menu system and 
                    capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's 
                    attributes. The program will use user input to define the vehicle's attributes. The options attribute in the parent class 
                    must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, power locks, 
                    remote start, backup camera, bluetooth, cruise control, etc). The user will choose from a list of options to add to the 
                    vehicle's options list and can must choose a minimum of one vehicle option per vehicle. When the user is finished adding 
                    vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.

'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASS DEFINTIONS ~~~~~~~~~~~~~~

class Vehicle:

    BASE_OPTS_MAP = {"Base Options" : ("Cruise Control", "Navigation System", "Heated Seats", "Power Mirrors", "Power Locks", 
                    "Keyless Entry", "Bluetooth", "Backup Camera"), "isMultiSelect" : True}
    FUEL_OPTS_MAP = {"Fuel Options" : ("Gasoline", "Diesel", "Hybrid", "Electric"), "isMultiSelect" : False}

    def __init__(self, make, model, color, options = None, fuelType = None):
        """Full constructor for a Vehicle base class.

        Args:
            make (str): Make of the vehicle
            model (str): Model of the vehicle
            color (str): Paint color fo the vehicle
            fuelType (str): One gad, deisel, electric, hydrogen
            options (str): A list of sticker options this vehicle has
        """
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getOptions(self):
        return self.options
    
    def setOptions(self, opts):
        self.options = options

    def setFuelType(self, fuel):
        self.fuelType = fuel

    def isElectric(self):
        return(self.fuelType == "Eletric")

    def isHybrid(self):
        return(self.fuelType == "Hybrid")

    def getBaseEquipOpts(self):
        Vehicle.BASE_OPTS_MAP

    def getFuelOpts(self):
        return(Car.FUEL_OPTS_MAP)

    def __str__(self):
        toStr = f"A {self.color} {self.make} {self.model} with a {self.fuelType} powered engine.\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

class Car(Vehicle):

    CAR_OPTS_MAP = {'Engine Size' : { 'choices': ("1.5L V3", "2.0L v4", "2.5L v5", "3.0L V6", "4.0L V8"), 'isMultiSelect' : False},
                    'Number of Doors' : { 'choices' : (2, 4, 5), 'isMultiSelect' : False}}

    def __init__(self, make, model, color, options = None, fuelType = None, engineSize = None, numDoors= None):
    
        super().__init__(make, model, color, options, fuelType)
        self.engineSize = engineSize
        self.numDoors = numDoors if numDoors >= 2 else 2 

    def getNumDoors(self):
        return self.numDoors

    def getEngineSize(self):
        return self.engineSize

    def getBaseEquipOpts(self):
        baseDict =  super().getBaseEquipOpts()
        options = baseDict.get('Base Options')
        for key, value in Vehicle.CAR_OPTS_MAP:
            baseDict[key] = value
        return options

    def __str__(self):
        toStr = f"A {self.color} {self.numDoors} door {self.make} {self.model} sedan with a {self.fuelType} powered {self.engineSize} engine.\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

class Pickup(Vehicle):

    PICKUP_OPTS_MAP = { 'Cab Style' : {'choices' : ("Standard", "Extra", "Crew", "Double"), 'isMultiSelect' : False},
                        'Bed Length' : {'choices' : ("Short Bed (5’8″ Box)", "Standard Bed (6.5′ Box)", "Long Bed (8′ Box)"), 'isMultiSelect' : False}}

    def __init__(self, make, model, color, options = None, fuelType = None, cabStyle = None, bedLength = None):

        super().__init__(make, model, color, options, fuelType)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def __str__(self):
        toStr = f"A {self.color} {self.cabStyle} cab {self.make} {self.model} with a {self.fuelType} powered engine\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

    def getBaseEquipOpts(self):
        baseDict =  super().getBaseEquipOpts()
        options = baseDict.get('Base Options')
        for key, value in Pickup.TRUCK_OPTS_MAP:
            baseDict[key] = value
        return options

class VirtualGarage:

    def __init__(self, capacity = 2):
        self.capacity = capacity
        self.vehicles = []

    def parkVehicle(self, vehicle):
        self.vehicles.append(vehicle)
        return len(self.vehicles)

    def atCapacity(self):
        return len(self.vehicles) == self.capacity

    