'''
    Program     :   Assignment 5.1
    Course      :   CIS245-O321 Introduction to Programming (2213-DD)
    Author      :   Gregory Stone — gstone@my365.bellevue.edu
    Description :   Classes to support generic vehicle abstraction.

'''
import utils

#~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASS DEFINTIONS ~~~~~~~~~~~~~~

class Vehicle:

 
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
        # Configure the available options, changing anything here will affect baseopts for all subclasses
        self.equipOpts = {"Base Options" : {
                                "choices" : ("Cruise Control", "Navigation System", "Heated Seats", "Power Mirrors", "Power Locks", 
                                                "Keyless Entry", "Bluetooth", "Backup Camera"), 
                                "isMultiSelect" : True ,
                                "setCallback" : self.setOptions 
                                },
                         "Fuel Options" : {
                                "choices" : ("Gasoline", "Diesel", "Hybrid"), 
                                "isMultiSelect" : False ,
                                "setCallback" : self.setFuelType
                                }
                        }
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getOptions(self):
        return self.options
    
    def setOptions(self, opts):
        self.options = list(opts)

    def getFuelType(self):
        return self.fuelType

    def setFuelType(self, fuel):
        self.fuelType = fuel

    def isElectric(self):
        return(self.fuelType == "Electric")

    def isHybrid(self):
        return(self.fuelType == "Hybrid")

    def getBaseEquipOpts(self):
        return self.equipOpts

    # Ordinarily you wouldn't put UI, even CLI UI, components in a class due to the best practices
    # of separation of concerns, i.e. keep presentation tier from model and controller. But the 
    # logic here is very specific to Vehicle objects but also quite generic across them based on design.
    # Another option is to put this in a UI specicifc class and use mixins.
    def prompt_options(self, prompt, optionsDict):
        ''' Given a top-level prompt string and an options dictionary from a Vehicle class,
            prompt the user for each option accordingly. Some options are multiple choice
            and not mutually exclusive, some are mutually exlsuive. The method prompts the
            user with either Y/N or a numbered menu accordingly.
            @param prompt - A String to prompt for the top level
            @param optionsDict - A dictionary from the Vehicle class base options to gather choices from

            @return - An array of all the chosen options.
        '''
        chosenOpts = []
        print(prompt)
        # optionsDict structure is map of option levels, and each level has choices (tuple),
        #  multiselect (boolean), and a callback to set the values. So loop through levels 
        # and each set of options.
        for optLevel, opts in optionsDict.items():
            choice, localOpts = None, []
            setter = opts['setCallback']
            print()
            if opts['isMultiSelect']:
                print(f"Let's pick your {optLevel}:")
                # loop and ask Y/N is they want each option, save each yes.
                for option in opts['choices']:
                    c = input(f"{option} [Y/N?]: ")
                    if c.lower() == 'y':
                        localOpts.append(option)
                setter(localOpts) # Use the callback to set 
                chosenOpts += localOpts
                localOpts.clear()
            else:
                # print menu with numbers to select jus tone of many options, save chosen value
                choice = utils.menufy(optLevel, opts['choices'])
                setter(choice[1])
                chosenOpts.append(choice[1])
                choice = None

        return chosenOpts

    def __str__(self):
        toStr = f"A {self.color} {self.make} {self.model} with a {self.fuelType} powered engine.\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

class Car(Vehicle):

    def __init__(self, make, model, color, options = None, fuelType = None, engineSize = None, numDoors = 2):
    
        super().__init__(make, model, color, options, fuelType)
        self.engineSize = engineSize
        self.numDoors = numDoors
        carOpts = {"Engine Size" : {
                                "choices": ("1.5L V3", "2.0L v4", "2.5L v5", "3.0L V6", "4.0L V8"), 
                                "isMultiSelect" : False ,
                                "setCallback" :  self.setEngineSize },
                            "Number of Doors" : { 
                                "choices" : (2, 4, 5), 
                                "isMultiSelect" : False,
                                "setCallback" :  self.setNumDoors }
                            }
        # This merges the parent options with the options specifci to this class
        superBase = super().getBaseEquipOpts()
        self.equipOpts = {**superBase, **carOpts}

    def getNumDoors(self):
        return self.numDoors

    def getEngineSize(self):
        return self.engineSize

    def setNumDoors(self, num):
        self.numDoors = num
    
    def setEngineSize(self, size):
        self.engineSize = size

    def __str__(self):
        toStr = f"A {self.color} {self.numDoors} door {self.make} {self.model} sedan with a {self.fuelType} powered {self.engineSize} engine.\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

class Pickup(Vehicle):

    
    def __init__(self, make, model, color, options = None, fuelType = None, cabStyle = None, bedLength = None):

        super().__init__(make, model, color, options, fuelType)
        self.cabStyle = cabStyle
        self.bedLength = bedLength
        pickupOptsMap = { "Cab Style" : {
                            "choices" : ("Standard", "Extra", "Crew", "Double"),
                            "isMultiSelect" : False,
                            "setCallback" : self.setCabStyle},
                        "Bed Length" : {
                            "choices" : ("Short Bed (5’8″ Box)", "Standard Bed (6.5′ Box)", "Long Bed (8′ Box)"),
                            "isMultiSelect" : False,
                            "setCallback" : self.setBedLength}
                        }
 
        # This merges the parent options with the options sepcfic to this class
        superBase = super().getBaseEquipOpts()
        self.equipOpts = {**superBase, **pickupOptsMap}

    def __str__(self):
        toStr = f"A {self.color} {self.cabStyle} cab {self.make} {self.model} with a {self.fuelType} powered engine\n"
        toStr += f"Optional equipment: {self.options}"
        return toStr

    def getCabStyle(self):
        return self.cabStyle

    def setCabStyle(self,  style):
        self.cabStyle = style
        
    def getBedLength(self):
        return self.bedLength

    def setBedLength(self, length):
        self.bedLength = length


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
        for door, vehicle in enumerate(self.vehicles):
            ret_str += f"In garage door #{door+1} we have {vehicle}\n"
        return ret_str
    