from tkinter import *
from tkinter import ttk
import datetime as dt

root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()

# I will create a dictionary with two schools
# have a loop that adds each school to the list
# each time that a value of a dictionary is a dictionary a sublist is made


# create two "opprotinities"
'''
Let there be 'Opprotunities' as follows
"type": (masters/scholarship/job/other)
"deadline": day/month/year OR rolling OR N/A (deafult to NA)
"application materials": This one will be complex and have sub dictionaries
"Location": Planet, Continent, Country, State, City (only continent is necessary)
"Organization": UniversityName/OrganizationName
"Submitted": True/False

'''



class Opprotunity:
    def __init__(self, name, location = {} , submitted = False, application = {}):
        self.name = name
        self.set_programType()
        self.set_deadline()
        self.location = location
        self.submitted = submitted
        self.application = {}

    def set_programType(self):
        # have the user set name of program
        # we will have some defaults but give the user to enter what they want
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
        # admission deadline could be fixed or have a date
        roll = int(input('Is application rolling? enter 1 if true: '))
        if roll == 1:
            self.deadline = "Rolling"
        else:
            print('What is the deadline of program?\n')
            day = int(input('Day: '))
            month = int(input('Month: '))
            year = int(input('Year: '))
            self.deadline = dt.date(year, month, day);

    
## This above will eventually be it's own code file

myOpp1 = Opprotunity("Bologna")
print("Organization Name: ", myOpp1.name) 
print("Deadline: ", myOpp1.deadline)
print("Program type: ", myOpp1.programType)
print("Submitted?: ", myOpp1.submitted)
print('Application Materials: ', myOpp1.application)

'''
myOpp1.__dict__.items() stores the object like a dictionary and then takes all of the items
Which is so sick and useful

This should be the order of events
(1) check to see if the item in the dictionary is "name"
    Each time name appears create a new item at the highest level of the treeview -> '' in insert (arg1)
(2) Add subsequent attributes under the ''name''

(3) check to see if the attribute being added is a dictionary
    if it is a dictionary then cycle through all of its elements
        check to see if those sub elements are dictionaries, as well
        Add elements if they are not dictionaries, add more tabs if they are dictionaries
    if not then just store a value


So what do I need? A loop at the high level to see if were checking a "name"
    If we've got a "name" then wee creating a new tab at the base level
I need to write a function that be called multiple times
    This function will check to see if the new element is a dictionary or a different data type
    if dictionary then add a tab at the current root directory and then recheck each element for dictionary type
    if not a dictionary then add a value under the current tab
'''

# I have a growing fear of the issue of assigning the identifier as a dictionary name of the same class for
# each element in the treeview 

def dictionaryChecker(treeview, items):
    # take in current root item
    # take in current value to test
    # see if current value is a dictionary
    # if it is not a dictionary then add the
    # will use a recursive function call in the return if we find another dictionary

    for x,y in items:
        if x =="name":
            treeview.insert('', 'end', y, text = y)
            parentName = y
        elif type(y) is not dict:
            treeview.insert(parentName, 'end', x, text = x)
            treeview.insert(x,'end',iid=None,text=y)
        else:
            # this is a dictionary then repeate above
            newItems = y
            print(y)
            dictionaryChecker(treeview, newItems)

dictionaryChecker(treeview, myOpp1.__dict__.items())
'''   
counter = 0 # start counter
# loop through each item in the dictionary
for x,y in myOpp1.__dict__.items():
    # transform index into a stiring
    index = str(counter)
    # if the type is a dictionary then sub add to list
    if type(y) is dict:
        # know the current root, which is under name, 
        
        # this needs to create a sub level of a dictionary
        
        treeview.insert('', index, x, text = x)
        treeview.insert(x, 'end', y, text = y)
    else:
        # insert to the highest level at the index position the key X and give it text X
        treeview.insert('', index, x, text = x)
        # beneth new place in the treeview, at the end, without an ID, give text to the value of X
        treeview.insert(x, 'end', iid=None, text = y)
    counter += 1

'''
