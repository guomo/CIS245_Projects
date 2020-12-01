'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Classes to support generic vehicle abstraction.

'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASS DEFINTIONS ~~~~~~~~~~~~~~

class Vehicle:

    BASE_OPTS_MAP = {"Base Options" : {'choices' : ("Cruise Control", "Navigation System", "Heated Seats", "Power Mirrors", "Power Locks", 
                    "Keyless Entry", "Bluetooth", "Backup Camera"), "isMultiSelect" : True}}
    FUEL_OPTS_MAP = {"Fuel Options" : {'choices' : ("Gasoline", "Diesel", "Hybrid", "Electric"), "isMultiSelect" : False}}

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
        return Vehicle.BASE_OPTS_MAP

    def getFuelOpts(self):
        return Vehicle.FUEL_OPTS_MAP

    def __str__(self):
        toStr = f"A {self.color} {self.make} {self.model} with a {self.fuelType} powered engine.\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

class Car(Vehicle):

    CAR_OPTS_MAP = {'Engine Size' : { 'choices': ("1.5L V3", "2.0L v4", "2.5L v5", "3.0L V6", "4.0L V8"), 'isMultiSelect' : False},
                    'Number of Doors' : { 'choices' : (2, 4, 5), 'isMultiSelect' : False}}

    def __init__(self, make, model, color, options = None, fuelType = None, engineSize = None, numDoors = 2):
    
        super().__init__(make, model, color, options, fuelType)
        self.engineSize = engineSize
        self.numDoors = numDoors
        superBase = super().getBaseEquipOpts()
        self.equipOpts = {**superBase, **Car.CAR_OPTS_MAP}

    def getNumDoors(self):
        return self.numDoors

    def getEngineSize(self):
        return self.engineSize

    def getBaseEquipOpts(self):
        return self.equipOpts

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
        superBase = super().getBaseEquipOpts()
        self.equipOpts = {**superBase, **Car.CAR_OPTS_MAP}

    def __str__(self):
        toStr = f"A {self.color} {self.cabStyle} cab {self.make} {self.model} with a {self.fuelType} powered engine\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

    def getBaseEquipOpts(self):
        return self.equipOpts

class VirtualGarage:

    def __init__(self, capacity = 2):
        self.capacity = capacity
        self.vehicles = []

    def parkVehicle(self, vehicle):
        self.vehicles.append(vehicle)
        return len(self.vehicles)

    def atCapacity(self):
        return len(self.vehicles) == self.capacity

    def getCapacity(self):
        return self.capacity

    def __str__(self):
        ret_str = ""
        for door, vehicle in enumerate(vehicles):
            ret_str += f"In garage door #{door} we have {vehicle}"
        return ret_str
    