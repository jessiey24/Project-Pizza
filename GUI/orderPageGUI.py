from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from tkinter import messagebox
from CartPageGUI import *
from Backend import *

#class definition for order page
class OrderPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.create_widgets() #this function creates all widgets that will be used on the page
        self.size = "Small" #initializing size for use in functions below
        self.crust = "Hand Tossed" #initializing crust for use in functions below
        
    def load_images(self): #loading images into page
         global final_pizzaIcon
         pizzaIcon = Image.open('mainPagePizzaIcon.ico')
         resized_pizzaIcon = pizzaIcon.resize((80, 80))
         final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon)
    
    # Creates a list of toppings based on the selected toppings
    def get_toppings_list(self):
      toppings = []
      if self.pepperoni_var.get():
        toppings.append('Pepperoni')
      if self.sausage_var.get():
        toppings.append('Sausage')
      if self.ham_var.get():
        toppings.append('Ham')
      if self.onion_var.get():
        toppings.append('Onion')
      if self.mushroom_var.get():
        toppings.append('Mushroom')
      if self.bellpepper_var.get():
        toppings.append('Green Bell Pepper')
      if self.blackolive_var.get():
        toppings.append('Black Olives')
      if self.jalapeno_var.get():
        toppings.append('Jalapeno')
      if self.bananapepper_var.get():
        toppings.append('Banana Pepper')
      return toppings
    
    #function make all values return to default
    def setDefaultPizzaOptions(self):
        self.size_clicked.set(self.sizeChoices[0])
        self.crust_clicked.set(self.crustChoices[0])
        self.pepperoni_var.set(0)
        self.sausage_var.set(0)
        self.ham_var.set(0)
        self.onion_var.set(0)
        self.mushroom_var.set(0)
        self.bellpepper_var.set(0)
        self.blackolive_var.set(0)
        self.jalapeno_var.set(0)
        self.bananapepper_var.set(0)
      #function to add all selected values to current order
        
    def addToOrder(self):
      response = messagebox.askquestion("Order Confirmation", "Would you like to add this pizza to order? ")
      if response == messagebox.YES:
        # Create PizzaDetails object to store details of the current pizza
        pizza_details = PizzaDetails(self.size, self.crust, self.get_toppings_list())
        # Add pizza to cart
        add_to_cart(pizza_details)
        # Set all values to default
        self.setDefaultPizzaOptions()
      elif response == messagebox.NO:
        # Set all values to default
        self.setDefaultPizzaOptions()


    def goToCart(self): #initiliazation of Cart Page 
       cartPage = CartPage(Toplevel(), 'Project Pizza Cart Page', 'pizzaIcon.ico', "600x600", {"bg": "#fae5cf"})  
       self.master.destroy()

      
    def create_widgets(self):
        #this label creates the company header
        self.companyTitle = Label(self.master, font=self.font_tuple, text="PROJECT PIZZA", fg="#d65738", bg="#fae5cf", anchor=N)
        self.companyTitle.grid(column=2, row=1, columnspan = 2)
        #formatting for the grid system 
        blank_label = Label(self.master, text="               ", bg="#fae5cf")
        blank_label.grid(row=1, column=1)  
        blank_label.grid(row=1, column=2)
        blank_label.grid(row=2, column=1)
        #implementation of the image being loaded into the UI
        self.load_images()
        self.orderPgIcon = Label(self.master, image=final_pizzaIcon, bg="#fae5cf")
        self.orderPgIcon.grid(row=1, column=1)
        # page title implementation 
        self.pageTitle = Label(self.master, font=self.font_tuple3, text="CREATE YOUR OWN PIZZA:", fg="#d65738", bg="#fae5cf", anchor=N)
        self.pageTitle.grid(column=1, row=2)
        # size title implementation 
        self.sizeTitle = Label(self.master,font = self.font_tuple4, text = "Choose your size: ", fg="#d65738", bg="#fae5cf", anchor = N)
        self.sizeTitle.grid(column =1 , row = 3)
        #size choices list
        self.sizeChoices = [
          "Small +$7.99",
         "Medium +$10.99",
         "Large +$14.99"
        ]
        #variable identification for size options
        self.size_clicked = StringVar()
        self.size_clicked.set(self.sizeChoices[0])
      
        #dropdown menu implementation for pizza size
        self.sizeOptions = OptionMenu(self.master, self.size_clicked, "Small +$7.99", "Medium +$10.99","Large +$14.99", command=self.apply_size_selection)
        self.sizeOptions.grid(column = 1, row= 4)
        self.apply_size_selection("")
            
        #crust title implementation
        self.crustTitle = Label(self.master,font = self.font_tuple4, text = "Choose your crust: ",fg="#d65738", bg="#fae5cf", anchor = N)
        self.crustTitle.grid(column =1 , row = 5)
        #crust choices list 
        self.crustChoices = [
          "Hand Tossed",
         "Thin 'n' Crispy",
         "Stuffed Crust +$3.99"
        ]
        #variable identification for crust options
        self.crust_clicked = StringVar()
        self.crust_clicked.set(self.crustChoices[0])

        #dropdown menu implementation for pizza crust option 
        self.crustOptions = OptionMenu(self.master, self.crust_clicked, "Hand Tossed", "Thin 'n' Crispy", "Stuffed Crust +$3.99", command=self.apply_crust_selection)
        self.crustOptions.grid(column = 1, row= 6)
        self.apply_crust_selection("")

        # toppings choices title implementation
        self.toppingTitle = Label(self.master,font = self.font_tuple4, text = "Choose your toppings: (Add $0.25 for each topping)", fg="#d65738", bg="#fae5cf", anchor = N)
        self.toppingTitle.grid(column = 2, row = 3)
        #toppings frame and checkbox menu creation 
        self.toppingsFrame = Frame(self.master, padx= 50, pady = 50, bg="#fae5cf")
        self.toppingsFrame.grid(column= 2,row = 4)
       
        #pepperoni selection
        self.pepperoni_var = IntVar()
        self.pepperoni = Checkbutton( self.toppingsFrame, text = "Pepperoni",variable = self.pepperoni_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.pepperoni.deselect()
        self.pepperoni.grid(column = 1, row=1)
        #sausage selection
        self.sausage_var = IntVar()
        self.sausage = Checkbutton( self.toppingsFrame, text = "Sausage",variable = self.sausage_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.sausage.deselect()
        self.sausage.grid(column = 2, row=1)
        #ham selection
        self.ham_var = IntVar()
        self.ham = Checkbutton( self.toppingsFrame, text = "Ham",variable = self.ham_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.ham.deselect()
        self.ham.grid(column =3, row = 1)
        #onion selection
        self.onion_var = IntVar()
        self.onion = Checkbutton( self.toppingsFrame, text = "Onion",variable = self.onion_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.onion.deselect()
        self.onion.grid(column =1, row = 2 )
        #mushroom selection
        self.mushroom_var = IntVar()
        self.mushroom = Checkbutton(self.toppingsFrame, text = "Mushroom",variable = self.mushroom_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.mushroom.deselect()
        self.mushroom.grid(column =2 , row=2 )
        #green bell pepper selection
        self.bellpepper_var = IntVar()
        self.bellpepper = Checkbutton( self.toppingsFrame, text = "Green Bell Pepper",variable = self.bellpepper_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.bellpepper.deselect()
        self.bellpepper.grid(column =3 , row = 2)
        #black olive selection 
        self.blackolive_var = IntVar()
        self.blackolive= Checkbutton( self.toppingsFrame, text = "Black Olive",variable = self.blackolive_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.blackolive.deselect()
        self.blackolive.grid(column = 1, row = 3)
        #jalapeno selection
        self.jalapeno_var = IntVar()
        self.jalapeno = Checkbutton( self.toppingsFrame, text = "Jalapeno",variable = self.jalapeno_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.jalapeno.deselect()
        self.jalapeno.grid(column = 2, row = 3)
        #banana pepper selection 
        self.bananapepper_var = IntVar()
        self.bananapepper = Checkbutton( self.toppingsFrame, text = "Banana Pepper",variable = self.bananapepper_var, fg="#d65738", bg="#fae5cf", anchor= W)
        self.bananapepper.deselect()
        self.bananapepper.grid(column= 3,row =3 )


        #add to cart button
        # I will also add some sort of functionality with adding the pizza to the cart with backend info if I can't get the list thing to work out
        self.addToCart = Button( self.master, text="Add to cart",command = self.addToOrder, bg="#d65738", fg="#fae5cf", padx=30, pady=10)
        self.addToCart.grid(column= 2, row = 5)

        #continue to cart button 
       
        self.Cart = Button(self.master, text = "Go to Cart", command = self.goToCart,bg="#d65738", fg="#fae5cf", padx=17, pady=10)
        self.Cart.grid(column=2, row = 6)
    
    # Update self.size when a new size is selected
    def apply_size_selection(self, *args):
      if self.size_clicked.get() =="Small +$7.99":
        self.size = "Small"
      elif self.size_clicked.get() == "Medium +$10.99":
        self.size = "Medium"
      elif self.size_clicked.get() == "Large +$14.99":
        self.size = "Large"
    
    # Update self.crust when a new crust is selected
    def apply_crust_selection(self, *args):
      if self.crust_clicked.get() =="Hand Tossed":
        self.crust = "Hand Tossed"
      elif self.crust_clicked.get() == "Thin 'n' Crispy":
        self.crust = "Thin 'n' Crispy"
      elif self.crust_clicked.get() == "Stuffed Crust +$3.99":
        self.crust = "Stuffed Crust"