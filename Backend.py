import sqlite3
from Pizza_Types import Pizza


def add_to_cart(pizza: Pizza) -> None:
    """
    Add a pizza to the cart.

    @param pizza: The pizza to add (note: the Pizza class can be found in Pizza_Types.py)
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


def get_cart() -> list[Pizza]:
    """
    Returns a list of all pizzas in the cart.
    """
    # return rows form cart table

    return Pizza("medium", "tossed", ["Pepperoni", "Sausage", "Ham"])


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