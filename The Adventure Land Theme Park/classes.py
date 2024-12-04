# classes.py: Contains backend logic for managing tickets, users, and admin functionality.

class Ticket:
    """
    Ticket class represents a type of ticket with price, validity, and optional discount.
    Aggregation Relationship: TicketBookingSystem and Ticket.
    Tickets are created externally and added to the TicketBookingSystem.
    The lifecycle of Tickets is independent of the system.
    """

    def __init__(self, ticket_type, price, validity, discount=0):
        self.ticket_type = ticket_type
        self.price = price
        self.validity = validity
        self.discount = discount

    def calculate_price(self, quantity):
        """
        Calculates the total price based on the quantity and applies a discount if available.
        """
        total = self.price * quantity
        if self.discount > 0:
            total -= total * (self.discount / 100)
        return total


class User:
    """
    User class represents a user of the system with their purchase history.
    Composition Relationship: TicketBookingSystem and User.
    Users are created and managed by the TicketBookingSystem.
    Their lifecycle is tied to the system.
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.purchase_history = []  # List of purchases made by the user.

    def add_purchase(self, ticket, quantity, total_price):
        """
        Aggregation Relationship: User and Ticket.
        Users can interact with multiple Tickets via purchases, but Tickets exist independently.
        """
        purchase = {
            "ticket_type": ticket.ticket_type,
            "quantity": quantity,
            "total_price": total_price,
        }
        self.purchase_history.append(purchase)

    def view_purchase_history(self):
        """Returns the user's purchase history."""
        return self.purchase_history


class Admin(User):
    """
    Inheritance Relationship: Admin inherits from User.
    Admin is a specialized type of User with additional privileges like managing sales data.
    """

    def __init__(self, username, email):
        super().__init__(username, email)  # Inherit username and email from User.
        self.sales_data = {}  # Tracks sales data for each ticket type.

    def record_sale(self, ticket_type, quantity):
        """Records the sales of tickets by type and quantity."""
        if ticket_type in self.sales_data:
            self.sales_data[ticket_type] += quantity
        else:
            self.sales_data[ticket_type] = quantity


class TicketBookingSystem:
    """
    Composition Relationship: TicketBookingSystem and Admin.
    The Admin is created and owned by the TicketBookingSystem.
    If the TicketBookingSystem is destroyed, the Admin is also destroyed.

    Composition Relationship: TicketBookingSystem and User.
    Users are created and managed by the TicketBookingSystem.
    Their lifecycle is tied to the system.
    """

    def __init__(self):
        self.tickets = []  # List of all available tickets (Aggregation).
        self.users = []  # List to store User instances (Composition).
        self.admin = Admin("admin", "admin@example.com")  # Admin instance (Composition).

    def add_ticket(self, ticket):
        """
        Aggregation Relationship: Tickets are added to the system but managed externally.
        """
        self.tickets.append(ticket)

    def register_user(self, username, email):
        """
        Composition Relationship: Users are created and managed internally by the system.
        """
        for user in self.users:
            if user.username == username:
                print(f"Error: User '{username}' already exists!")
                return
        new_user = User(username, email)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully!")

    def purchase_ticket(self, username, ticket_type, quantity):
        """
        Processes a ticket purchase for a registered user.
        Demonstrates aggregation between User and Ticket.
        """
        # Find the user
        user = next((u for u in self.users if u.username == username), None)
        if not user:
            print(f"Error: User '{username}' not registered!")
            return

        # Find the ticket
        ticket = next((t for t in self.tickets if t.ticket_type == ticket_type), None)
        if not ticket:
            print(f"Error: Ticket type '{ticket_type}' not found!")
            return

        # Process the purchase
        total_price = ticket.calculate_price(quantity)
        user.add_purchase(ticket, quantity, total_price)
        self.admin.record_sale(ticket_type, quantity)  # Admin records sales.
        print(f"Purchase successful for '{username}'! Total price: {total_price} DHS")

    def view_admin_sales_data(self):
        """
        Displays sales data managed by the Admin.
        Demonstrates the composition relationship between the system and Admin.
        """
        print("Admin sales data:")
        for ticket_type, quantity in self.admin.sales_data.items():
            print(f"{ticket_type}: {quantity} tickets sold")
