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
    hrs_worked = 0

    def __init__(self, name:str):
        self.name = name
        self.hrs_paid = 120
        self.rate_per_hour = 15

    def get_name(self):
        return self.name
    
    def get_hrs_payed(self):
        return self.hrs_paid
    
    def get_rate_per_hour(self):
        return self.rate_per_hour
    
    def get_hrs_worked(self):
        return Barista.hrs_worked
    
    def increase_hrs_worked(self, hrs):
        Barista.hrs_worked += hrs

    def reset_hrs_worked(self):
        Barista.hrs_worked = 0
    
    def get_paid(self, current_cash:float):
        Barista.hrs_worked = 0
        salary = self.rate_per_hour*self.hrs_paid
        current_cash -= salary
        print(f"Paid {self.name}, hourly rate = £{self.rate_per_hour:.2f}, amount £{(self.hrs_paid*self.rate_per_hour):.2f}")
        return current_cash