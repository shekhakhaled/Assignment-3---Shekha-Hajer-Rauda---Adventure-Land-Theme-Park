# classes.py: Contains backend logic for managing tickets, users, and admin functionality.


import pickle
import os


class Ticket:
   def __init__(self, ticket_type, price, validity, discount=0):
       self.ticket_type = ticket_type
       self.price = price
       self.validity = validity
       self.discount = discount


   def calculate_price(self, quantity):
       total = self.price * quantity
       if self.discount > 0:
           total -= total * (self.discount / 100)
       return total




class User:
   def __init__(self, username, email):
       self.username = username
       self.email = email
       self.purchase_history = []  # List of purchases made by the user.


   def add_purchase(self, ticket, quantity, total_price):
       purchase = {
           "ticket_type": ticket.ticket_type,
           "quantity": quantity,
           "total_price": total_price,
       }
       self.purchase_history.append(purchase)


   def view_purchase_history(self):
       return self.purchase_history




class Admin(User):
   def __init__(self, username, email):
       super().__init__(username, email)
       self.sales_data = {}  # Tracks sales data for each ticket type.


   def record_sale(self, ticket_type, quantity):
       if ticket_type in self.sales_data:
           self.sales_data[ticket_type] += quantity
       else:
           self.sales_data[ticket_type] = quantity




class TicketBookingSystem:
   def __init__(self):
       self.tickets = []  # List of all available tickets (Aggregation).
       self.users = []  # List to store User instances (Composition).
       self.admin = Admin("admin", "admin@example.com")  # Admin instance (Composition).
       self._data_dir = "data"
       self._init_storage()


   def _init_storage(self):
       """Initializes storage directory and files."""
       if not os.path.exists(self._data_dir):
           os.makedirs(self._data_dir)


   def _save_to_file(self, filename, data):
       """Helper function to save data to a binary file."""
       filepath = os.path.join(self._data_dir, filename)
       with open(filepath, "wb") as file:
           pickle.dump(data, file)


   def _load_from_file(self, filename):
       """Helper function to load data from a binary file."""
       filepath = os.path.join(self._data_dir, filename)
       if os.path.exists(filepath):
           with open(filepath, "rb") as file:
               return pickle.load(file)
       return None


   def save_all_data(self):
       """Saves all system data to binary files."""
       self._save_to_file("tickets.pkl", self.tickets)
       self._save_to_file("users.pkl", self.users)
       self._save_to_file("admin.pkl", self.admin)


   def load_all_data(self):
       """Loads all system data from binary files."""
       self.tickets = self._load_from_file("tickets.pkl") or []
       self.users = self._load_from_file("users.pkl") or []
       admin_data = self._load_from_file("admin.pkl")
       if admin_data:
           self.admin = admin_data


   def add_ticket(self, ticket):
       self.tickets.append(ticket)
       self.save_all_data()


   def register_user(self, username, email):
       for user in self.users:
           if user.username == username:
               print(f"Error: User '{username}' already exists!")
               return
       new_user = User(username, email)
       self.users.append(new_user)
       self.save_all_data()
       print(f"User '{username}' registered successfully!")


   def purchase_ticket(self, username, ticket_type, quantity):
       user = next((u for u in self.users if u.username == username), None)
       if not user:
           print(f"Error: User '{username}' not registered!")
           return


       ticket = next((t for t in self.tickets if t.ticket_type == ticket_type), None)
       if not ticket:
           print(f"Error: Ticket type '{ticket_type}' not found!")
           return


       total_price = ticket.calculate_price(quantity)
       user.add_purchase(ticket, quantity, total_price)
       self.admin.record_sale(ticket_type, quantity)
       self.save_all_data()
       print(f"Purchase successful for '{username}'! Total price: {total_price} DHS")


   def view_admin_sales_data(self):
       print("Admin sales data:")
       for ticket_type, quantity in self.admin.sales_data.items():
           print(f"{ticket_type}: {quantity} tickets sold")