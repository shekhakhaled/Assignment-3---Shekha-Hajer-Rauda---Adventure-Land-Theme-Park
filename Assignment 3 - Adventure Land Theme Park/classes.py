# classes.py: Contains backend logic for managing tickets, users, and admin functionality.

class Ticket:
    # Represents a type of ticket with price, validity, and optional discount.
    def __init__(self, ticket_type, price, validity, discount=0):
        self.ticket_type = ticket_type
        self.price = price
        self.validity = validity
        self.discount = discount

    def calculate_price(self, quantity):
        # Calculates total price based on quantity and applies discount if available.
        total = self.price * quantity
        if self.discount > 0:
            total -= total * (self.discount / 100)
        return total


class User:
    # Represents a user with their purchase history.
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.purchase_history = []  # List of purchases made by the user.

    def add_purchase(self, ticket, quantity, total_price):
        # Adds a purchase to the user's history.
        purchase = {
            "ticket_type": ticket.ticket_type,
            "quantity": quantity,
            "total_price": total_price
        }
        self.purchase_history.append(purchase)

    def view_purchase_history(self):
        # Returns the user's purchase history.
        return self.purchase_history


class Admin(User):
    # Represents an admin, inheriting from the User class.
    def __init__(self, username, email):
        super().__init__(username, email)  # Inherit username and email from User.
        self.sales_data = {}  # Tracks sales data for each ticket type.

    def record_sale(self, ticket_type, quantity):
        # Records ticket sales by type and quantity.
        if ticket_type in self.sales_data:
            self.sales_data[ticket_type] += quantity
        else:
            self.sales_data[ticket_type] = quantity


class TicketBookingSystem:
    # Manages the entire ticket booking system.
    def __init__(self):
        self.tickets = []  # List of all available tickets.
        self.users = {}  # Dictionary to store registered users by username.
        self.admin = Admin("admin", "admin@example.com")  # Default admin account.

    def add_ticket(self, ticket):
        # Adds a new ticket type to the system.
        self.tickets.append(ticket)

    def register_user(self, username, email):
        # Registers a new user in the system.
        if username not in self.users:
            self.users[username] = User(username, email)
        else:
            print("User already exists!")  # Prevent duplicate user registration.

    def purchase_ticket(self, username, ticket_type, quantity):
        # Processes a ticket purchase for a user.
        user = self.users.get(username)
        if user:
            for ticket in self.tickets:
                if ticket.ticket_type == ticket_type:
                    total_price = ticket.calculate_price(quantity)
                    user.add_purchase(ticket, quantity, total_price)
                    self.admin.record_sale(ticket_type, quantity)  # Update sales data.
                    print(f"Purchase successful! Total price: {total_price} DHS")
                    return
            print("Ticket type not found!")  # If the ticket type doesn't exist.
        else:
            print("User not registered!")  # If the user is not registered.
