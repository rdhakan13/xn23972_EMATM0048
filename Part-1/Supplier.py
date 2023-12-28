class Supplier:
    """
    A class to represent supplier and its attributes.
    ...
    
    Attributes
    ----------
    name : str
        name of the supplier
    milk_rate : float
        price per litre of milk charged by the supplier
    beans_rate : float
        price per gram of beans charged by the supplier
    spices_rate : float
        price per gram of spices charged by the supplier
    """
    def __init__(self, name:str, milk_rate:float, beans_rate:float, spices_rate:float):
        """Constructs all the necessary attributes for the supplier object."""
        self.name = name
        self.milk_rate = milk_rate
        self.beans_rate = beans_rate
        self.spices_rate = spices_rate

    def getMilkRate(self):
        """Returns suppliers milk rate."""
        return self.milk_rate

    def getBeansRate(self):
        """Returns suppliers beans rate."""
        return self.beans_rate

    def getSpicesRate(self):
        """Returns suppliers spices rate."""
        return self.spices_rate
