"""Raj Dhakan (xn23972) | Part-1 | Ingredient.py contains the Ingredient class."""

import math # used for rounding up depreciated quantity value

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
        self.quantity_used = 0

    def getName(self):
        """Returns ingredient's name."""
        return self.name

    def getCapacity(self):
        """Returns ingredient's maximum quantity."""
        return self.capacity

    def getPantryCostRate(self):
        """Returns ingredient's pantry cost rate."""
        return self.pantry_cost_rate

    def getQuantityUsed(self):
        """Returns amount of ingredient used up."""
        return self.quantity_used

    def increaseQuantityUsed(self, demand:int, coffeetype):
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
            self.quantity_used += (demand*coffeetype.getMilkReqd())
        elif self.name == "Beans":
            self.quantity_used += (demand*coffeetype.getBeansReqd())
        else:
            self.quantity_used += (demand*coffeetype.getSpicesReqd())

    def resetQuantityUsed(self):
        """Resets ingredient's quantity used to 0."""
        self.quantity_used = 0

    def getLeftoverQuantity(self):
        """Calculates and returns the unused quantity of the ingredient."""
        self.leftover = self.capacity - self.quantity_used
        return self.leftover

    def getRestockCost(self, supplier):
        """
        For restocking the ingredient to its maximum capacity, getRestockCost calculates
        the total quantity to be ordered from the supplier and the respective cost.

        Parameters
        ----------
        supplier : class
            Supplier class

        Returns
        -------
        Cost of restocking a ingredient from supplier
        """
        quantity_used = self.quantity_used + math.ceil(self.leftover*self.deprec)
        if quantity_used > self.capacity:
            quantity_used = self.capacity
        if self.name == "Milk":
            restock_cost = supplier.getMilkRate()*quantity_used
            return restock_cost
        elif self.name == "Beans":
            restock_cost = supplier.getBeansRate()*quantity_used
            return restock_cost
        else:
            restock_cost = supplier.getSpicesRate()*quantity_used
            return restock_cost
