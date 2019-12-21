class Degrees:
    # the degree class of what a school has to offer
    # there is no space between the optional variables and the equal sign as good practice
    def __init__(self, name, deadline = None, cycle="", duration=None, courses=[], note=""):
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

