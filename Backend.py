import sqlite3


def add_to_cart(pizza_details: list[str, any]) -> None:
    """
    Add a pizza to the cart.

    @param pizza_details: Details of new pizza. This list must be in this format:
    {
        'size': 'Small' | 'Medium' | 'Large',
        'crust': 'Hand Tossed' | 'Thin 'n' Crispy' | 'Stuffed Crust',
        'toppings': list['Pepperoni' | 'Sausage' | 'Ham' | 'Onion' | 'Mushroom' | 'Green Bell Pepper' | 'Black Olives' | 'Jalapeno' | 'Banana Pepper'],
        'price': float
    }
    """

    # add row to cart table
    pass


def remove_from_cart(index: int) -> None:
    """
    Removes a pizza from the cart at the provided index.

    @param index: The location of the pizza in the cart (0 is the first, 1 is the second, and so on...)
    """
    # validate index
    # remove row from cart table
    pass


def get_cart() -> list[list[str, any]]:
    """
    Returns a list of all pizzas in the cart in this format:
    [
        {
            'size': 'Small' | 'Medium' | 'Large',
            'crust': 'Hand Tossed' | 'Thin 'n' Crispy' | 'Stuffed Crust',
            'toppings': list['Pepperoni' | 'Sausage' | 'Ham' | 'Onion' | 'Mushroom' | 'Green Bell Pepper' | 'Black Olives' | 'Jalapeno' | 'Banana Pepper'],
            'price': float
        },
        ...
    ]
    """
    # return rows form cart table

    test_pizza = {
        'size': 'Small',  
        'crust': 'Hand Tossed',  
        'toppings': ['Pepperoni', 'Sausage', 'Onion'],
        'price': 14.99
    }

    return [test_pizza]


def add_payment_method():
    """
    Not yet implemented.
    """
    # add row to payment table
    pass


def add_customer():
    """
    Not yet implemented.
    """
    # add row to customer table
    pass


def purchase_cart():
    """
    Purchases all pizzas in the cart.
    """
    # remove all rows from cart table
    # add row to purchase table
    pass


def init_db():
    """ Makes sure the database tables are setup properly """

    con = sqlite3.connect("Data.db")
    print("Database initialized")

    # ensure tables are setup properly


# Automatically initialize the database
init_db()