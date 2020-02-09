from tkinter import *
from tkinter import ttk
import datetime as dt
import pdb # for interactive debugging


'''
EXECUTIVE SUMMARY:
    (1) initialize GUI using tkinter
    (2) Create an Opprotunity class that standardizes application materials
    (3) Display data from each Opprotunity onto the tkinter GUI as a treeview
'''

### Iinitialize the GUI
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()


class Opprotunity:
    '''
    Create an Opprotunity class that stores standardizes information of programs to apply to
    Let there be 'Opprotunities' as follows
    "type": (masters/scholarship/job/other)
    "deadline": day/month/year OR rolling OR N/A (deafult to NA)
    "application materials": This one will be complex and may have sub dictionaries
    "Location": {Planet, Continent, Country, State, City} (only continent is necessary)
    "Organization": UniversityName/OrganizationName
    "Submitted": True/False

    '''
    def __init__(self, name, location = {} , submitted = False, application = {}):
        self.name = name
        self.set_programType()
        self.set_deadline()
        self.location = location
        self.submitted = submitted
        self.application = {}

    def set_programType(self):
        # have the user set name of program
        # we will have some defaults but give the user the option enter what they want
        print("What is the type of program? Enter:\n")
        print("1 for Masters")
        print("2 for Scholarship")
        print("3 for Job")
        print("4 for 'Other'")
        response = input("Or enter a desired name: \n")
        if response == "1":
            self.programType = "Masters"
        elif response == "2":
            self.programType = "Scholarship"
        elif response == "3":
            self.programType = "Job"
        elif response == "4":
            self.programType = "Other"
        else:
            self.programType = str(response)
            
    def set_deadline(self):
        # The daedline will either be a string for "rolling"
        #   or a datetime object
        roll = int(input('Is application rolling? enter 1 if true: '))
        if roll == 1:
            self.deadline = "Rolling"
        else:
            print('What is the deadline of program?\n')
            day = int(input('Day: '))
            month = int(input('Month: '))
            year = int(input('Year: '))
            self.deadline = dt.date(year, month, day);

def dictionaryChecker(treeview, rootlevel, items):
    '''
    ARGS:
        treeview: a pointer to the treeview GUI object
        rootlevel: a pointer to the higher item in the hierarchy
            in which the next item will be stored under
        items: a key value pair in which the key will become the "header" in the GUI
            the value will be displayed as the "value" i.e.
            "deadline" is the key and will become the header
            "2020-03-15" is the ``value" and will be the value under deadline
            IF "values" is a dictionary than dictionaryChecker is called recursivly
                
    RETURNS:
        NOTHING. Things are just added to the GUI
        
    CALLING SEQUENCE:
        dictionaryChecker(treeview, rootlevel, items):

    '''
    # items is intended to be the Opprotunity object turned into a dictionary
    #   OR an occasion when the value of an attribute of Opprotunity is a dictionary
    #   items are key=value pairs
    for x,y in items:
        itemName = rootlevel + "_" + x
        # itemName must be unique
        #   therefore we just use the hierarchy for the naming
        #   Example: itemName = Bologna_deadline
        if x =="name":
            print('skip the name field for: ', x)
        elif type(y) is not dict:
            # Adds each key to the GUI and stores the value beneath
            treeview.insert(rootlevel, 'end', itemName, text = x)
            treeview.insert(itemName,'end',iid=None,text=y)
        else:
            # IF y is a dictionary then start opening the dictionary and
            #   put each of the keys and values from that dictionary under x in the GUI
            print(x, y)
            treeview.insert(rootlevel, 'end', itemName, text = x)
            dictionaryChecker(treeview, itemName, y.items())
        '''
        We essentially do not need to create another conditional if y is an empty dictionary
        Because if y is empty the native python for loop functionality does exactly what we want
        This is so great beause I could also easlity imagine the program crashing is
        trying to assign an empty item to a variable. 

        '''


# create two Opprotunity objects for testing and store them in a list
myOpp1 = Opprotunity("Bologna")
myOpp2 = Opprotunity("Roma")
opprotunities = []
#       itemName = rootlevel + "_" + x
opprotunities.append(myOpp1)
opprotunities.append(myOpp2)

# iterate through each object and store 
for i in range(0, len(opprotunities)):
    treeview.insert('', 'end', opprotunities[i].name, text=opprotunities[i].name)
    dictionaryChecker(treeview, opprotunities[i].name, opprotunities[i].__dict__.items())
    
root.mainloop()

'''
6 February 2020
Things we still need:

(1) an application materials class.
Some basic attributes such as:
    Number of recomendation letters: int
    Personal statement: True/False (maybe prompt?)
    Statement of Purpose: True/False (maybe store prompt instead)
    Language requirements: {"Italian": "B2", "French": "C1", "English": "C2"}
    Demographics: "Finished" or "Not Finished"
    
We also need a method that allows the user to enter specific/ not standard
    items to application class (maybe, I think this is a lower priority item)
    
    class application:
        def __init__(self):

(2) Be able to save, store, and load Opprotunity objects

(3) Have a way to create new opprotunity objects and add the conents to a previous
        the save file

(4) Edit layout of GUI to have values be in columns adjacent to names instead of below
        > programType:    Masters
    instead of
        > programType:
            Masters
    (this is low priority)
    ^ I think just think of the best layout in general

'''

