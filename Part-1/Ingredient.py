import math

class Ingredient:
    """
    A class to represent ingredient and its attributes.
    ...
    
    Attributes
    ----------
    name : str
        name of the ingredient
    capacity : int
        maximum quantity of the ingredient that the shop can hold
    deprec : float
        quantity per month that the ingredient depreciates (i.e. goes bad) at the end of each month
    pantry_cost_rate : float
        cost incurred by the leftover quantity of ingredient per month
    leftover : float
        unused quantity of the ingredient
    pantry_cost : float
        total cost incurred by the leftover quantity of ingredient (i.e leftover x pantry_cost_rate)
    quantity_used : float
        quantity of the ingredient used up
    """
    def __init__(self, name:str, capacity:int, deprec:float, pantry_cost_rate:float):
        """Constructs all the necessary attributes for the ingredient object."""
        self.name = name
        self.capacity = capacity
        self.deprec = deprec
        self.pantry_cost_rate = pantry_cost_rate
        self.leftover = 0
        self.pantry_cost = 0
        self.quantity_used = 0

    def get_name(self):
        """Returns ingredient's name."""
        return self.name

    def get_capacity(self):
        """Returns ingredient's maximum quantity."""
        return self.capacity

    def get_deprec(self):
        """Returns ingredient's depreciation per month on the leftover quantity."""
        return self.deprec

    def get_pantry_cost_rate(self):
        """Returns ingredient's pantry cost rate."""
        return self.pantry_cost_rate

    def get_quantity_used(self):
        """Returns amount of ingredient used up."""
        return self.quantity_used

    def increase_quantity_used(self, demand:int, coffeetype):
        """
        Calculates the updated quantity used by the ingredient based on serving the demand.

        Parameters
        ----------
        demand : int
            quantity of a particular coffee asked for
        coffeetype : class
            CoffeeType class

        Returns
        -------
        None
        """
        if self.name == "Milk":
            self.quantity_used += (demand*coffeetype.get_milk_reqd())
        elif self.name == "Beans":
            self.quantity_used += (demand*coffeetype.get_beans_reqd())
        else:
            self.quantity_used += (demand*coffeetype.get_spices_reqd())

    def reset_quantity_used(self):
        """Resets ingredient's quantity used to 0."""
        self.quantity_used = 0

    def calculate_pantry_cost(self, current_cash:float):
        """
        Calculates the pantry cost of the ingredient using its pantry cost rate.

        Parameters
        ----------
        current_cash : float
            current amount of cash (£) held by the shop

        Returns
        -------
        Updated value of the shop's cash after taking out the pantry cost. 
        """
        self.leftover = self.capacity - self.quantity_used
        self.pantry_cost = self.pantry_cost_rate*self.leftover
        current_cash -= self.pantry_cost
        return current_cash

    def get_pantry_cost(self):
        """Returns ingredient's total pantry cost."""
        return self.pantry_cost

    def get_leftover_quantity(self):
        """Returns the unused quantity of the ingredient."""
        return self.leftover

    def order_from_supplier(self, supplier, current_cash:float):
        """
        For restocking the ingredient to its maximum capacity, order_from_supplier calculates
        the total quantity to be ordered from the supplier and the respective cost is subtracted
        from the current cash held by shop.

        Parameters
        ----------
        supplier : class
            Supplier class
        current_cash : float
            current amount of cash (£) held by the shop

        Returns
        -------
        Updated value of the shop's cash after restocking from supplier
        """
        quantity_used = self.quantity_used + math.ceil(self.leftover*self.deprec)
        if quantity_used > self.capacity:
            quantity_used = self.capacity
        if self.name == "Milk":
            current_cash -= supplier.get_milk_rate()*quantity_used
            return current_cash
        elif self.name == "Beans":
            current_cash -= supplier.get_beans_rate()*quantity_used
            return current_cash
        else:
            current_cash -= supplier.get_spices_rate()*quantity_used
            return current_cash
