"""Raj Dhakan (xn23972) | Part-1 | Barista.py contains the Barista class."""

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
        number of hours a barista works for (maximum a barista can work for is
        80hrs)
    """
    def __init__(self):
        """Constructs all the necessary attributes for the barista object."""
        self.name = ""
        self.speciality = None
        self.hrs_paid = 120
        self.rate_per_hour = 15
        self.hrs_worked = 0

    def set_name(self, name:str):
        """Takes name as input and assigns it to the name attribute."""
        self.name = name

    def get_name(self):
        """Returns barista's name."""
        return self.name

    def set_speciality(self, speciality:str):
        """Takes speciality as input and assigns it to the speciality attribute."""
        self.speciality = speciality

    def get_speciality(self):
        """Returns the speciality coffee."""
        return self.speciality

    def get_hrs_paid(self):
        """Returns the number of hours a barista gets paid for."""
        return self.hrs_paid

    def get_rate_per_hour(self):
        """Returns £ per hour charge of a barista."""
        return self.rate_per_hour

    def get_hrs_worked(self):
        """Returns the number of hours a barista has worked for."""
        return self.hrs_worked

    def increase_hrs_worked(self, hrs):
        """Increases number of hours a barista has worked for."""
        self.hrs_worked += hrs

    def reset_hrs_worked(self):
        """Resets the number of hours a barista has worked for to 0."""
        self.hrs_worked = 0
