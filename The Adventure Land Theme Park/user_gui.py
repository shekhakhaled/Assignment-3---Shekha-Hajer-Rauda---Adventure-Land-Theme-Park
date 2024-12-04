# user_gui.py: Contains the GUI for user registration, ticket purchasing, and history viewing.

import tkinter as tk
from tkinter import ttk, messagebox
from classes import Ticket, TicketBookingSystem  # Import backend classes.

class UserGUI:
    """
    Aggregation Relationship: UserGUI and TicketBookingSystem.
    The GUI interacts with the TicketBookingSystem instance, but the system's lifecycle is independent.
    """

    def __init__(self, root, system):
        self.root = root  # Tkinter root window.
        self.system = system  # Aggregation: TicketBookingSystem instance passed to the GUI.
        self.root.title("Adventure Land - User Interface")
        self.root.geometry("600x500")

        # Create GUI components.
        self.create_gui()

    def create_gui(self):
        """Creates the tabbed interface for the GUI."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        self.create_user_tab()       # Tab for user registration.
        self.create_purchase_tab()   # Tab for ticket purchasing.
        self.create_history_tab()    # Tab for viewing purchase history.

    def create_user_tab(self):
        """Tab for registering users."""
        user_tab = ttk.Frame(self.notebook)
        self.notebook.add(user_tab, text="User Registration")

        ttk.Label(user_tab, text="Register User", font=("Arial", 14)).grid(row=0, column=0, pady=10)
        ttk.Label(user_tab, text="Username:").grid(row=1, column=0, pady=5)
        ttk.Label(user_tab, text="Email:").grid(row=2, column=0, pady=5)

        self.username_entry = ttk.Entry(user_tab, width=30)
        self.username_entry.grid(row=1, column=1, pady=5)
        self.email_entry = ttk.Entry(user_tab, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)

        ttk.Button(user_tab, text="Register", command=self.register_user).grid(row=3, column=1, pady=10)

    def create_purchase_tab(self):
        """Tab for purchasing tickets."""
        purchase_tab = ttk.Frame(self.notebook)
        self.notebook.add(purchase_tab, text="Purchase Tickets")

        ttk.Label(purchase_tab, text="Purchase Tickets", font=("Arial", 14)).grid(row=0, column=0, pady=10)
        ttk.Label(purchase_tab, text="Username:").grid(row=1, column=0, pady=5)
        ttk.Label(purchase_tab, text="Ticket Type:").grid(row=2, column=0, pady=5)
        ttk.Label(purchase_tab, text="Quantity:").grid(row=3, column=0, pady=5)
        ttk.Label(purchase_tab, text="Payment Method:").grid(row=4, column=0, pady=5)

        self.purchase_username_entry = ttk.Entry(purchase_tab, width=30)
        self.purchase_username_entry.grid(row=1, column=1, pady=5)
        self.ticket_type_combobox = ttk.Combobox(
            purchase_tab, values=[t.ticket_type for t in self.system.tickets], width=28
        )
        self.ticket_type_combobox.grid(row=2, column=1, pady=5)
        self.quantity_entry = ttk.Entry(purchase_tab, width=30)
        self.quantity_entry.grid(row=3, column=1, pady=5)

        self.payment_method_combobox = ttk.Combobox(
            purchase_tab, values=["Credit Card", "Digital Wallet"], width=28
        )
        self.payment_method_combobox.grid(row=4, column=1, pady=5)

        ttk.Button(purchase_tab, text="Purchase", command=self.purchase_ticket).grid(row=5, column=1, pady=10)

    def create_history_tab(self):
        """Tab for viewing purchase history."""
        history_tab = ttk.Frame(self.notebook)
        self.notebook.add(history_tab, text="Purchase History")

        ttk.Label(history_tab, text="View All Purchase Histories", font=("Arial", 14)).grid(row=0, column=0, pady=10)

        ttk.Button(history_tab, text="View All Histories", command=self.view_all_purchase_histories).grid(row=1, column=0, pady=10)

        self.history_display = tk.Text(history_tab, width=70, height=20)
        self.history_display.grid(row=2, column=0, columnspan=2, pady=10)

    def register_user(self):
        """Handles user registration."""
        username = self.username_entry.get()
        email = self.email_entry.get()
        if username and email:
            self.system.register_user(username, email)  # Register user in the system (Composition).
            messagebox.showinfo("Success", f"User '{username}' registered successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def purchase_ticket(self):
        """Handles ticket purchasing."""
        username = self.purchase_username_entry.get()
        ticket_type = self.ticket_type_combobox.get()
        quantity = self.quantity_entry.get()
        payment_method = self.payment_method_combobox.get()

        if username and ticket_type and quantity.isdigit() and payment_method:
            quantity = int(quantity)
            self.system.purchase_ticket(username, ticket_type, quantity)  # Purchase ticket in the system.
            messagebox.showinfo(
                "Payment Successful",
                f"Payment made using {payment_method}. Ticket(s) purchased successfully!"
            )
        else:
            messagebox.showerror("Error", "All fields are required!")

    def view_all_purchase_histories(self):
        """Displays purchase history for all users."""
        self.history_display.delete(1.0, tk.END)
        for user in self.system.users:
            self.history_display.insert(tk.END, f"User: {user.username}\n")
            for record in user.view_purchase_history():
                self.history_display.insert(
                    tk.END,
                    f"  Ticket: {record['ticket_type']}, Quantity: {record['quantity']}, Total: {record['total_price']} DHS\n"
                )
            self.history_display.insert(tk.END, "\n")
