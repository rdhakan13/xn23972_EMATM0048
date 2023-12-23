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
        self.hrs_payed = 120
        self.rate_per_hour = 15

    def get_name(self):
        return self.name
    
    def get_hrs_payed(self):
        return self.hrs_payed
    
    def get_rate_per_hour(self):
        return self.rate_per_hour
