import math
from fractions import Fraction

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
        self.sold = 0
    
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
    
    def get_quantity_sold(self):
        return self.sold

    def increase_sold_quantity(self, demand:int):
        self.sold = demand
    
    def reset_sold_quantity(self):
        CoffeeType.sold = 0
    
    def check_supply(self, demand:int, baristas_dict:dict, ingredients:dict):
        sufficient_supply = True
        messages = []
        ingredient_capacity = []
        total_time_available = 0
        t = []
        for barista in list(baristas_dict.values()):
            total_time_available += Fraction(80) - Fraction(barista.get_hrs_worked())
            t.append(barista.get_hrs_worked())
        for ingredient in list(ingredients.values()):
            if ingredient.get_name() == "Milk":
                req = demand*self.milk_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.milk_reqd))
                    if avl < req:
                        messages.append("Milk need {req:.1f}L, pantry contains only {avl:.1f}L".format(req=req, avl = avl))
                else:
                    pass
            elif ingredient.get_name() == "Beans":
                req = demand*self.beans_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.beans_reqd))
                    if avl < req:
                        messages.append("Beans need {req:.1f}g, pantry contains only {avl:.1f}g".format(req=req, avl = avl))
                else:
                    pass
            else:
                req = demand*self.spices_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.spices_reqd))
                    if avl < req:
                        messages.append("Spices need {req:.1f}g, pantry contains only {avl:.1f}g".format(req=req, avl = avl))
                else:
                    pass
        if (total_time_available < (((Fraction(demand)*Fraction(self.prep_time))/Fraction(60)))) and not messages:
            sufficient_supply = False
            capacity = (Fraction(total_time_available)*Fraction(60))/Fraction(self.prep_time)
            capacity = math.floor(capacity)
            print(f"Insufficient labour: quantity requested {demand}, capacity {capacity}")
            return sufficient_supply
        elif len(messages)>0 and (total_time_available > (((Fraction(demand)*Fraction(self.prep_time))/Fraction(60)))):
            sufficient_supply = False
            print("Insufficient ingredients: ")
            for message in messages:
                print(message)
            capacity = min(ingredient_capacity)
            print(f"Capacity is {capacity:.1f}")
            return sufficient_supply
        elif (total_time_available < (((Fraction(demand)*Fraction(self.prep_time))/Fraction(60)))) and len(messages)>0:
            sufficient_supply = False
            barista_capacity = math.floor((Fraction(total_time_available)*Fraction(60))/Fraction(self.prep_time))
            if barista_capacity <= min(ingredient_capacity):
                print(f"Insufficient labour: quantity requested {demand}, capacity {barista_capacity}")
            else:
                print("Insufficient ingredients: ")
                for message in messages:
                    print(message)
                    capacity = min(ingredient_capacity)
                print(f"Capacity is {capacity:.1f}")
            return sufficient_supply
        else:
            return sufficient_supply

    def calculate_income(self, current_cash:float):
        coffee_income = self.sold*self.sell_price
        current_cash += coffee_income
        self.sold = 0
        return current_cash
        

    

    


