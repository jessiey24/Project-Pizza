from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from tkinter import messagebox


class CartPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure, order, price, size, crust, selected_toppings, pizza_details):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.order = order
        self.price = price, 
        self.size = size,
        self.crust = crust,
        self.selected_toppings = selected_toppings,
        self.pizza_details = pizza_details
    
       
        for pizza in self.order:
            pizza_details = f"Size: {pizza['size']}, Crust: {pizza['crust']}, Toppings: {', '.join(pizza['toppings'])}, Price: ${pizza['price']}"
            currentOrder = Label(self.master, font=self.font_tuple4, text=pizza_details, fg="#d65738", bg="#fae5cf",
                                 anchor=N)
            currentOrder.grid(column=1, row=1) 
            