from Ingredient import Ingredient

class CoffeeType:
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
    def __init__(self, name:str, milk_reqd:float, beans_reqd:int, spices_reqd:int, prep_time:int, mon_dem:int, sell_price:float):
        self.name = name
        self.milk_reqd = milk_reqd
        self.beans_reqd = beans_reqd
        self.spices_reqd = spices_reqd
        self.prep_time = prep_time
        self.mon_dem = mon_dem
        self.sell_price = sell_price
    
    def get_name(self):
        return self.name
    
    def get_milk_reqd(self):
        return self.milk_reqd
    
    def get_beans_reqd(self):
        return self.beans_reqd
    
    def get_spices_reqd(self):
        return self.spices_reqd
    
    def get_prep_time(self):
        return self.prep_time
    
    def get_mon_dem(self):
        return self.mon_dem
    
    def get_sell_price(self):
        return self.sell_price
    
    def check(self, baristas_dict:dict, ingredients:dict):
        valid_response = False
        while valid_response is False:
            try:
                demand = int(input(f"Coffee {self.name()}, demand {self.mon_dem()}, how much to sell: "))
                if demand >= 0:
                    calculate
                    valid_response = True
                else:
                    print("Please enter a value greater than or equal to 0!")
            except:
                print("Please enter a value greater than or equal to 0!")
        match self.name:
            case ""
        

    

    


