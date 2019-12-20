class School:
    def __init__(self, name, location=None, note="", degrees=[]):
        self.SetName(name)
        self.SetLocation(location)
        self.SetNote(note)
        self.SetDegrees(degrees)

    def SetName(self, name):
        self.name = name

    def SetLocation(self, location):
        self.location = location

    def SetNote(self, note):
        self.note = note

    def SetDegrees(self, degrees):
        self.degrees = degrees
