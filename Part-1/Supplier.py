class Supplier:
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
    def __init__(self, name:str):
        self.name = name
        self.milk_rate = 0.3
        self.beans_rate = 0.1
        self.spices_rate = 0.05
    
    def get_name(self):
        return self.name
    
    def get_milk_rate(self):
        return self.milk_rate
    
    def get_beans_rate(self):
        return self.beans_rate
    
    def get_spices_rate(self):
        return self.spices_rate