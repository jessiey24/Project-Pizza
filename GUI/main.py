from tkinter import *
from PIL import ImageTk, Image
from pizza_class import *
from orderPageGUI import OrderPage
from mainPageGUI import *

def main():
    root = Tk()
    app = MainPage(root, 'Project Pizza Main Page', 'pizzaIcon.ico', "600x600", {"bg": "#fae5cf"}) #first reference to main page
#function definition for order page
    def open_order_page(): #definition to open order page
        order_page = OrderPage(Toplevel(), 'Project Pizza Order Page', 'pizzaIcon.ico', "600x600", {"bg": "#fae5cf"} )
# button definition for order page   
    app.orderNowBtn = Button(app.master, text="ORDER NOW!", command = open_order_page,  bg="#d65738", fg="#fae5cf", padx=20, pady=20)
    app.orderNowBtn.grid(column=2, row=4, sticky=SW)

    root.mainloop()
    

if __name__ == "__main__":
    main()














































