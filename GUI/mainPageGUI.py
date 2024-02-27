from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
class MainPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.load_images()
        self.create_widgets()
    def create_widgets(self):
        self.companyTitle = Label(self.master, font=self.font_tuple, text="PROJECT PIZZA", fg="#d65738", bg="#fae5cf", anchor=N)
        self.companyTitle.grid(column=2, row=3)

        blank_label = Label(self.master, text="               ", bg="#fae5cf")
        blank_label.grid(row=1, column=1)  
        blank_label.grid(row=1, column=2)
        blank_label.grid(row=2, column=1)

        self.load_images()
       

        self.mainPgIcon = Label(self.master, image=self.final_pizzaIcon, bg="#fae5cf")
        self.mainPgIcon.grid(row=3, column=1)

        self.companyMotto = Label(self.master, font=self.font_tuple2, text="WHERE YOUR PIZZA IS OUR PASSION", fg="#d65738", bg="#fae5cf", anchor=S)
        self.companyMotto.grid(row=2, column=2)

        self.mainPgImage = Label(self.master, image=self.final_pizzaImage, bg="#fae5cf")
        self.mainPgImage.grid(column=1, row=4, columnspan=3, rowspan=2, sticky=NSEW)

        self.orderNowBtn = Button(self.master, text="ORDER NOW!", bg="#d65738", fg="#fae5cf", padx=20, pady=20)
        self.orderNowBtn.grid(column=2, row=4, sticky=SW)

   
