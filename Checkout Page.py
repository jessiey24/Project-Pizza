import tkinter as tk
from tkinter import messagebox

class CheckoutPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Project Pizza - Checkout")

        # Project Pizza heading
        self.heading_label = tk.Label(master, text="Project Pizza", font=("Helvetica", 16, "bold"))
        self.heading_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="w")

        # Checkout heading
        self.checkout_label = tk.Label(master, text="Check Out", font=("Helvetica", 14))
        self.checkout_label.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="w")

        # Delivery options
        self.delivery_label = tk.Label(master, text="Delivery +$7.99", font=("Helvetica", 12))
        self.delivery_label.grid(row=2, column=0, columnspan=4, pady=5, padx=10, sticky="w")

        self.carryout_label = tk.Label(master, text="Carryout", font=("Helvetica", 12))
        self.carryout_label.grid(row=3, column=0, columnspan=4, pady=5, padx=10, sticky="w")

        # Customer Information
        self.customer_info_label = tk.Label(master, text="Customer Information", font=("Helvetica", 12, "underline"))
        self.customer_info_label.grid(row=4, column=0, columnspan=4, pady=10, padx=10, sticky="w")

        self.first_name_label = tk.Label(master, text="First Name:")
        self.first_name_label.grid(row=5, column=0, pady=5, padx=10, sticky="e")
        self.first_name_entry = tk.Entry(master)
        self.first_name_entry.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        self.last_name_label = tk.Label(master, text="Last Name:")
        self.last_name_label.grid(row=6, column=0, pady=5, padx=10, sticky="e")
        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=7, column=0, pady=5, padx=10, sticky="e")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        self.city_label = tk.Label(master, text="City:")
        self.city_label.grid(row=8, column=0, pady=5, padx=10, sticky="e")
        self.city_entry = tk.Entry(master)
        self.city_entry.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        self.state_label = tk.Label(master, text="State:")
        self.state_label.grid(row=9, column=0, pady=5, padx=10, sticky="e")
        self.state_entry = tk.Entry(master)
        self.state_entry.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        self.zip_label = tk.Label(master, text="Zip Code:")
        self.zip_label.grid(row=10, column=0, pady=5, padx=10, sticky="e")
        self.zip_entry = tk.Entry(master)
        self.zip_entry.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        # Payment Information
        self.payment_info_label = tk.Label(master, text="Payment Information", font=("Helvetica", 12, "underline"))
        self.payment_info_label.grid(row=4, column=2, columnspan=2, pady=10, padx=10, sticky="w")

        self.pay_at_store_var = tk.IntVar()
        self.pay_online_var = tk.IntVar()

        self.pay_at_store_checkbox = tk.Checkbutton(master, text="Pay at Store/Delivery Driver", variable=self.pay_at_store_var)
        self.pay_at_store_checkbox.grid(row=5, column=2, columnspan=2, pady=5, padx=10, sticky="w")

        self.pay_online_checkbox = tk.Checkbutton(master, text="Pay Online", variable=self.pay_online_var, command=self.toggle_payment_fields)
        self.pay_online_checkbox.grid(row=6, column=2, columnspan=2, pady=5, padx=10, sticky="w")

        self.payment_fields_frame = tk.Frame(master)
        self.payment_fields_frame.grid(row=7, column=2, columnspan=2, pady=10, padx=10, sticky="w")

        self.card_name_label = tk.Label(self.payment_fields_frame, text="Cardholder Name:")
        self.card_name_label.grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.card_name_entry = tk.Entry(self.payment_fields_frame)
        self.card_name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        self.card_number_label = tk.Label(self.payment_fields_frame, text="Card Number:")
        self.card_number_label.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        self.card_number_entry = tk.Entry(self.payment_fields_frame)
        self.card_number_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        self.cvv_label = tk.Label(self.payment_fields_frame, text="CVV:")
        self.cvv_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        self.cvv_entry = tk.Entry(self.payment_fields_frame)
        self.cvv_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.expiry_date_label = tk.Label(self.payment_fields_frame, text="Expiration Date:")
        self.expiry_date_label.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        self.expiry_date_entry = tk.Entry(self.payment_fields_frame)
       
