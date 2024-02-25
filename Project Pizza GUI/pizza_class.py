from tkinter import *
from PIL import ImageTk, Image

class ProjectPizza:
    font_tuple = ("Times New Roman", 40, "normal")
    font_tuple2 = ("Times New Roman", 20, "italic")
    font_tuple3 = ("Times New Roman",15, "normal")
    font_tuple4 = ("Times New Roman", 10, "italic")

    def __init__(self, master, title, iconbitmap, geometry, configure):
        self.master = master
        self.master.title(title)
        self.master.iconbitmap(iconbitmap)
        self.master.geometry(geometry)
        self.master.configure(**configure)
        self.create_widgets()
        self.load_images()

    def load_images(self):
        pizzaIcon = Image.open('mainPagePizzaIcon.ico')
        resized_pizzaIcon = pizzaIcon.resize((80, 80))
        self.final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon)

        pizzaImage = Image.open('pizzaImage.jpeg')
        resized_pizzaImage = pizzaImage.resize((600, 300))
        self.final_pizzaImage = ImageTk.PhotoImage(resized_pizzaImage)
    

    def create_widgets(self):
        pass

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

   

  