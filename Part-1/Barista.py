class Barista:
    """
    A class to represent barista and its attributes.
    ...
    
    Attributes
    ----------
    name : str
        name of the barista
    speciality : str
        type of coffee that barista has the speciality in making
    hrs_paid : float
        number of hours a barista gets paid for
    rate_per_hour : float
        £ per hour a barista earns
    hrs_worked : fraction
        number of hours a barista works for (maximum a barista can work for is 80hrs)
    """
    def __init__(self):
        """Constructs all the necessary attributes for the barista object."""
        self.name = ""
        self.speciality = None
        self.hrs_paid = 120
        self.rate_per_hour = 15
        self.hrs_worked = 0

    def setName(self, name:str):
        """Takes name as input and assigns it to the name attribute."""
        self.name = name

    def getName(self):
        """Returns barista's name."""
        return self.name

    def setSpeciality(self, speciality:str):
        """Takes speciality as input and assigns it to the speciality attribute."""
        self.speciality = speciality

    def getSpeciality(self):
        """Returns the speciality coffee."""
        return self.speciality

    def getHrsPaid(self):
        """Returns the number of hours a barista gets paid for."""
        return self.hrs_paid

    def getRatePerHour(self):
        """Returns £ per hour charge of a barista."""
        return self.rate_per_hour

    def getHrsWorked(self):
        """Returns the number of hours a barista has worked for."""
        return self.hrs_worked

    def increaseHrsWorked(self, hrs):
        """Increases number of hours a barista has worked for."""
        self.hrs_worked += hrs

    def resetHrsWorked(self):
        """Resets the number of hours a barista has worked for to 0."""
        self.hrs_worked = 0
