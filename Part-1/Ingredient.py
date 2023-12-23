import math
from Supplier import Supplier

class Ingredient:
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
    quantity_used = 0

    def __init__(self, name:str, capacity:int, deprec:float, pantry_cost_rate:float):
        self.name = name
        self.capacity = capacity
        self.deprec = deprec
        self.pantry_cost_rate = pantry_cost_rate
    
    def get_name(self):
        return self.name
    
    def get_capacity(self):
        return self.capacity
    
    def get_deprec(self):
        return self.deprec
    
    def get_pantry_cost_rate(self):
        return self.pantry_cost_rate
    
    def get_quantity_used(self):
        return Ingredient.quantity_used
    
    def increase_quantity_used(self, demand:int, requirement):
        Ingredient.quantity_used += (demand*requirement)

    def reset_quantity_used(self):
        Ingredient.quantity_used = 0
    
    def pantry_cost(self, current_cash:float):
        leftover = self.capacity - Ingredient.quantity_used
        pantry_cost = self.pa*leftover
        print(f"Pantry {self.name} cost £{pantry_cost:.2f}")
        current_cash -= pantry_cost
        return pantry_cost

    def order_from_supplier(self):
        leftover = self.capacity - Ingredient.quantity_used
        Ingredient.quantity_used += math.ceil(leftover*self.deprec)
        if self.name.lower() == "milk":
            self.supplier_cost = Supplier.get_milk_rate()*Ingredient.quantity_used
            return self.supplier_cost
        elif self.name.lower() == "beans":
            self.supplier_cost = Supplier.get_beans_rate()*Ingredient.quantity_used
            return self.supplier_cost
        else:
            self.supplier_cost = Supplier.get_spices_rate()*Ingredient.quantity_used
            return self.supplier_cost
