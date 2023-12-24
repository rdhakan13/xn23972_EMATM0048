from Ingredient import Ingredient
from Supplier import Supplier
from Barista import Barista
from CoffeeType import CoffeeType
from fractions import Fraction

class CoffeeShop:
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
    # chosen_baristas = {}
    # current_cash = 10000

    def __init__(self, name:str, simulation_months:int):
        self.name = name
        self.simulation_months = simulation_months
        self.current_cash = 10000
        self.fixed_monthly_rent = 1500
        self.chosen_baristas = {}
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

    def print_header(self):
        print("==========================================================================")
        print(f"=========================== SIMULATING MONTH {self.simulation_months} ===========================")
        print("==========================================================================")    

    def select_barista(self):
        valid_response = False
        if not self.chosen_baristas:
            while valid_response is False:
                try:
                    no_of_baristas = int(input("Please enter the number of baristas to add: "))
                    if no_of_baristas > 4:
                        print("The shop can only take a maximum of 4 baristas at a time")
                    elif no_of_baristas <= 0:
                        print("Please enter a positive integer")
                    else:
                        for i in range(no_of_baristas):
                            name_exists = True
                            while name_exists is True:
                                name = input("Please enter barista name: ")
                                if name.strip()!="":
                                    if name in self.chosen_baristas:
                                        print("Barista name already exists, please enter a unique name")
                                    else:
                                        barista = Barista()
                                        barista.set_name(name)
                                        self.chosen_baristas.update({name:barista})
                                        print(f"Added {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                        name_exists = False
                        valid_response = True
                except:
                    print("Please enter a positive integer")
        else:
            while valid_response is False:
                try:
                    add_or_remove = int(input("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s) enter a negative integer (e.g. -2), no change enter '0'."))
                    if add_or_remove > 0:
                        if (add_or_remove + len(self.chosen_baristas)) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(self.chosen_baristas)}")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = True
                                while name_exists is True:
                                    name = input("Please enter barista name: ")
                                    if name.strip()!="":
                                        if name in self.chosen_baristas:
                                            print("Barista name already exists, please enter a unique name")
                                        else:
                                            barista = Barista()
                                            barista.set_name(name)
                                            self.chosen_baristas.update({name:barista})
                                            print(f"Added {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                            name_exists = False
                            valid_response = True
                    elif add_or_remove < 0:
                        if (add_or_remove + len(self.chosen_baristas)) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(self.chosen_baristas)}")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = False
                                while name_exists is False:
                                    name = input("Please enter barista name: ")
                                    if name.strip()!="":
                                        if name in self.chosen_baristas:
                                            print(f"Removed {name}, hourly rate = £{self.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                            del self.chosen_baristas[name]
                                            name_exists = True
                                        else:
                                            print("Please enter a valid barista name. Here are the current baristas: ")
                                            print(*(list(self.chosen_baristas.keys())), sep = ", ") 
                            valid_response = True
                    else:
                        valid_response = True
                except:
                    print("Please enter an integer")
    
    def attend_coffee_demand(self):
        for coffee in list(self.coffeetypes.values()):
            valid_response = False
            sufficient_supply = False
            while valid_response is False or sufficient_supply is False:
                try:
                    demand = int(input(f"Coffee {coffee.get_name()}, demand {coffee.get_mon_dem()}, how much to sell: "))
                    if demand > coffee.get_mon_dem():
                        print(f"Please enter a value less than or equal to {coffee.get_mon_dem()}")
                    elif demand >=0:
                        sufficient_supply = coffee.check_supply(demand, self.chosen_baristas, self.ingredients)
                        valid_response = True
                        if sufficient_supply is True:
                            list_of_baristas = list(self.chosen_baristas.values())
                            for i, barista in enumerate(list_of_baristas):
                                if barista.get_hrs_worked()!=80:
                                    avl = Fraction(80) - Fraction(barista.get_hrs_worked())
                                    if avl >= ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)):
                                        hrs = (Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)
                                        barista.increase_hrs_worked(hrs)
                                        break
                                    else:
                                        rem = ((Fraction(demand)*Fraction(coffee.get_prep_time()))/Fraction(60)) - avl
                                        barista.increase_hrs_worked(avl)
                                        list_of_baristas[i+1].increase_hrs_worked(rem)
                                        break
                            for ingredient in list(self.ingredients.values()):
                                ingredient.increase_quantity_used(demand,coffee)
                            coffee.increase_sold_quantity(demand)
                    else:
                        print("Please enter an integer greater than or equal to 0!")
                except:
                    print("Please enter an integer greater than or equal to 0!")
    
    def status(self):
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
                        print("Supplier list:")
                        print(*(list(self.suppliers.keys())), sep = ", ") 
                        supplier_choose = input("Please select a supplier from the above list: ")
                        if supplier_choose.strip() in self.suppliers:
                            valid_response = True
                        else:
                            print("Supplier does not exist!")
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
                        print(f"MONTH {self.simulation_months} FINAL BALANCE: {self.current_cash:.2f}")
                        print('--------------------------------------------------------------------------')
                        print(" ")
                        return bankrupt