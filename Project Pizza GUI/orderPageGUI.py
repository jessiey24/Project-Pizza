from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *

class OrderPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.create_widgets()
    def load_images(self):
         global final_pizzaIcon
         pizzaIcon = Image.open('mainPagePizzaIcon.ico')
         resized_pizzaIcon = pizzaIcon.resize((80, 80))
         final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon)
    
    def create_widgets(self):
        self.companyTitle = Label(self.master, font=self.font_tuple, text="PROJECT PIZZA", fg="#d65738", bg="#fae5cf", anchor=N)
        self.companyTitle.grid(column=2, row=1, columnspan = 2)

        blank_label = Label(self.master, text="               ", bg="#fae5cf")
        blank_label.grid(row=1, column=1)  
        blank_label.grid(row=1, column=2)
        blank_label.grid(row=2, column=1)

        self.load_images()
        self.orderPgIcon = Label(self.master, image=final_pizzaIcon, bg="#fae5cf")
        self.orderPgIcon.grid(row=1, column=1)

        self.pageTitle = Label(self.master, font=self.font_tuple3, text="CREATE YOUR OWN PIZZA:", fg="#d65738", bg="#fae5cf", anchor=N)
        self.pageTitle.grid(column=1, row=2)

        self.sizeTitle = Label(self.master,font = self.font_tuple4, text = "Choose your size: ", fg="#d65738", bg="#fae5cf", anchor=N )
        self.sizeTitle.grid(column =1 , row = 3)
