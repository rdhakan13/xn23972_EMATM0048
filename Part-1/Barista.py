class Barista:
    """
    TODO: CoffeeShop class definition
    ...
    
    Attributes (TODO)
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person
    
    Methods (TODO)
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    # hrs_worked = 0

    def __init__(self, name:str):
        self.name = name
        self.hrs_paid = 120
        self.rate_per_hour = 15
        self.hrs_worked = 0

    def get_name(self):
        return self.name
    
    def get_hrs_paid(self):
        return self.hrs_paid
    
    def get_rate_per_hour(self):
        return self.rate_per_hour
    
    def get_hrs_worked(self):
        return self.hrs_worked
    
    def increase_hrs_worked(self, hrs):
        self.hrs_worked += hrs

    def reset_hrs_worked(self):
        self.hrs_worked = 0
    
    def get_paid(self, current_cash:float):
        self.hrs_worked = 0
        self.salary = self.rate_per_hour*self.hrs_paid
        current_cash -= self.salary
        return current_cash