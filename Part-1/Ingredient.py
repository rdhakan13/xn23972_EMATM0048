import math

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
    # quantity_used = 0

    def __init__(self, name:str, capacity:int, deprec:float, pantry_cost_rate:float):
        self.name = name
        self.capacity = capacity
        self.deprec = deprec
        self.pantry_cost_rate = pantry_cost_rate
        self.quantity_used = 0
    
    def get_name(self):
        return self.name
    
    def get_capacity(self):
        return self.capacity
    
    def get_deprec(self):
        return self.deprec
    
    def get_pantry_cost_rate(self):
        return self.pantry_cost_rate
    
    def get_quantity_used(self):
        return self.quantity_used
    
    def increase_quantity_used(self, demand:int, coffee):
        if self.name == "Milk":
            self.quantity_used += (demand*coffee.get_milk_reqd())
        elif self.name == "Beans":
            self.quantity_used += (demand*coffee.get_beans_reqd())
        else:
            self.quantity_used += (demand*coffee.get_spices_reqd())

    def reset_quantity_used(self):
        self.quantity_used = 0
    
    def calculate_pantry_cost(self, current_cash:float):
        self.leftover = self.capacity - self.quantity_used
        self.pantry_cost = self.pantry_cost_rate*self.leftover
        current_cash -= self.pantry_cost
        return current_cash
    
    def get_pantry_cost(self):
        return self.pantry_cost
    
    def get_leftover_quantity(self):
        return self.leftover
    
    # def order_from_supplier(self, suppliers_list:dict):
    #     leftover = self.capacity - Ingredient.quantity_used
    #     Ingredient.quantity_used += math.ceil(leftover*self.deprec)
    #     if self.name.lower() == "milk":
    #         self.supplier_cost = Supplier.get_milk_rate()*Ingredient.quantity_used
    #         return self.supplier_cost
    #     elif self.name.lower() == "beans":
    #         self.supplier_cost = Supplier.get_beans_rate()*Ingredient.quantity_used
    #         return self.supplier_cost
    #     else:
    #         self.supplier_cost = Supplier.get_spices_rate()*Ingredient.quantity_used
    #         return self.supplier_cost
