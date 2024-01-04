"""Raj Dhakan (xn23972) | Part-1 | CoffeeShop.py contains the CoffeeShop class."""

from fractions import Fraction # used to avoid rounding errors
from Ingredient import Ingredient
from Supplier import Supplier
from Barista import Barista
from CoffeeType import CoffeeType

class CoffeeShop:
    """
    A class to represent types of coffeeshop and its attributes.
    ...
    
    Attributes
    ----------
    name : str
        name of the coffee shop
    simulation_month : int
        the simulation month number
    fixed_monthly_rent : int
        monthly rent and utilities cost (£)
    coffeetypes : dict
        dictionary of various coffeetypes as described by CoffeeType class
    ingredients : dict
        dictionary of ingredients as described by Ingredient class
    suppliers : dict
        dictionary of supplier(s) as described by Supplier class
    current_cash : float
        cash (£) held by the shop at any given time
    chosen_barista : dict
        dictionary of baristas as described by Barista class
    all_speciality_staff_name : list
        list of all baristas names who have a coffee making speciality
    all_normal_staff_name : list
        list of all baristas names who do not have a coffee making speciality
    """
    def __init__(self, name:str):
        """Constructs all the necessary attributes for the coffeeshop object."""
        self.name = name
        self.simulation_month = None
        self.fixed_monthly_rent = 1500
        self.coffeetypes = {
            "Expresso": CoffeeType("Expresso", 0, 8, 0, 3, 500, 1.5),
            "Americano": CoffeeType("Americano", 0, 6, 0, 2, 200, 2.5),
            "Filter": CoffeeType("Filter", 0, 4, 0, 1, 300, 1.5),
            "Macchiatto": CoffeeType("Macchiatto", 0.1, 8, 2, 4, 400, 3.0),
            "Flat White": CoffeeType("Flat White", 0.2, 8, 1, 5, 600, 3.5),
            "Latte": CoffeeType("Latte", 0.3, 8, 3, 6, 1000, 4.0)
        }
        self.ingredients = {
            "Milk": Ingredient("Milk", 300, 0.4, 0.1),
            "Beans": Ingredient("Beans", 20000, 0.1, 0.001),
            "Spices": Ingredient("Spices", 4000, 0.1, 0.001)
        }
        self.suppliers = {
            "Hasty": Supplier("Hasty", 0.3, 0.1, 0.05)
        }
        self.current_cash = 10000
        self.chosen_baristas = {}
        self.all_speciality_staff_name = []
        self.all_normal_staff_name = []

    def get_coffee_types(self):
        """Returns coffeetypes dictionary."""
        return self.coffeetypes

    def get_ingredients(self):
        """Returns ingredients dictionary."""
        return self.ingredients

    def get_current_cash(self):
        """Returns cash (£) held by the shop at any given time."""
        return self.current_cash

    def get_chosen_baristas(self):
        """Returns baristas dictionary."""
        return self.chosen_baristas

    def get_all_speciality_staff_name(self):
        """Returns a list of all baristas names who have a coffee making speciality."""
        return self.all_speciality_staff_name

    def get_all_normal_staff_name(self):
        """Returns a list of all baristas names who do not have a coffee making speciality."""
        return self.all_normal_staff_name

    def set_month(self, month:int):
        """Sets the simulation month number."""
        self.simulation_month = month

    def print_header(self):
        """Prints out the header at the beginning of each month."""
        print("================================================================================")
        print(f"============================== SIMULATING MONTH {self.simulation_month} ==============================")
        print("================================================================================")

    # PROGRAM EXTENSION
    def maximise_income(self):
        """Uses bubble sort to sort coffeetypes dictionary based on largest price per unit time of barista
        so that coffee demand is attended accordingly to maximize income."""
        list_of_coffeetypes = list(self.coffeetypes.values())
        n = len(list_of_coffeetypes)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                j_0 = list_of_coffeetypes[j].get_sell_price()/list_of_coffeetypes[j].get_prep_time()
                j_1 = list_of_coffeetypes[j+1].get_sell_price()/list_of_coffeetypes[j+1].get_prep_time()
                if j_0 < j_1:
                    list_of_coffeetypes[j], list_of_coffeetypes[j+1] = list_of_coffeetypes[j+1], list_of_coffeetypes[j]
                    swapped = True
            if swapped is False:
                break
        sorted_coffeetype_dict = {}
        # creates a new dictionary with sorted values/objects
        for coffee in list_of_coffeetypes:
            sorted_coffeetype_dict.update({coffee.get_name():coffee})
        # reassigns the old the dictionary with the new one
        self.coffeetypes = sorted_coffeetype_dict

    def add_barista(self):
        "Adds barista to the chosen_baristas dictionary."
        name_exists = True # boolean used to check if the name is unique or not
        # if barista already exists then user is prompted to enter a new name
        characters = '"0123456789!@#$%^&*()~|\;:}{]{£.-+?_=,<>/'
        exception = "'"
        while name_exists is True:
            name = input("Please enter a valid barista name: ").strip().title()
            if name=="" or any(char in characters for char in name) or any(char in exception for char in name):
                print("Please enter a name with no numbers and no special characters!")
            else:
                if name in self.chosen_baristas:
                    print("Barista name already exists, please enter a unique name!")
                else:
                    barista = Barista()
                    barista.set_name(name)
                    self.chosen_baristas.update({name:barista})
                    name_exists = False
                    return name, barista

    def remove_barista(self):
        "Removes barista from the chosen_baristas dictionary and all_speciality_staff_name list."
        name_exists = False
        # prompts user to name the barista to remove and checks if that exits
        while name_exists is False:
            name = input("Please enter barista name: ").strip().title()
            if name!="":
                if name in self.chosen_baristas:
                    # if barista has any speciality
                    if name in self.all_speciality_staff_name:
                        # removes name from the respective coffeetype object
                        type_coffee = self.chosen_baristas[name].get_speciality()
                        self.coffeetypes[type_coffee].remove_speciality_staff(name)
                        # removes name from speciality staff name list
                        self.all_speciality_staff_name.remove(name)
                    else:
                        # removes name from the normal staff name list
                        self.all_normal_staff_name.remove(name)
                    print(f"Removed {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_month}")
                    del self.chosen_baristas[name]
                    name_exists = True
                else:
                    print("Please enter a valid barista name. Here are the current baristas: ")
                    print(*(list(self.chosen_baristas.keys())), sep = ", ")

    def select_speciality(self, name, barista):
        """
        Prompts user to enter barista's coffee making speciality (if any) from a list of
        coffees served at the shop.

        Parameters
        ----------
        name : str
            quantity of a particular coffee asked for
        barista : class
            Barista class

        Returns
        -------
        None
        """
        # boolean used to check if barista has any speciality or not
        speciality_valid_response = False 
        loop_bool = False
        valid_answers = ["yes","y","no","n"]
        print(f"Types of coffee served at {self.name}:")
        print(*(list(self.coffeetypes.keys())), sep = ", ")
        # keeps asking until valid response is given
        while speciality_valid_response is False:
            while loop_bool is False:
                print("Does this barista have a speciality in any one of the above coffee types?")
                speciality_exists = input("Y/N: ").strip()
                if speciality_exists.lower() in valid_answers:
                    loop_bool = True
                else:
                    print("Please enter a valid response!")
            # if positive response then prompts user to enter the type of coffee
            if speciality_exists.lower()=="y" or speciality_exists.lower()=="yes":
                speciality = input("Please enter the type of coffee: ").strip().title()
                if speciality in list(self.coffeetypes.keys()):
                    barista.set_speciality(speciality) # assigns to speciality within barista object
                    # assigns barista name within coffee type
                    self.coffeetypes[speciality].set_speciality_staff(barista.get_name())
                    # assigns barista name to the list of speciality staff only
                    self.all_speciality_staff_name.append(barista.get_name())
                    speciality_valid_response = True
                else:
                    print("Please enter a valid type of coffee! (Note: response is case sensitve)")
            else:
                # assignes barista name to the list of normal staff
                self.all_normal_staff_name.append(barista.get_name())
                speciality_valid_response = True
        print(f"Added {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_month}")

    def assign_demand(self, rem, coffeetype, demand:int, barista_list:list, speciality:bool):
        """
        Calculates the updated quantity used by the ingredient based on serving the demand.

        Parameters
        ----------
        rem : fraction
            remaining unassigned value of time for the required demand
        coffeetype : class
            CoffeeType class
        demand : int
            quantity of coffee demanded to be made
        barista_list : list
            list of baristas who are to be assigned the time to fulfil the demand
        speciality : bool
            a boolean to indicate whether the list of barista contains baristas with any
            specialities any of the coffee types

        Returns
        -------
        rem : fraction
            remaining unassigned value of time for the required demand
        """
        if speciality is True:
            denom = Fraction(120)
        else:
            denom = Fraction(60)

        for name in barista_list:
            if self.chosen_baristas[name].get_hrs_worked()!=80:
                avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                # if available (avl) hrs for each barista is greater than hrs demand for serving
                # type of coffee then all the hrs are assigned to one barista, else the remainder 
                # (rem) number of hrs is assigned to the next barista in line
                if rem >0:
                    if rem > avl:
                        rem = rem - avl
                        self.chosen_baristas[name].increase_hrs_worked(avl)
                    else:
                        self.chosen_baristas[name].increase_hrs_worked(rem)
                        rem = 0
                        break
                elif avl >= ((Fraction(demand)*Fraction(coffeetype.get_prep_time()))/denom):
                    hrs = (Fraction(demand)*Fraction(coffeetype.get_prep_time()))/denom
                    self.chosen_baristas[name].increase_hrs_worked(hrs)
                    break
                else:
                    rem = ((Fraction(demand)*Fraction(coffeetype.get_prep_time()))/denom) - avl
                    self.chosen_baristas[name].increase_hrs_worked(avl)
        return rem

    def assign_leftover_demand(self, rem, barista_list:list):
        """
        Calculates the updated quantity used by the ingredient based on serving the demand.

        Parameters
        ----------
        rem : fraction
            remaining unassigned value of time for the required demand
        barista_list : list
            list of baristas who are to be assigned the time to fulfil the demand

        Returns
        -------
        None
        """
        if rem > 0:
            for name in barista_list:
                if self.chosen_baristas[name].get_hrs_worked()!=80:
                    avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                    if rem > 0:
                        if rem > avl:
                            rem = rem - avl
                            self.chosen_baristas[name].increase_hrs_worked(avl)
                        else:
                            self.chosen_baristas[name].increase_hrs_worked(rem)
                            rem = 0
                            break

    def print_status(self):
        """Prints out the shop name, cash status, quantity of each ingredient available and
        hired baristas."""
        print(f"Shop Name: {self.name}, Cash: £{self.current_cash:.2f}")
        print("\t Pantry")
        # prints out remaining quantity of each ingredient
        for ingredient in list(self.ingredients.values()):
            if ingredient.get_name()=="Milk":
                units = "L"
            else:
                units = "g"
            print(f"\t\t {ingredient.get_name()}, remaining {ingredient.get_leftover_quantity():.2f}{units} (capacity = {ingredient.get_capacity()}{units})")
        print("\t Barista")
        # prints out baristas and their rates
        for barista in list(self.chosen_baristas.values()):
            print(f"\t\tBarista {barista.get_name()}, hourly rate = £{barista.get_rate_per_hour():.2f}")

    def collect_coffee_income(self):
        """Calculates the amount earned from quantities sold for each type of coffee."""
        for coffee in list(self.coffeetypes.values()):
            coffee_income = coffee.get_quantity_sold()*coffee.get_sell_price()
            self.current_cash += coffee_income
            coffee.reset_sold_quantity()

    def pay_monthly_rent(self):
        """Returns a boolean to indicate if there sufficient cash to pay the monthly rent and if
        there is then rent is deducted from the cash held by the shop."""
        if (self.current_cash - self.fixed_monthly_rent) < 0:
            print("Insufficient cash to make utilities payment!")
            # informs user how much is required vs current cash that shop has
            print(f"Require £{self.fixed_monthly_rent:.2f}, but only have £{self.current_cash:.2f}!")
            bankrupt = True
            return bankrupt
        else:
            self.current_cash -= self.fixed_monthly_rent
            print(f"\tPaid rent/utilities £{self.fixed_monthly_rent:.2f}")
            bankrupt = False
            return bankrupt

    def pay_baristas(self):
        """Returns a boolean to indicate if there sufficient cash to pay all the baristas and if
        there is then salaries are deducted from the cash held by the shop."""
        bankrupt = False
        for barista in list(self.chosen_baristas.values()):
            barista_salary = barista.get_rate_per_hour()*barista.get_hrs_paid()
            if (self.current_cash - barista_salary)<0:
                print(f"BANKRUPT: Insufficient cash to pay {barista.get_name()}!")
                # informs user how much is required vs current cash that shop has
                print(f"Require £{(barista_salary):.2f}, but only have £{self.current_cash:.2f}!")
                bankrupt = True
                break
            else:
                self.current_cash -= barista_salary
                barista.reset_hrs_worked()
                print(f"\tPaid {barista.get_name()}, hourly rate = £{barista.get_rate_per_hour():.2f}, amount £{(barista_salary):.2f}")
        return bankrupt

    def pay_pantry_costs(self):
        """Returns a boolean to indicate if there sufficient cash to pay all the pantry costs and if
        there is then costs are deducted from the cash held by the shop."""
        bankrupt = False
        for ingredient in list(self.ingredients.values()):
            pantry_cost = ingredient.get_pantry_cost_rate()*ingredient.get_leftover_quantity()
            if (self.current_cash - pantry_cost) <0:
                print(f"BANKRUPT: Insufficient cash to pay pantry costs for {ingredient.get_name()}!")
                # informs user how much is required vs current cash that shop has
                print(f"Require £{(pantry_cost):.2f}, but only have £{self.current_cash:.2f}!")
                bankrupt = True
                break
            else:
                self.current_cash -= pantry_cost
                print(f"\tPantry {ingredient.get_name()} cost £{pantry_cost:.2f}")
        return bankrupt

    def restock_ingredients(self):
        """Returns a boolean to indicate if there sufficient cash to restock all the ingredients and if
        there is then costs are deducted from the cash held by the shop."""
        valid_response = False # boolean used to acquire valid response
        bankrupt = False
        # prompting user to select the supplier from the list
        print("Supplier list: ")
        print(*(list(self.suppliers.keys())), sep = ", ")
        while valid_response is False:
            supplier_choose = input("Please select a supplier from the above list to restock ingredients: ").strip().title()
            if supplier_choose in self.suppliers:
                valid_response = True
            else:
                print("Supplier does not exist! (Note: response is case sensitve)")
        # looping through each ingredient to get the updated value of cash and reset its quantity
        for ingredient in list(self.ingredients.values()):
            if (self.current_cash - ingredient.get_restock_cost(self.suppliers[supplier_choose])) < 0:
                print (f"BANKRUPT: Insufficient cash to restock {ingredient.get_name()}!")
                # informs user how much is required vs current cash that shop has
                print (f"Require £{(ingredient.get_restock_cost(self.suppliers[supplier_choose])):.2f}, but only have £{self.current_cash:.2f}!")
                bankrupt = True
                break
            else:
                self.current_cash -= ingredient.get_restock_cost(self.suppliers[supplier_choose])
                ingredient.reset_quantity_used()
        return bankrupt
                    