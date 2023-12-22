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

    def __init__(self, name, capacity, deprec, pantry_cost_rate):
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
    
    def refill_supplier_cost(self):
        if self.name.lower() == "milk":
            self.supplier_cost = Supplier.get_milk_rate()*Ingredient.quantity_used
            return self.supplier_cost
        elif self.name.lower() == "beans":
            self.supplier_cost = Supplier.get_beans_rate()*Ingredient.quantity_used
            return self.supplier_cost
        elif self.name.lower() == "spices":
            self.supplier_cost = Supplier.get_spices_rate()*Ingredient.quantity_used
            return self.supplier_cost
    
    # def pantry
        