#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

class ProjectPizzaUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Project Pizza Ordering System")
        self.create_ordering_page()

    def create_ordering_page(self):
        # Project Pizza heading
        self.heading_label = tk.Label(self.master, text="Project Pizza", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        # Create Your Own heading
        self.create_your_own_label = tk.Label(self.master, text="Create Your Own", font=("Helvetica", 14))
        self.create_your_own_label.pack(pady=10)

        # Size options
        self.size_label = tk.Label(self.master, text="Size", font=("Helvetica", 12, "bold"))
        self.size_label.pack()

        self.size_options = [("Small - $7.99", 7.99), ("Medium - $10.99", 10.99), ("Large - $14.99", 14.99)]
        self.size_var = tk.StringVar()
        self.size_var.set(self.size_options[0][0])

        for size_text, _ in self.size_options:
            tk.Radiobutton(self.master, text=size_text, variable=self.size_var, value=size_text).pack()

        # Crust options
        self.crust_label = tk.Label(self.master, text="Crust", font=("Helvetica", 12, "bold"))
        self.crust_label.pack()

        self.crust_options = ["Hand Tossed", "Thin N Crispy", "Stuffed Crust - ADD $3"]
        self.crust_var = tk.StringVar()
        self.crust_var.set(self.crust_options[0])

        for crust_text in self.crust_options:
            tk.Radiobutton(self.master, text=crust_text, variable=self.crust_var, value=crust_text).pack()

        # Toppings options
        self.toppings_label = tk.Label(self.master, text="Toppings", font=("Helvetica", 12, "bold"))
        self.toppings_label.pack()

        self.toppings_options = ["Pepperoni", "Sausage", "Ham", "Onion", "Mushroom", "Green Bell Pepper", "Black", "Jalapeno", "Banana Pepper"]
        self.selected_toppings = tk.Listbox(self.master, selectmode=tk.MULTIPLE, height=len(self.toppings_options))

        for topping_text in self.toppings_options:
            self.selected_toppings.insert(tk.END, topping_text)

        self.selected_toppings.pack()

        # Add to Cart button
        self.add_to_cart_button = tk.Button(self.master, text="Add to Cart", command=self.show_cart)
        self.add_to_cart_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def show_cart(self):
        # Get selected options
        selected_size = self.size_var.get()
        selected_crust = self.crust_var.get()
        selected_toppings = [self.toppings_options[i] for i in self.selected_toppings.curselection()]

        # Calculate total price based on selections
        total_price = 0
        for size_text, price in self.size_options:
            if size_text == selected_size:
                total_price += price
                break

        if "Stuffed Crust - ADD $3" in selected_crust:
            total_price += 3

        total_price += 0.25 * len(selected_toppings)

        # Display Cart
        cart_text = f"Size: {selected_size}\nCrust: {selected_crust}\nToppings: {', '.join(selected_toppings)}\nTotal Price: ${total_price:.2f}"

        self.master.destroy()  # Close the current window

        cart_window = tk.Tk()
        cart_window.title("Cart")

        cart_label = tk.Label(cart_window, text="Cart", font=("Helvetica", 16, "bold"))
        cart_label.pack(pady=10)

        cart_content_label = tk.Label(cart_window, text=cart_text, font=("Helvetica", 12))
        cart_content_label.pack(pady=10)

        # Continue Ordering button
        continue_ordering_button = tk.Button(cart_window, text="Continue Ordering", command=self.create_ordering_page)
        continue_ordering_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Check Out button
        check_out_button = tk.Button(cart_window, text="Check Out", command=self.check_out)
        check_out_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def check_out(self):
        # Placeholder for checkout action
        messagebox.showinfo("Checkout", "Redirecting to Checkout Page")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectPizzaUI(root)
    root.mainloop()

