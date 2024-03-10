import sqlite3

class CustomerInfo:
    def __init__(self, phone_num, first_name, last_name):
        self.phone_num = phone_num
        self.first_name = first_name
        self.last_name = last_name


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
        # Insert into pizzas
        Size = pizza_details['size']
        Crust = pizza_details['crust']
        Price = pizza_details['price']
        cursor.execute(f'INSERT INTO Pizzas (Size, Crust, Price) VALUES ("{Size}", "{Crust}", {Price})')

        # Get id of the new pizza
        cursor.execute('SELECT PizzaId FROM Pizzas')
        rows = cursor.fetchall()
        last = rows[rows.__len__() - 1]
        PizzaId = last[0]

        # Insert into cart
        cursor.execute(f'INSERT INTO PizzasInCart (PizzaId) VALUES ({PizzaId})')

        # Insert into toppings
        for Name in pizza_details['toppings']:
            cursor.execute(f'INSERT INTO Toppings (PizzaId, Name) VALUES ({PizzaId}, "{Name}")')

        # Commit and close
        con.commit()
    except Exception:
        print(f'Error adding pizza to cart: {Exception}')

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
    cursor.execute('SELECT PizzaId FROM PizzasInCart')
    pizzas = cursor.fetchall()

    # Validate index
    if pizzas.__len__() == 0:
        raise IndexError('Error removing pizza from cart: Cart is empty')
    elif index < 0 or index >= pizzas.__len__():
        raise IndexError('Error removing pizza from cart: Invalid index')

    try:
        # Remove pizza from cart
        PizzaId = pizzas[index][0]
        cursor.execute(f'DELETE FROM PizzasInCart WHERE PizzaId={PizzaId}')

        # Remove pizza from pizzas table
        cursor.execute(f'DELETE FROM Pizzas WHERE PizzaId={PizzaId}')

        # Remove toppings from toppings table
        cursor.execute(f'DELETE FROM Toppings WHERE PizzaId={PizzaId}')

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

    output = []

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    # Retrieve pizzas from Cart table
    cursor.execute('SELECT PizzaId FROM PizzasInCart')
    rows = cursor.fetchall()

    # Assemble pizza details for each pizza
    for row in rows:
        PizzaId = row[0]

        # Select from Pizzas table
        cursor.execute(f'SELECT Size, Crust, Price FROM Pizzas WHERE PizzaId={PizzaId}')
        row = cursor.fetchone()

        # Setup this pizza's details
        pizza_details = {
            'size': row[0],
            'crust': row[1],
            'toppings': [],
            'price': row[2]
        }

        # Select from Toppings table
        cursor.execute(f'SELECT Name FROM Toppings WHERE PizzaId={PizzaId}')
        toppings = cursor.fetchall()
        for topping in toppings:
            pizza_details['toppings'].append(topping[0])

        # Add pizza to output list
        output.append(pizza_details)

    # Close database
    con.close()

    return output


def purchase_cart(customerInfo: CustomerInfo) -> None:
    """
    Removes all pizzas from the cart.
    """

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    #try:
        # ----- Move contents of cart to an order -----

        # Insert customer
    data = (customerInfo.phone_num, customerInfo.first_name, customerInfo.last_name)
    cursor.execute('INSERT INTO Customers (PhoneNum, FirstName, LastName) VALUES (?, ?, ?)', data)

    # Inset order
    cursor.execute(f'INSERT INTO Orders (Total, PhoneNum) VALUES (-1, {customerInfo.phone_num})')

    # Get new order id
    cursor.execute('SELECT OrderId FROM Orders')
    rows = cursor.fetchall()
    last = rows[rows.__len__() - 1]
    OrderId = last[0]

    # Select pizzas in cart
    cursor.execute('SELECT PizzaId FROM PizzasInCart')
    rows = cursor.fetchall()

    # Insert pizzas in order
    for row in rows:
        PizzaId = row[0]
        cursor.execute(f'INSERT INTO PizzasInOrder (OrderId, PizzaId) VALUES ({OrderId}, {PizzaId})')

    # Remove pizzas in cart
    cursor.execute('DELETE FROM PizzasInCart')

    # Commit and close
    con.commit()
    '''except Exception as e:
        print(f'Error purchasing cart: {e}')

        # Discard database changes
        con.rollback()'''

    # Close database
    con.close()


def calculate_price(pizza_details: list[str, any]) -> float:
    '''
    Calculates the price of a pizza based on its size and number of toppings.
    '''

    total = 0.0
    size = pizza_details['size']

    if size == 'Small':
        total += 7.99
    elif size == 'Medium':
        total += 10.99
    elif size == 'Large':
        total += 14.99
    else:
        print(f'Error calculating price: {size} is not a recognized size')
    
    total += pizza_details['toppings'].__len__() * 0.25

    return total


def init_db():
    """
    Makes sure the database tables are setup properly.
    """

    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pizzas (
            PizzaId INTEGER NOT NULL,
            Size VARCHAR(64) NOT NULL,
            Crust VARCHAR(64) NOT NULL,
            Price FLOAT NOT NULL,

            PRIMARY KEY (PizzaId)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Toppings (
            PizzaId INTEGER NOT NULL,
            Name VARCHAR(64) NOT NULL,

            PRIMARY KEY (PizzaId, Name)
            FOREIGN KEY (PizzaId) REFERENCES Pizzas(PizzaId)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PizzasInCart (
            PizzaId INTEGER NOT NULL,

            PRIMARY KEY (PizzaId)
            FOREIGN KEY (PizzaId) REFERENCES Pizzas(PizzaId)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            PhoneNum VARCHAR(16) NOT NULL,
            FirstName VARCHAR(64) NOT NULL,
            LastName VARCHAR(64) NOT NULL,

            PRIMARY KEY (PhoneNum)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            OrderId INTEGER NOT NULL,
            Total FLOAT NOT NULL,
            PhoneNum VARCHAR(16) NOT NULL,

            PRIMARY KEY (OrderId)
            FOREIGN KEY (PhoneNum) REFERENCES Customers(PhoneNum)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PizzasInOrder (
            OrderId INTEGER NOT NULL,
            PizzaId INTEGER NOT NULL,

            PRIMARY KEY (OrderId, PizzaId)
            FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            FOREIGN KEY (PizzaId) REFERENCES Pizzas(PizzaId)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
    ''')

    con.commit()
    con.close()

    print("Database initialized")


# Automatically initialize the database on import
init_db()
