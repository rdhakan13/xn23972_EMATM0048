from Ingredient import Ingredient
from Supplier import Supplier
from Barista import Barista
from CoffeeType import CoffeeType

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
    chosen_baristas = {}
    current_cash = 10000

    def __init__(self, name, simulation_months):
        self.name = name
        self.simulation_months = simulation_months
        self.start_cash_balance = 10000
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
            "Milk": Ingredient(),
            "Beans": Ingredient(),
            "Spices": Ingredient()
        }

    def print_header(self):
        print("================================================================")
        print(f"====================== SIMULATING MONTH {self.simulation_months} ======================")
        print("================================================================")    

    def bartista_selection(self):
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
                                if name in CoffeeShop.chosen_baristas:
                                    print("Barista name already exists, please enter a unique name")
                                else:
                                    self.chosen_baristas.update({name:Barista(name)})
                                    print(f"Added {name}, hourly rate = £{CoffeeShop.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                    name_exists = False
                        valid_response = True
                except:
                    print("Please enter a positive integer")
        else:
            while valid_response is False:
                try:
                    add_or_remove = int(input("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s) enter a negative integer (e.g. -2), no change enter '0'."))
                    if add_or_remove > 0:
                        if (add_or_remove + len(CoffeeShop.chosen_baristas)) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(CoffeeShop.chosen_baristas)}")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = True
                                while name_exists is True:
                                    name = input("Please enter barista name: ")
                                    if name in CoffeeShop.chosen_baristas:
                                        print("Barista name already exists, please enter a unique name")
                                    else:
                                        CoffeeShop.chosen_baristas.update({name:Barista(name)})
                                        print(f"Added {name}, hourly rate = £{CoffeeShop.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                        name_exists = False
                            valid_response = True
                    elif add_or_remove < 0:
                        if (add_or_remove + len(CoffeeShop.chosen_baristas)) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(CoffeeShop.chosen_baristas)}")
                        else:
                            for i in range(abs(add_or_remove)):
                                name_exists = False
                                while name_exists is False:
                                    name = input("Please enter barista name: ")
                                    if name in CoffeeShop.chosen_baristas:
                                        print(f"Removed {name}, hourly rate = £{CoffeeShop.chosen_baristas[name].get_rate_per_hour():.2f} in month {self.simulation_months}")
                                        del CoffeeShop.chosen_baristas[name]
                                        name_exists = True
                                    else:
                                        print("Please enter a valid barista name. Here are the current baristas: ")
                                        print(*(list(CoffeeShop.chosen_baristas.keys())), sep = ", ") 
                            valid_response = True
                    else:
                        valid_response = True
                except:
                    print("Please enter an integer")
    
    # def request_coffee_demand(self):
    #     valid_response = False
    #     while valid_response is False:
    #         try:
    #             request_demand = 