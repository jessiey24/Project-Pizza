from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from tkinter import messagebox



class DeliveryPage(ProjectPizza):
    def __init__(self, master, title, iconbitmap, geometry, configure):
        super().__init__(master, title, iconbitmap, geometry, configure)
        self.create_widgets()
    def create_widgets(self):
        pass