from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from tkinter import messagebox
from DeliveryCheckout import *

class CartPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure, order, price, size, crust, selected_toppings, pizza_details):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.order = order
        self.price = price 
        self.size = size
        self.crust = crust
        self.selected_toppings = selected_toppings
        self.pizza_details = pizza_details
        self.create_widgets()

    def load_images(self): #loading images into page
         global final_pizzaIcon
         pizzaIcon = Image.open('mainPagePizzaIcon.ico')
         resized_pizzaIcon = pizzaIcon.resize((80, 80))
         final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon)
         
    def chooseDelivery(self):
        DeliveryChkout = DeliveryPage(Toplevel(), 'Project Pizza Checkout Page', 'pizzaIcon.ico', "600x600", {"bg": "#fae5cf"} )  
        self.master.withdraw()

    def chooseCarryout(self):
        pass
    '''def showOrder(self):
        #this is where I will probably just have backend instead and pull from database cause this is not working
        index = 0
        for index, pizza in enumerate(self.order):
            pizza_details = f"Size: {pizza['size']}, Crust: {pizza['crust']}, Toppings: {', '.join(pizza['toppings'])}, Price: ${pizza['price']}"
            currentOrder = Label(self.currentOrder, font=self.font_tuple4, text=pizza_details, fg="#d65738", bg="#fae5cf", anchor=NW)
            currentOrder.grid(column=0, row=index, sticky=W) 
        return currentOrder '''

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

        self.currentOrder= LabelFrame(self.master, font=self.font_tuple5, text="Current Order:", fg="#d65738", bg="#fae5cf", padx = 50, pady = 150)
        self.currentOrder.grid(column=1, row=2)
        # current order listed in frame
        self.ListOrder = Label(self.currentOrder, font=self.font_tuple5, text="List order here", fg="#d65738", bg="#fae5cf", anchor = N ).pack()
        #price listed in the frame
        self.currentPrice = LabelFrame(self.master, font=self.font_tuple5, text="Total:", fg="#d65738", bg="#fae5cf", padx = 50, pady = 150)
        self.currentPrice.grid(column=2, row=2)
        self.ListPrice = Label(self.currentPrice, font=self.font_tuple5, text="List price here", fg="#d65738", bg="#fae5cf", anchor = N )
        self.ListPrice.grid(column = 1, row = 1, columnspan= 2, rowspan = 3)
        self.chooseDelivery = Button(self.currentPrice, font=self.font_tuple3, text="Delivery +7.99", command= self.chooseDelivery, fg="#fae5cf", bg="#d65738", anchor = S )
        self.chooseDelivery.grid(column = 1, row=4)
        self.chooseCarryout = Button(self.currentPrice, font=self.font_tuple3, text="Carry-out", command = self.chooseCarryout, fg="#fae5cf", bg="#d65738", anchor = S )
        self.chooseCarryout.grid(column = 2, row=4)