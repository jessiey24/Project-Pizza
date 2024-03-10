from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from tkinter import messagebox
from __init__ import *


class CarryoutPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.create_widgets()
    def completeOrder(self):
       
            purchase_cart()
            allDone=messagebox.showinfo("OrderConfirmed", "Your order has been placed!")
            
    def create_widgets(self):
    # add info frame
        self.checkoutframe= LabelFrame(self.master,font=self.font_tuple5, text="Customer Information:", fg="#d65738", bg="#fae5cf", padx =25, pady = 25)
        self.checkoutframe.grid(column=1, row=1)
    # first name entry creation
        self.first_name_label = Label(self.checkoutframe, text="First Name:", font=self.font_tuple3, fg="#d65738", bg="#fae5cf")
        self.first_name_label.grid(row=1, column=1, pady=5, padx=10)
        self.first_name_entry =  Entry(self.checkoutframe)
        self.first_name_entry.grid(row=1, column=2, pady=5, padx=10)
    # last name entry creation
        self.last_name_label = Label(self.checkoutframe, text="Last Name:", font=self.font_tuple3, fg="#d65738", bg="#fae5cf")
        self.last_name_label.grid(row=2, column=1, pady=5, padx=10)
        self.last_name_entry = Entry(self.checkoutframe)
        self.last_name_entry.grid(row=2, column=2, pady=5, padx=10)
    # phone number entry creation
        self.phone_number_label = Label(self.checkoutframe, text = "Enter phone number (########## format): ", font=self.font_tuple3, fg="#d65738", bg="#fae5cf")
        self.phone_number_label.grid(row=3, column=1, pady=5, padx=10)
        self.last_name_entry = Entry(self.checkoutframe)
        self.last_name_entry.grid(row=3, column=2, pady=5, padx=10)
    #confirm order frame
        self.confirmOrderFrame = LabelFrame(self.master,font=self.font_tuple5, text="Confirm order :", fg="#d65738", bg="#fae5cf", padx =25, pady = 50)
        self.confirmOrderFrame.grid(column= 1, row=2)
    #show price
        self.show_price_label = Label(self.confirmOrderFrame, text="price breakdown will be here", font=self.font_tuple3, fg="#d65738", bg="#fae5cf").pack()
        #confirm order button 
        self.confirmOrder = Button(self.confirmOrderFrame, text="Place Order", command = self.completeOrder, font=self.font_tuple3, fg="#fae5cf", bg="#d65738").pack()
        
            


        
