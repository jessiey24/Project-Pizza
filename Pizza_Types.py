class Pizza:
    """
    A collection of values and methods for pizzas

    @param size: str - Available sizes are "small", "medium", and "large"
    @param crust: str - Available values are "tossed", "thin", and "stuffed"
    @param toppings: list[str] - List of topping names
    """

    def __init__(self, size: str, crust: str, toppings: list[str]):
        self.size = size
        self.crust = crust
        self.toppings = toppings
