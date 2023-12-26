import math # used to round down capacity values
from fractions import Fraction # used to avoid rounding errors

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
    sold : int
        quanitity of a coffee type sold
    speciality_staff : list
        list of staff name who have speciality in a particular coffee type
    """
    def __init__(self, name:str, milk_reqd:float,beans_reqd:int, spices_reqd:int,
                 prep_time:float, mon_dem:int, sell_price:float):
        """Constructs all the necessary attributes for the coffeetype object."""
        self.name = name
        self.milk_reqd = milk_reqd
        self.beans_reqd = beans_reqd
        self.spices_reqd = spices_reqd
        self.prep_time = prep_time
        self.mon_dem = mon_dem
        self.sell_price = sell_price
        self.sold = 0
        self.speciality_staff = []

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
        self.sold = 0

    def check_supply(self, demand:int, baristas_dict:dict, ingredients:dict):
        """
        Checks if there is enough barista hours and quantity of ingredients available to
        meet the requested demand.

        Parameters
        ----------
        demand : int
            quantity of a particular coffee type requested
        baristas_dict : dict
            dictionary of baristas as described by Barista class
        ingredients : dict
            dictionary of ingredients as described by Ingredient class

        Returns
        -------
        sufficient_supply : bool
            a boolean to indicate whether there is sufficient labour hours and ingredients
        """
        sufficient_supply = True # boolean used
        messages = [] # list of error messages when ingredients have insufficient capacity
        ingredient_capacity = [] # list to hold the maximum capacity for each ingredient with current quantities
        total_time_available = 0 # total time available from all baristas
        time_from_specialist = 0 # time available from specialist baristas

        # iterating through list of baristas to cumulate total time available (in hrs) and also separately
        # cumulate time available from specialist barista for the given coffee type
        for barista in list(baristas_dict.values()):
            total_time_available += Fraction(80) - Fraction(barista.get_hrs_worked())
            if barista.get_speciality()==self.name:
                time_from_specialist += Fraction(80) - Fraction(barista.get_hrs_worked())

        # given the time available, for both specialist and non specialist baristas, the below calculates
        # the total capacity of barista given if ingredients were not the limiting factor
        capacity_normal_staff = (Fraction(total_time_available)-Fraction(time_from_specialist))/(Fraction(self.prep_time)/Fraction(60))
        capacity_specialist = Fraction(time_from_specialist)/(Fraction(self.prep_time)/Fraction(120))
        barista_capacity = math.floor(capacity_normal_staff+capacity_specialist)

        # iterating through the ingredients dictionary to check if the each ingredient as sufficient supply
        # to meet the requested demand
        for ingredient in list(ingredients.values()):
            if ingredient.get_name() == "Milk":
                req = demand*self.milk_reqd
                if req!=0:
                    avl = ingredient.get_capacity() - ingredient.get_quantity_used()
                    ingredient_capacity.append(math.floor(avl/self.milk_reqd))
                    # if the available (avl) quantity is less than the requested (req) then an warning message
                    # is logged
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
        
        # the below provide 4 possibilities:
        # 1. barista capacity is the limiting factor (i.e. not enough barista hrs to fulfil demand)
        # 2. one or more ingredients are the limiting factor
        # 3. both barista and ingredients supplies are less than demand, however the dictating limiting
        # #  factor is found and then the appropriate error message is displayed
        # 4. all supplies are sufficient
        if ((barista_capacity < demand) and not messages):
            sufficient_supply = False
            print(f"Insufficient labour: quantity requested {demand}, capacity {barista_capacity}")
            return sufficient_supply
        elif (len(messages)>0 and (barista_capacity > demand)):
            sufficient_supply = False
            print("Insufficient ingredients: ")
            for message in messages:
                print(message)
            capacity = min(ingredient_capacity)
            print(f"Capacity is {capacity:.1f}")
            return sufficient_supply
        elif (barista_capacity < demand) and len(messages)>0:
            sufficient_supply = False
            # checks which of the two, barista or ingredient, has the least capacity as such is the
            # limiting factor
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

    def set_speciality_staff(self, name:str):
        """Assigns name to speciality staff list."""
        self.speciality_staff.append(name)

    def get_speciality_staff_list(self):
        """Returns speciality staff list."""
        return self.speciality_staff

    def remove_speciality_staff(self, name:str):
        """Removes the given name of staff from speciality staff list."""
        self.speciality_staff.remove(name)

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
    