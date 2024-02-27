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



















































'''
mainPage = Tk()


#text configurations
font_tuple = ("Times New Roman", 50, "normal") #tuple for text conifgurations for company name
font_tuple2 = ("Times New Roman", 20, "italic") #tuple for text conifgurations for motto


mainPage.title('Project Pizza Main Page') # main page title
mainPage.iconbitmap('pizzaIcon.ico') # icon for window header
mainPage.geometry("600x600") #size of window
mainPage.configure(bg= "#fae5cf") #background color  

companyTitle = Label(mainPage, font = font_tuple, text = "PROJECT PIZZA",fg= "#d65738", bg= "#fae5cf", anchor = N) #Company title text configuration
companyTitle.grid(column= 2, row=3) #company title implementation

blank_label =Label(mainPage, text = "               ", bg = "#fae5cf") #this label was created to help with formatting in tkinter's grid system
blank_label.grid(row= 1, column =1) #formatting for the main page
blank_label.grid(row= 1, column =2) #formatting for the main page
blank_label.grid(row= 2, column =1)#formatting for the main page


# Load and resize the images from the configurations file
#image configuration

pizzaIcon = (Image.open('mainPagePizzaIcon.ico')) #open icon to be used in main page
resized_pizzaIcon = pizzaIcon.resize((80,80)) #resizing of icon
final_pizzaIcon = ImageTk.PhotoImage(resized_pizzaIcon) # icon that is to be placed into the application
mainPgIcon = Label(mainPage, image = final_pizzaIcon, bg = "#fae5cf") #icon definition
mainPgIcon.grid(row= 3, column = 1) #icon implementation

companyMotto =  Label(mainPage, font = font_tuple2, text = "WHERE YOUR PIZZA IS OUR PASSION", fg= "#d65738", bg= "#fae5cf", anchor = S) #motto text configuration
companyMotto.grid(row = 2, column = 2) #motto implementation

    
    
pizzaImage= (Image.open('pizzaImage.jpeg'))  #open image to be used in main page
resized_pizzaImage = pizzaImage.resize((600,300)) #resizing image
final_pizzaImage = ImageTk.PhotoImage(resized_pizzaImage) #image to be placed in definition
mainPgImage = Label(mainPage, image = final_pizzaImage, bg = "#fae5cf") #image definition
mainPgImage.grid(column= 1, row= 4, columnspan=3,rowspan=2, sticky = NSEW) #image implementation


orderNowBtn = Button(mainPage, text= "ORDER NOW!", command =open_order_page, bg= "#d65738", fg= "#fae5cf", padx = 20, pady = 20) #order now button definition
orderNowBtn.grid(column = 2, row = 4, sticky = SW)


mainPage.mainloop()
'''