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
    def __init__(self, name:str, milk_rate:float, beans_rate:float, spices_rate:float):
        self.name = name
        self.milk_rate = milk_rate
        self.beans_rate = beans_rate
        self.spices_rate = spices_rate
    
    def get_name(self):
        return self.name
    
    def get_milk_rate(self):
        return self.milk_rate
    
    def get_beans_rate(self):
        return self.beans_rate
    
    def get_spices_rate(self):
        return self.spices_rate