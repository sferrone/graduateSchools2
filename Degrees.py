class Degrees:
    # the degree class of what a school has to offer
    # there is no space between the optional variables and the equal sign as good practice
    def __init__(self, name, deadline = "", cycle="", duration=None, courses=[], note=""):
        self.name = name
        self.deadline = deadline
        self.cycle = cycle  
        self.duration = duration
        self.courses = courses 
        self.note = note

myDegree = Degrees("Sapienza", courses = ["General Relativity", "Particle Physics"], cycle = "Magistrale", duration = 2, note = "This is my first python object")
print("name", myDegree.name)
print("cycle", myDegree.cycle)
print("duration", myDegree.duration)
print("courses = ", myDegree.courses)
print('Note: ', myDegree.note)