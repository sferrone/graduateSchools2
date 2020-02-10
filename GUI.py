from tkinter import *
from tkinter import ttk
import datetime as dt
import csv


'''
EXECUTIVE SUMMARY:
    (1) initialize GUI using tkinter
    (2) Create an Opportunity class that standardizes application materials
    (3) Display data from each Opportunity onto the tkinter GUI as a treeview
'''

### Iinitialize the GUI
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()


class Opportunity:
    '''
    Create an Opportunity class that stores standardizes information of programs to apply to
    Let there be 'Opportunities' as follows
    "type": (masters/scholarship/job/other)
    "deadline": day/month/year OR rolling OR N/A (deafult to NA)
    "application materials": This one will be complex and may have sub dictionaries
    "Location": {Planet, Continent, Country, State, City} (only continent is necessary)
    "Organization": UniversityName/OrganizationName
    "Submitted": True/False

    '''
    def __init__(self, name, link="", location = {} , submitted = False, application = {}):
        self.name = name
        self.link=link
        self.programType = ""
        self.deadline = ""
        self.location = location
        self.submitted = submitted
        self.application = application # make setter function
        

    def set_programType(self, programType):

        self.programType = programType
            
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
            
class CsvFile:
    """ 
    CsvFile class:
    A CsvFile object will make easier the reading and manipulation of our data from CSV sheets.
    filename - "filename.csv" the name of our CSV file
    hasHeader - if our CSV file has a header (which any CSV file we use should), this is True
    columns - the columns dictionary object exists to avoid hardcoding, and will be useful if we ever read from additional CSV files.
              For now, the columns object assumes that the 12 header names --"Name", "Field", "Type", etc will be present in each CSV
              file that we will use, and this class will probably require some modifications if we actually end up adding other data files.
    """
    def __init__(self, filename, hasHeader=True):
        self.filename = filename
        self.columns={}
        self.setReader(self.filename)
        
        self.hasHeader = hasHeader
        if self.hasHeader:
            self.headers = next(self.reader, None)
            
        
    def setColumnNumbers(self, filename):

        
        for col_num in range(len(self.headers)):
            name = self.headers[col_num]
            
            self.columns[name] = col_num
            
        self.NAME_COL_NO = self.columns["Name"]
        self.FIELD_COL_NO = self.columns["Field"]
        self.TYPE_COL_NO = self.columns["Type"]
        self.DEADLINE_COL_NO = self.columns["Deadline"]
        self.RECOMMENDERS_COL_NO = self.columns["NumberOfRecommenders"]
        self.LOCATION_COL_NO = self.columns["Location"]
        self.LINK_COL_NO = self.columns["Link"]
        self.COST_COL_NO = self.columns["Cost"]
        self.SCHOLARSHIP_LINK_COL_NO = self.columns["ScholarshipLink"]
        self.SCHOLARSHIP_DEADLINE_COL_NO = self.columns["ScholarshipDeadline"]
        self.NOTE_COL_NO = self.columns["Note"]
        self.LANGUAGE_COL_NO = self.columns["Language"]
        self.APPLICATION_FEE_COL_NO = self.columns["ApplicationFee"]
            
    def setReader(self, filename):
        
        f = open(filename,'r')
        self.reader = csv.reader(f)
            

        

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
    # items is intended to be the Opportunity object turned into a dictionary
    #   OR an occasion when the value of an attribute of Opportunity is a dictionary
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


def makePrograms(csvFile):
    """
    makePrograms(csvFile) - returns a list of Opportunity objects that will later be inserted into the GUI.
    This function uses a helper function, makeProgram to create a single one of these Opportunity objects.
    args:
    csvFile - a CsvFile object containing data on our opportunities.
    """
    reader_as_list = list(csvFile.reader)

    programs = []
    
    for row_number in range(len(reader_as_list)):
#         print(row_number)
        program = makeProgram(reader_as_list[row_number], csvFile)
        programs.append(program)
#         print(program.name)
    return programs
        
    
def makeProgram(row, csvFile):
    """
    Takes in a row representing an opportunity as well as the csvFile that we're using
    and creates an opportunity object, setting a couple attributes. Eventually this function
    should set as many attributes as we can, as all this information is contained in the
    "row" object
    args:
    row - a row in csvFile containing all of the data of a particular opportunity
    """
    name = row[csvFile.NAME_COL_NO]
    programType = row[csvFile.TYPE_COL_NO]
    link = row[csvFile.LINK_COL_NO]
    
    
    program = Opportunity(name,link=link)
    program.set_programType(programType)
    return program





""" 
everything below here is our program execution. This should eventually be put into a __main__() function
"""
grad_school_csv = CsvFile("Programs.csv")
grad_school_csv.setColumnNumbers(grad_school_csv.filename)
opportunities = makePrograms(grad_school_csv)



for i in range(0, len(opportunities)):
    treeview.insert('', 'end', opportunities[i].name, text=opportunities[i].name)
    dictionaryChecker(treeview, opportunities[i].name, opportunities[i].__dict__.items())

root.mainloop()
