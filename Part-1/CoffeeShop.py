from Ingredient import Ingredient
from Supplier import Supplier
from Barista import Barista
from CoffeeType import CoffeeType
from fractions import Fraction

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

    def set_month(self, month:int):
        """Sets the simulation month number."""
        self.simulation_month = month

    def print_header(self):
        """Prints out the header at the beginning of each month."""
        print("==========================================================================")
        print(f"=========================== SIMULATING MONTH {self.simulation_month} ===========================")
        print("==========================================================================")    

    def select_barista(self):
        """Prompts user to add/remove baristas and add each barista's speciality in coffee-making."""
        valid_response = False # boolean used to check if number of baristas entered is valid
        # if there are no baristas, as is at the beginning, user is only prompted to add baristas
        if not self.chosen_baristas:
            while valid_response is False:
                try:
                    no_of_baristas = int(input("Please enter the number of baristas to add: "))
                    if no_of_baristas > 4:
                        # if more than 4 baristas are asked to enter then error message is printed
                        print("The shop can only take a maximum of 4 baristas at a time!")
                    elif no_of_baristas <= 0:
                        # if no value is entered then user is prompted again
                        print("Please enter a positive integer!")
                    else:
                        for i in range(no_of_baristas):
                            name_exists = True # boolean used to check if the name is unique or not
                            speciality_valid_response = False # boolean used to check if barista has any speciality or not
                            loop_bool = False
                            # if barista already exists then user is prompted to enter a new name
                            while name_exists is True:
                                name = input("Please enter a valid barista name: ").strip().title()
                                if name=="" or not name.isalpha():
                                    print("Please enter a name with no numbers and no special characters!")
                                else:
                                    if name in self.chosen_baristas:
                                        print("Barista name already exists, please enter a unique name!")
                                    else:
                                        barista = Barista()
                                        barista.set_name(name)
                                        self.chosen_baristas.update({name:barista})
                                        name_exists = False
                            # user is prompted if barista has any coffee making speciality
                            while speciality_valid_response is False:
                                valid_answers = ["yes","y","no","n"]
                                print(f"Types of coffee served at {self.name}:")
                                print(*(list(self.coffeetypes.keys())), sep = ", ")
                                while loop_bool is False:
                                    print("Does this barista have a speciality in any one of the above coffee types?")
                                    speciality_exists = input("Y/N: ").strip()
                                    if speciality_exists.lower() in valid_answers:
                                        loop_bool = True
                                    else:
                                        print("Please enter a valid response!")
                                if speciality_exists.lower()=="y" or speciality_exists.lower()=="yes":
                                    speciality = input("Please enter the type of coffee: ").strip().title()
                                    if speciality in list(self.coffeetypes.keys()):
                                        barista.set_speciality(speciality)
                                        self.coffeetypes[speciality].set_speciality_staff(barista.get_name())
                                        self.all_speciality_staff_name.append(barista.get_name())
                                        speciality_valid_response = True
                                    else:
                                        print("Please enter a valid type of coffee! (Note: response is case sensitve)")
                                else:
                                    self.all_normal_staff_name.append(barista.get_name())
                                    speciality_valid_response = True
                            print(f"Added {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_month}")
                        valid_response = True
                except ValueError:
                    print("Please enter a positive integer!")
        else:
            while valid_response is False:
                try:
                    print("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s)")
                    add_or_remove = int(input("enter a negative integer (e.g. -2), no change enter '0': "))
                    if add_or_remove > 0:
                        if (add_or_remove + len(self.chosen_baristas)) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(self.chosen_baristas)}!")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = True
                                speciality_valid_response = False
                                loop_bool = False
                                while name_exists is True:
                                    name = input("Please enter a valid barista name: ").strip().title()
                                    if name=="" or not name.isalpha():
                                        print("Please enter a name with no numbers and no special characters!")
                                    else:
                                        if name in self.chosen_baristas:
                                            print("Barista name already exists, please enter a unique name!")
                                        else:
                                            barista = Barista()
                                            barista.set_name(name)
                                            self.chosen_baristas.update({name:barista})
                                            name_exists = False
                                while speciality_valid_response is False:
                                    valid_answers = ["yes","y","no","n"]
                                    print(f"Types of coffee served at {self.name}:")
                                    print(*(list(self.coffeetypes.keys())), sep = ", ")
                                    while loop_bool is False:
                                        print("Does this barista have a speciality in any one of the above coffee types?")
                                        speciality_exists = input("Y/N: ").strip()
                                        if speciality_exists.lower() in valid_answers:
                                            loop_bool = True
                                        else:
                                            print("Please enter a valid response!")
                                    if speciality_exists.lower()=="y" or speciality_exists.lower()=="yes":
                                        speciality = input("Please enter the type of coffee: ").strip().title()
                                        if speciality in list(self.coffeetypes.keys()):
                                            barista.set_speciality(speciality)
                                            self.coffeetypes[speciality].set_speciality_staff(barista.get_name())
                                            self.all_speciality_staff_name.append(barista.get_name())
                                            speciality_valid_response = True
                                        else:
                                            print("Please enter a valid type of coffee! (Note: response is case sensitve)")
                                    else:
                                        self.all_normal_staff_name.append(barista.get_name())
                                        speciality_valid_response = True
                                print(f"Added {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_month}")
                            valid_response = True
                    elif add_or_remove < 0:
                        if (add_or_remove + len(self.chosen_baristas)) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(self.chosen_baristas)}!")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = False
                                while name_exists is False:
                                    name = input("Please enter barista name: ").strip().title()
                                    if name!="":
                                        if name in self.chosen_baristas:
                                            if name in self.all_speciality_staff_name:
                                                type_coffee = self.chosen_baristas[name].get_speciality()
                                                self.coffeetypes[type_coffee].remove_speciality_staff(name)
                                                self.all_speciality_staff_name.remove(name)
                                            else:
                                                self.all_normal_staff_name.remove(name)
                                            print(f"Removed {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_month}")
                                            del self.chosen_baristas[name]
                                            name_exists = True
                                        else:
                                            print("Please enter a valid barista name. Here are the current baristas: ")
                                            print(*(list(self.chosen_baristas.keys())), sep = ", ")
                            valid_response = True
                    else:
                        valid_response = True
                except ValueError:
                    print("Please enter an integer")

    def attend_coffee_demand(self):
        """Asks users to enter the quantity of each coffee type checks if demand can be achieved."""

        for coffee in list(self.coffeetypes.values()):

            # boolean used to check if demand values are valid
            valid_response = False 
            # boolean used to check if demand entered can be met with available baristas & ingredient quantities
            sufficient_supply = False 

            # loop ends when response is valid and demand can be met by available supply of baristas and ingredients
            while valid_response is False or sufficient_supply is False:

                try:

                    demand = int(input(f"Coffee {coffee.get_name()}, demand {coffee.get_mon_dem()}, how much to sell: "))

                    if demand > coffee.get_mon_dem():

                        # if input value is greater than requested demand, error message is printed
                        print(f"Please enter a value less than or equal to {coffee.get_mon_dem()}")

                    elif demand >=0:

                        # checks supplies by calling on check_supply method from CoffeeType class
                        sufficient_supply = coffee.check_supply(demand, self.chosen_baristas, self.ingredients)
                        valid_response = True
                        rem = 0
                        # if supplies are sufficient, only then baristas hrs are increased
                        if sufficient_supply is True:
                            list_of_baristas = list(self.chosen_baristas.values())
                            speciality_staff = coffee.get_speciality_staff_list()
                            if len(speciality_staff)>0:
                                for i, name in enumerate(speciality_staff):
                                    if self.chosen_baristas[name].get_hrs_worked()!=80:
                                        avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                        # if available (avl) hrs for each barista is greater than hrs demand for serving
                                        # type of coffee then all the hrs are assigned to one barista, else the remainder (rem)
                                        # number of hrs is assigned to the next barista in line
                                        if avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)):
                                            hrs = (Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)
                                            self.chosen_baristas[name].increase_hrs_worked(hrs)
                                            print(f"+ {hrs} {name}")
                                            break
                                        else:
                                            rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)) - avl
                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                            print(f"+ {avl} {name}")
                                            try:
                                                self.chosen_baristas[speciality_staff[i+1]].increase_hrs_worked(rem)
                                                print(f"+ {rem} {speciality_staff[i+1]}")
                                                rem = 0
                                                break
                                            except IndexError:
                                                break
                                if rem > 0:
                                    outstanding = rem
                                    for i, barista in enumerate(list_of_baristas):
                                        if barista.get_hrs_worked()!=80:
                                            avl = Fraction(80) - Fraction(barista.get_hrs_worked())
                                            # if available (avl) hrs for each barista is greater than hrs demand for serving
                                            # type of coffee then all the hrs are assigned to one barista, else the remainder (rem)
                                            # number of hrs is assigned to the next barista in line
                                            if avl >= outstanding:
                                                barista.increase_hrs_worked(outstanding)
                                                print(f"+{hrs} {barista.get_name()}")
                                                break
                                            else:
                                                rem = outstanding - avl
                                                barista.increase_hrs_worked(avl)
                                                list_of_baristas[i+1].increase_hrs_worked(rem)
                                                print(f"+ {avl} {barista.get_name()}")
                                                print(f"+ {rem} {list_of_baristas[i+1].get_name()}")
                                                break
                            else:
                                for i, name in enumerate(self.all_normal_staff_name):
                                    if self.chosen_baristas[name].get_hrs_worked()!=80:
                                        avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                        if avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)):
                                            hrs = (Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)
                                            self.chosen_baristas[name].increase_hrs_worked(hrs)
                                            print(f"+{hrs} {name}")
                                            break
                                        else:
                                            rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)) - avl
                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                            print(f"+{avl} {name}")
                                            try:
                                                self.chosen_baristas[self.all_normal_staff_name[i+1]].increase_hrs_worked(rem)
                                                print(f"+ {rem} {self.all_normal_staff_name[i+1]}")
                                                break
                                            except IndexError:
                                                for i, name in enumerate(self.all_speciality_staff_name):
                                                    if self.chosen_baristas[name].get_hrs_worked()!=80:
                                                        avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                                        if avl >= rem:
                                                            avl = rem
                                                            print(f"+{avl} {name}")
                                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                                            break
                                                        else:
                                                            rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)) - avl
                                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                                            self.chosen_baristas[self.all_speciality_staff_name[i+1]].increase_hrs_worked(rem)
                                                            print(f"+{avl} {name}")
                                                            print(f"+ {rem} {self.all_speciality_staff_name[i+1]}")
                                                            break
                            for ingredient in list(self.ingredients.values()):
                                ingredient.increase_quantity_used(demand,coffee)
                            coffee.increase_sold_quantity(demand)
                    else:
                        print("Please enter an integer greater than or equal to 0!")
                except ValueError:
                    print("Please enter an integer greater than or equal to 0!")

    def status(self):
        """Prints out the shop name, cash status, quantity of each ingredient available and hired baristas."""
        print(f"Shop Name: {self.name}, Cash: £{self.current_cash:.2f}")
        print("\t Pantry")
        for ingredient in list(self.ingredients.values()):
            print(f"\t\t {ingredient.get_name()}, remaining {ingredient.get_leftover_quantity():.2f} (capacity = {ingredient.get_capacity()})")
        print("\t Barista")
        for barista in list(self.chosen_baristas.values()):
            print(f"\t\tBarista {barista.get_name()}, hourly rate = £{barista.get_rate_per_hour():.2f}")

    def pay_expenses(self):
        bankrupt = False
        for coffee in list(self.coffeetypes.values()):
            self.current_cash = coffee.calculate_income(self.current_cash)
        if (self.current_cash - self.fixed_monthly_rent) < 0:
            print("Insufficient cash to make utilities payment!")
            print(f"Require £{self.fixed_monthly_rent:.2f}, but only have £{self.current_cash:.2f}!")
            bankrupt = True
            return bankrupt
        else:
            self.current_cash -= self.fixed_monthly_rent
            print(f"Paid rent/utilities £{self.fixed_monthly_rent:.2f}")
            for barista in list(self.chosen_baristas.values()):
                if barista.get_paid(self.current_cash)<0:
                    temp_value = self.current_cash - barista.get_paid(self.current_cash)
                    print(f"BANKRUPT: Insufficient cash to pay {barista.get_name()}!")
                    print(f"Require £{(temp_value):.2f}, but only have £{self.current_cash:.2f}!")
                    bankrupt = True
                    break
                else:
                    self.current_cash = barista.get_paid(self.current_cash)
                    barista.reset_hrs_worked()
                    print(f"Paid {barista.get_name()}, hourly rate = £{barista.get_rate_per_hour():.2f}, amount £{(barista.get_hrs_paid()*barista.get_rate_per_hour()):.2f}")
            if bankrupt is True:
                return bankrupt
            else:
                for ingredient in list(self.ingredients.values()):
                    if ingredient.calculate_pantry_cost(self.current_cash)<0:
                        temp_value = self.current_cash - ingredient.calculate_pantry_cost(self.current_cash)
                        print(f"BANKRUPT: Insufficient cash to pay pantry costs for {ingredient.get_name()}!")
                        print(f"Require £{(temp_value):.2f}, but only have £{self.current_cash:.2f}!")
                        bankrupt = True
                        break
                    else:
                        self.current_cash = ingredient.calculate_pantry_cost(self.current_cash)
                        print(f"Pantry {ingredient.get_name()} cost £{ingredient.get_pantry_cost():.2f}")
                if bankrupt is True:
                    return bankrupt
                else:
                    CoffeeShop.status(self)
                    valid_response = False
                    while valid_response is False:
                        print("Supplier list: ")
                        print(*(list(self.suppliers.keys())), sep = ", ") 
                        supplier_choose = input("Please select a supplier from the above list to restock ingredients: ").strip().title()
                        if supplier_choose in self.suppliers:
                            valid_response = True
                        else:
                            print("Supplier does not exist! (Note: response is case sensitve)")
                    for ingredient in list(self.ingredients.values()):
                        if ingredient.order_from_supplier(self.suppliers[supplier_choose], self.current_cash) < 0:
                            temp_value = self.current_cash - ingredient.order_from_supplier(supplier_choose, self.current_cash)
                            print (f"BANKRUPT: Insufficient cash to restock {ingredient.get_name()}!")
                            print (f"Require £{(temp_value):.2f}, but only have £{self.current_cash:.2f}!")
                            bankrupt = True
                        else:
                            self.current_cash = ingredient.order_from_supplier(self.suppliers[supplier_choose], self.current_cash)
                            ingredient.reset_quantity_used()
                    if bankrupt is True:
                        return bankrupt
                    else:
                        print("All expenses have been paid!")
                        print("All ingredients have been fully restocked.")
                        print(f"MONTH {self.simulation_month} FINAL BALANCE: {self.current_cash:.2f}")
                        print('--------------------------------------------------------------------------')
                        print(" ")
                        return bankrupt
                    