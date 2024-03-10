import sqlite3


class CustomerInfo:
    def __init__(self, phone_num: str, first_name: str, last_name: str):
        self.phone_num = phone_num
        self.first_name = first_name
        self.last_name  = last_name


class PizzaDetails:
    def __init__(self, size: str, crust: str, toppings: list[str]):
        # Make sure provided values are valid
        if not self.is_valid_size(size):
            raise Exception(f'Error creating PizzaDetails: "{size}" is not a valid size name. Valid sizes are "Lage", "Medium", and "Small".')
        if not self.is_valid_crust(crust):
            raise Exception(f'Error creating PizzaDetails: "{crust}" is not a valid crust name. Valid crust names are "Hand Tossed", "Thin \'n\' Crispy", and "Stuffed Crust".')
        if not self.are_valid_toppings(toppings):
            raise Exception('Error creating PizzaDetails: One of the toppings has an invalid name')
        
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def __str__(self) -> str:
        toppings_str = ''

        first = False
        for topping in self.toppings:
            if not first:
                toppings_str += ' w/ '
                first = True
            else:
                toppings_str += ', '

            toppings_str += topping 

        return f'{self.size}, {self.crust}' + toppings_str
        pass

    def get_price(self) -> float:
        price = 0.0

        if self.size == 'Small':
            price += 7.99
        elif self.size == 'Medium':
            price += 10.99
        elif self.size == 'Large':
            price += 14.99
        
        price += self.toppings.__len__() * 0.25

        if self.crust == 'Stuffed Crust':
            price += 3.99

        return price

    def is_valid_size(self, size: str):
        return size == 'Small' or size == 'Medium' or size == 'Large'

    def is_valid_crust(self, crust: str):
        return crust == 'Hand Tossed' or crust == "Thin 'n' Crispy" or crust == 'Stuffed Crust'

    def is_valid_topping(self, topping: str):
        return topping == 'Pepperoni' or topping == 'Sausage' or topping == 'Ham' or topping == 'Onion' or topping == 'Mushroom' or topping == 'Green Bell Pepper' or topping == 'Black Olives' or topping == 'Jalapeno' or topping == 'Banana Pepper'

    def are_valid_toppings(self, toppings: list[str]):
        for topping in toppings:
            if not self.is_valid_topping(topping):
                return False
            
        return True


def add_to_cart(pizza_details: PizzaDetails) -> None:
    """
    Add a pizza to the cart.
    """

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    try:
        # Insert into pizzas
        cursor.execute(f'INSERT INTO Pizzas (Size, Crust, Price) VALUES ("{pizza_details.size}", "{pizza_details.crust}", {pizza_details.get_price()})')

        # Get id of the new pizza
        cursor.execute('SELECT PizzaId FROM Pizzas')
        rows = cursor.fetchall()
        last = rows[rows.__len__() - 1]
        PizzaId = last[0]

        # Insert into cart
        cursor.execute(f'INSERT INTO PizzasInCart (PizzaId) VALUES ({PizzaId})')

        # Insert into toppings
        for topping in pizza_details.toppings:
            cursor.execute(f'INSERT INTO Toppings (PizzaId, Name) VALUES ({PizzaId}, "{topping}")')

        # Commit and close
        con.commit()
    except Exception as e:
        print(f'Error adding pizza to cart: {e}')

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
    except Exception as e:
        print(f'Error removing pizza from cart: {e}')

        # Discard database changes
        con.rollback()

    # Close database
    con.close()


def get_cart() -> list[PizzaDetails]:
    """
    Returns a list of all pizzas in the cart.
    """

    output: list[PizzaDetails] = []

    # Open DB connection
    con = sqlite3.connect("Data.db")
    cursor = con.cursor()

    # Retrieve pizzas from Cart table
    cursor.execute('SELECT PizzaId FROM PizzasInCart')
    rows = cursor.fetchall()

    # Assemble pizza details for each pizza
    for cart_row in rows:
        PizzaId = cart_row[0]

        # Select pizza from Pizzas table
        cursor.execute(f'SELECT Size, Crust, Price FROM Pizzas WHERE PizzaId={PizzaId}')
        pizza_row = cursor.fetchone()

        # Select from Toppings table
        toppings: list[str] = []
        cursor.execute(f'SELECT Name FROM Toppings WHERE PizzaId={PizzaId}')
        toppings_rows = cursor.fetchall()
        for toppings_row in toppings_rows:
            toppings.append(toppings_row[0])

        # Add pizza to output list
        output.append(PizzaDetails(pizza_row[0], pizza_row[1], toppings))

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

    # Get total cost of cart
    total = 0.0
    for pizza in get_cart():
        total += pizza.get_price()

    try:
        # Insert customer
        data = (customerInfo.phone_num, customerInfo.first_name, customerInfo.last_name)
        cursor.execute('INSERT INTO Customers (PhoneNum, FirstName, LastName) VALUES (?, ?, ?)', data)

        # Inset order
        cursor.execute(f'INSERT INTO Orders (Total, PhoneNum) VALUES ({total}, {customerInfo.phone_num})')

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
    except Exception as e:
        print(f'Error purchasing cart: {e}')

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
