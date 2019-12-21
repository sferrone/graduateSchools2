class Degrees:
    # the degree class of what a school has to offer
    # there is no space between the optional variables and the equal sign as good practice
    def __init__(self, name, deadline = "", cycle="", duration=None, courses=[], note=""):
        self.SetName(name)
        self.SetDeadline(deadline)
        self.SetCycle(cycle)  
        self.SetDuration(duration)
        self.SetCourses(courses) 
        self.SetNote(note)


    def SetName(self, name):
        self.name = name
    def SetDeadline(self, deadline):
        self.deadline = deadline
    def SetCycle(self, cycle):
        self.cycle = cycle
    def SetDuration(self, duration):
        self.duration = duration
    def SetCourses(self, courses):
        self.courses = courses
    def SetNote(self, note):
        self.note = note

myDegree = Degrees("Sapienza", courses = ["General Relativity", "Particle Physics"], cycle = "Magistrale", duration = 2, note = "This is my first python object")
print("name", myDegree.name)
print("cycle", myDegree.cycle)
print("duration", myDegree.duration)
print("courses = ", myDegree.courses)
print('Note: ', myDegree.note)