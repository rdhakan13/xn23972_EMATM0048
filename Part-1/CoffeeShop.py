from Ingredient import Ingredient
from Supplier import Supplier
from Barista import Barista
from CoffeeType import CoffeeType
from fractions import Fraction # used to avoid rounding errors

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
                        valid_response = True
                except ValueError:
                    print("Please enter a positive integer!")
        else:
            # if there are already barista, as with the case with month 2 onwards, then the option of removing
            # baristas becomes valid and also to make no change
            while valid_response is False:
                try:
                    print("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s)")
                    add_or_remove = int(input("enter a negative integer (e.g. -2), no change enter '0': "))
                    # if decides to add barista
                    if add_or_remove > 0:
                        # checks if no more than 4 baristas
                        if (add_or_remove + len(self.chosen_baristas)) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(self.chosen_baristas)}!")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = True
                                speciality_valid_response = False
                                loop_bool = False
                                # prompts user to input name
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
                                # prompts user if new barista has any speciality in any of the coffee types
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
                    # if user decides to remove baristas
                    elif add_or_remove < 0:
                        # checks if there will be at least one barista
                        if (add_or_remove + len(self.chosen_baristas)) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(self.chosen_baristas)}!")
                        else:
                            for i in range(abs(add_or_remove)):
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
                            valid_response = True
                    else:
                        valid_response = True
                except ValueError:
                    print("Please enter an integer")

    def attend_coffee_demand(self):
        """Asks users to enter the quantity of each coffee type checks if demand can be achieved."""
        # loops through each coffee
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
                        rem = 0  # remainder variable used when the total time to prepare the demanded coffee is
                        # split between two or more baristas
                        # if supplies are sufficient, only then baristas hrs are increased
                        if sufficient_supply is True:
                            list_of_baristas = list(self.chosen_baristas.values())
                            # fetches list of speciality staff saved in the coffeetype class
                            speciality_staff = coffee.get_speciality_staff_list()
                            # checks if there are any speciality staff
                            if len(speciality_staff)>0:
                                # if there are speciality staff dedicated to the type of coffee in the LOOP 
                                # then it loops through the list
                                for i, name in enumerate(speciality_staff):
                                    if self.chosen_baristas[name].get_hrs_worked()!=80:
                                        avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                        # if available (avl) hrs for each barista is greater than hrs demand for serving
                                        # type of coffee then all the hrs are assigned to one barista, else the remainder (rem)
                                        # number of hrs is assigned to the next barista in line
                                        if rem >0:
                                            if rem > avl:
                                                rem = rem - avl
                                                self.chosen_baristas[name].increase_hrs_worked(avl)
                                                print(f"+ {avl} {name}")
                                            else:
                                                self.chosen_baristas[name].increase_hrs_worked(rem)
                                                print(f"+ {rem} {name}")
                                                rem = 0
                                                break
                                        elif avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)):
                                            hrs = (Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)
                                            self.chosen_baristas[name].increase_hrs_worked(hrs)
                                            print(f"+ {hrs} {name}")
                                            break
                                        else:
                                            rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(120)) - avl
                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                            print(f"+ {avl} {name}")
                                # if there isn't a speciality staff in line, it assigns time to any other barista
                                if rem > 0:
                                    for i, barista in enumerate(list_of_baristas):
                                        if barista.get_hrs_worked()!=80:
                                            avl = Fraction(80) - Fraction(barista.get_hrs_worked())
                                            if rem > 0:
                                                if rem > avl:
                                                    rem = rem - avl
                                                    barista.increase_hrs_worked(avl)
                                                    print(f"+{avl} {barista.get_name()}")
                                                else:
                                                    barista.increase_hrs_worked(rem)
                                                    print(f"+{rem} {barista.get_name()}")
                                                    rem = 0
                                                    break
                            # if there are no speciality staff at all
                            else:
                                # loops through the normal staff list first
                                for i, name in enumerate(self.all_normal_staff_name):
                                    if self.chosen_baristas[name].get_hrs_worked()!=80:
                                        avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                        if rem > 0:
                                            if rem > avl:
                                                rem = rem - avl
                                                self.chosen_baristas[name].increase_hrs_worked(avl)
                                                print(f"+{avl} {name}")
                                            else:
                                                self.chosen_baristas[name].increase_hrs_worked(rem)
                                                print(f"+{rem} {name}")
                                                rem = 0
                                                break
                                        elif avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)):
                                            hrs = (Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)
                                            self.chosen_baristas[name].increase_hrs_worked(hrs)
                                            print(f"+{hrs} {name}")
                                            break
                                        else:
                                            rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)) - avl
                                            self.chosen_baristas[name].increase_hrs_worked(avl)
                                            print(f"+{avl} {name}")
                                # if there isn't a barista that is normal, then it loops through all speciality staff
                                # which is not for coffee type in the LOOP (i.e. if a barista specialising in latte is
                                # can be assigned time to fulfill demand for filter coffee)
                                if rem >0:
                                    for i, name in enumerate(self.all_speciality_staff_name):
                                        if self.chosen_baristas[name].get_hrs_worked()!=80:
                                            avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                            # the remainder from the previous loop is now distributed amongst
                                            if rem > 0:
                                                if rem > avl:
                                                    rem = rem - avl
                                                    self.chosen_baristas[name].increase_hrs_worked(avl)
                                                    print(f"+{avl} {name}")
                                                else:
                                                    self.chosen_baristas[name].increase_hrs_worked(rem)
                                                    print(f"+{rem} {name}")
                                                    rem = 0
                                                    break
                                # if remainder (rem) is zero then it suggests that there no normal baristas, or baristas
                                # with coffee making speciality to the coffeetype currently in LOOP, therefore it loops direct
                                if len(self.all_normal_staff_name)==0:
                                    for i, name in enumerate(self.all_speciality_staff_name):
                                        if self.chosen_baristas[name].get_hrs_worked()!=80:
                                            avl = Fraction(80) - Fraction(self.chosen_baristas[name].get_hrs_worked())
                                            if rem > 0:
                                                if rem > avl:
                                                    rem = rem - avl
                                                    self.chosen_baristas[name].increase_hrs_worked(avl)
                                                    print(f"+{avl} {name}")
                                                else:
                                                    self.chosen_baristas[name].increase_hrs_worked(rem)
                                                    print(f"+{rem} {name}")
                                                    rem = 0
                                                    break
                                            elif avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)):
                                                avl = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60))
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
                            # updates the quantity sold within the coffeetype class
                            coffee.increase_sold_quantity(demand)
                    else:
                        print("Please enter an integer greater than or equal to 0!")
                except ValueError:
                    print("Please enter an integer greater than or equal to 0!")

    def status(self):
        """Prints out the shop name, cash status, quantity of each ingredient available and hired baristas."""
        print(f"Shop Name: {self.name}, Cash: £{self.current_cash:.2f}")
        print("\t Pantry")
        # prints out remaining quantity of each ingredient
        for ingredient in list(self.ingredients.values()):
            print(f"\t\t {ingredient.get_name()}, remaining {ingredient.get_leftover_quantity():.2f} (capacity = {ingredient.get_capacity()})")
        print("\t Barista")
        # prints out baristas and their rates
        for barista in list(self.chosen_baristas.values()):
            print(f"\t\tBarista {barista.get_name()}, hourly rate = £{barista.get_rate_per_hour():.2f}")

    def pay_expenses(self):
        """Updates cash of coffee shop by paying out expenses; if at any point there is insufficient cash
        then program halts and an error messages informs which expense could not be satisfied."""
        bankrupt = False # boolean used to stop the program when cash is insufficient
        # order of cash updates follows as such:
        # 1. add income from selling different types of coffee
        # 2. paying up utilities/rent
        # 3. paying up baristas salary
        # 4. paying up pantry costs
        # 5. paying up supplier to restock the ingredients to full capacity

        # 1. add income from selling different types of coffee
        for coffee in list(self.coffeetypes.values()):
            self.current_cash = coffee.calculate_income(self.current_cash)
        # 2. paying up utilities/rent
        if (self.current_cash - self.fixed_monthly_rent) < 0:
            print("Insufficient cash to make utilities payment!")
            # informs user how much is required vs current cash that shop has
            print(f"Require £{self.fixed_monthly_rent:.2f}, but only have £{self.current_cash:.2f}!")
            bankrupt = True
            return bankrupt
        else:
            self.current_cash -= self.fixed_monthly_rent
            print(f"Paid rent/utilities £{self.fixed_monthly_rent:.2f}")
            # 3. paying up baristas salary
            # looping through all baristas to pay them up
            for barista in list(self.chosen_baristas.values()):
                if barista.get_paid(self.current_cash)<0:
                    temp_value = self.current_cash - barista.get_paid(self.current_cash)
                    print(f"BANKRUPT: Insufficient cash to pay {barista.get_name()}!")
                    # informs user how much is required vs current cash that shop has
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
                # 4. paying up pantry costs
                # looping through each ingredient to pay up pantry cost
                for ingredient in list(self.ingredients.values()):
                    if ingredient.calculate_pantry_cost(self.current_cash)<0:
                        temp_value = self.current_cash - ingredient.calculate_pantry_cost(self.current_cash)
                        print(f"BANKRUPT: Insufficient cash to pay pantry costs for {ingredient.get_name()}!")
                        # informs user how much is required vs current cash that shop has
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
                    valid_response = False # boolean value used to acquire a valid response
                    # 5. paying up supplier to restock the ingredients to full capacity
                    # selecting supplier
                    while valid_response is False:
                        print("Supplier list: ")
                        print(*(list(self.suppliers.keys())), sep = ", ") 
                        supplier_choose = input("Please select a supplier from the above list to restock ingredients: ").strip().title()
                        if supplier_choose in self.suppliers:
                            valid_response = True
                        else:
                            print("Supplier does not exist! (Note: response is case sensitve)")
                    # looping through each ingredient to get the updated value of cash and reset its quantity
                    for ingredient in list(self.ingredients.values()):
                        if ingredient.order_from_supplier(self.suppliers[supplier_choose], self.current_cash) < 0:
                            temp_value = self.current_cash - ingredient.order_from_supplier(supplier_choose, self.current_cash)
                            print (f"BANKRUPT: Insufficient cash to restock {ingredient.get_name()}!")
                            # informs user how much is required vs current cash that shop has
                            print (f"Require £{(temp_value):.2f}, but only have £{self.current_cash:.2f}!")
                            bankrupt = True
                        else:
                            self.current_cash = ingredient.order_from_supplier(self.suppliers[supplier_choose], self.current_cash)
                            ingredient.reset_quantity_used()
                    if bankrupt is True:
                        return bankrupt
                    # Prints final message
                    else:
                        print("All expenses have been paid!")
                        print("All ingredients have been fully restocked.")
                        print(f"MONTH {self.simulation_month} FINAL BALANCE: {self.current_cash:.2f}")
                        print('--------------------------------------------------------------------------')
                        print(" ")
                        return bankrupt
                    