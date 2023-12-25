import math
from fractions import Fraction

class CoffeeType:
    """
    A class to represent types of coffee and its attributes.
    ...
    
    Attributes
    ----------
    name : str
        name of coffee type (e.g. Americano)
    milk_reqd : float
        quantity of milk required (in litres) to make the coffee
    beans_reqd : int
        quantity of beans required (in grams) to make the coffee
    spices_reqd : int
        quantity of spices required (in grams) to make the coffee
    prep_time : float
        time (in minutes) it takes to prepare the coffee
    mon_dem : int
        the number of coffees demanded in a month
    sell_price : float
        unit price of a coffee
    """
    def __init__(self, name:str, milk_reqd:float,beans_reqd:int, spices_reqd:int,
                 prep_time:float, mon_dem:int, sell_price:float):
        """Constructs all the necessary attributes for the student object."""
        self.name = name
        self.milk_reqd = milk_reqd
        self.beans_reqd = beans_reqd
        self.spices_reqd = spices_reqd
        self.prep_time = prep_time
        self.mon_dem = mon_dem
        self.sell_price = sell_price
        self.sold = 0

    def get_name(self):
        """Returns the name of coffee type."""
        return self.name

    def get_milk_reqd(self):
        """Returns the quantity of milk required (in litres)."""
        return self.milk_reqd

    def get_beans_reqd(self):
        """Returns the quantity of beans required (in grams)."""
        return self.beans_reqd

    def get_spices_reqd(self):
        """Returns the quantity of spices required (in grams)."""
        return self.spices_reqd

    def get_prep_time(self):
        """Returns the time taken to prepare 1 coffee (in minutes)."""
        return self.prep_time

    def get_mon_dem(self):
        """Returns the quantity of coffee demanded in a month."""
        return self.mon_dem

    def get_sell_price(self):
        """Returns the unit price of a coffee."""
        return self.sell_price

    def get_quantity_sold(self):
        """Returns the quantity of coffee sold in a month."""
        return self.sold

    def increase_sold_quantity(self, demand:int):
        """Increases the quantity of coffee sold in a month."""
        self.sold = demand

    def reset_sold_quantity(self):
        """Resets the quantity of coffee sold to 0."""
        CoffeeType.sold = 0

    def check_supply(self, demand:int, baristas_dict:dict, ingredients:dict):
        """
        Calculates money earned by selling a type of coffee and adds it to the shop's cash.

        Parameters
        ----------
        current_cash : float
            current amount of cash (£) held by the shop

        Returns
        -------
        Updated value of the shop's cash after adding the income from selling a type of coffee.
        """
        sufficient_supply = True
        messages = []
        ingredient_capacity = []
        total_time_available = 0
        for barista in list(baristas_dict.values()):
            total_time_available += Fraction(80) - Fraction(barista.get_hrs_worked())
        for ingredient in list(ingredients.values()):
            if ingredient.get_name() == "Milk":
                req = demand*self.milk_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.milk_reqd))
                    if avl < req:
                        messages.append(f"Milk need {req:.1f}L, pantry contains only {avl:.1f}L")
                else:
                    pass
            elif ingredient.get_name() == "Beans":
                req = demand*self.beans_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.beans_reqd))
                    if avl < req:
                        messages.append(f"Beans need {req:.1f}g, pantry contains only {avl:.1f}g")
                else:
                    pass
            else:
                req = demand*self.spices_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.spices_reqd))
                    if avl < req:
                        messages.append(f"Spices need {req:.1f}g, pantry contains only {avl:.1f}g")
                else:
                    pass
        if ((total_time_available < (((Fraction(demand)*Fraction(self.prep_time))/Fraction(60)))) 
                and not messages):
            sufficient_supply = False
            capacity = (Fraction(total_time_available)*Fraction(60))/Fraction(self.prep_time)
            capacity = math.floor(capacity)
            print(f"Insufficient labour: quantity requested {demand}, capacity {capacity}")
            return sufficient_supply
        elif (len(messages)>0 and (total_time_available > (((Fraction(demand)*Fraction(self.prep_time))/Fraction(60))))):
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
        """
        Calculates money earned by selling a type of coffee and adds it to the shop's cash.

        Parameters
        ----------
        current_cash : float
            current amount of cash (£) held by the shop

        Returns
        -------
        Updated value of the shop's cash after adding the income from selling a type of coffee.
        """
        coffee_income = self.sold*self.sell_price
        current_cash += coffee_income
        self.sold = 0
        return current_cash
    