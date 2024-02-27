from tkinter import *
from PIL import ImageTk, Image
# Initial class description that every window will have
class ProjectPizza:
    font_tuple = ("Times New Roman", 40, "normal") #Title font for main page
    font_tuple2 = ("Times New Roman", 20, "italic") #Subtitle font for the company motto
    font_tuple3 = ("Times New Roman",12, "normal") #Font for the other page titles 
    font_tuple4 = ("Times New Roman", 10, "italic") #headings for different instructions/choices

    def __init__(self, master, title, iconbitmap, geometry, configure): #attributes all windows will have
        self.master = master
        self.master.title(title)
        self.master.iconbitmap(iconbitmap)
        self.master.geometry(geometry)
        self.master.configure(**configure)
        self.create_widgets()
        self.load_images()

#function to help load images into windows
    def load_images(self):
        pizzaIcon = Image.open('mainPagePizzaIcon.ico')
        resized_pizzaIcon = pizzaIcon.resize((80, 80))
        self.final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon)

        pizzaImage = Image.open('pizzaImage.jpeg')
        resized_pizzaImage = pizzaImage.resize((600, 300))
        self.final_pizzaImage = ImageTk.PhotoImage(resized_pizzaImage)
    
#function to create widgets
    def create_widgets(self):
        pass

  