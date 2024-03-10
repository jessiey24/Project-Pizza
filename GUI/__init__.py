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

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    try:
        # Insert into cart
        size = pizza_details['size']
        crust = pizza_details['crust']
        price = pizza_details['price']
        cursor.execute(f'INSERT INTO Cart (Size, Crust, Price) VALUES ("{size}", "{crust}", {price})')

        # Get id of new pizza
        cursor.execute('SELECT PizzaId FROM Cart')
        rows = cursor.fetchall()
        last = rows[rows.__len__() - 1]
        pizzaId = last[0]

        # Insert toppings
        for topping in pizza_details['toppings']:
            cursor.execute(f'INSERT INTO Toppings (PizzaId, Name) VALUES ({pizzaId}, "{topping}")')

        # Commit and close
        con.commit()
    except:
        print('Error adding pizza to cart')

        # Discard database changes
        con.rollback()

    # Close database
    con.close()


def remove_from_cart(index: int) -> None:
    """
    Removes a pizza from the cart at the specified index.

    @param index: The location of the pizza in the cart (0 is the first, 1 is the second, and so on...)
    """
    
    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    # Get pizzas in cart
    cursor.execute('SELECT PizzaId FROM Cart')
    pizzas = cursor.fetchall()

    # Validate index
    if pizzas.__len__() == 0:
        raise IndexError('Error removing pizza from cart: Cart is empty')
    elif index < 0 or index >= pizzas.__len__():
        raise IndexError('Error removing pizza from cart: Invalid index')

    try:
        # Remove row from Cart table
        pizzaId = pizzas[index][0]
        cursor.execute(f'DELETE FROM Cart WHERE PizzaId={pizzaId}')

        # Remove toppings form Toppings table
        cursor.execute(f'DELETE FROM Toppings WHERE PizzaId={pizzaId}')

        # Commit and close
        con.commit()
    except:
        print('Error removing pizza from cart')

        # Discard database changes
        con.rollback()

    # Close database
    con.close()


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
    
    # Get all rows in Cart table
    # For each, get all its toppings

    pizzas_output = []

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    # Retrieve pizzas from Cart table
    cursor.execute('SELECT * FROM Cart')
    rows = cursor.fetchall()

    # Assemble pizza details for each pizza
    for row in rows:
        pizza_id = row[0]
        size = row[1]
        crust = row[2]
        price = row[3]

        pizza_details = {
            'size': size,
            'crust': crust,
            'toppings': [],
            'price': price
        }

        # Get toppings for this pizza
        cursor.execute(f'SELECT Name FROM Toppings WHERE PizzaId={pizza_id}')
        toppings = cursor.fetchall()
        for topping in toppings:
            pizza_details['toppings'].append(topping[0])

        # Add pizza to output
        pizzas_output.append(pizza_details)

    # Close database
    con.close()

    return pizzas_output


def purchase_cart():
    """
    Removes all pizzas from the cart.
    """

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    try:
        # Remove all rows from Cart table
        cursor.execute(f'DELETE FROM Cart')

        # Remove all rows form Toppings table
        cursor.execute(f'DELETE FROM Toppings')

        # Commit and close
        con.commit()
    except:
        print('Error purchasing cart cart')

        # Discard database changes
        con.rollback()

    # Close database
    con.close()


def init_db():
    """
    Makes sure the database tables are setup properly.
    """

    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    # Ensure Cart table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cart (
            PizzaId INTEGER NOT NULL,
            Size VARCHAR(64) NOT NULL,
            Crust VARCHAR(64) NOT NULL,
            Price FLOAT NOT NULL,
                   
            PRIMARY KEY (PizzaId)
        )
    ''')

    # Ensure Toppings table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Toppings (
            PizzaId INTEGER NOT NULL,
            Name VARCHAR(64) NOT NULL,
                   
            PRIMARY KEY (PizzaId, Name)
            FOREIGN KEY (PizzaId) REFERENCES Cart(PizzaId)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
    ''')

    con.commit()
    con.close()

    print("Database initialized")


# Automatically initialize the database on import
init_db()

__all__ = ['add_to_cart', 'remove_from_cart', 'get_cart', 'purchase_cart']