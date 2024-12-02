# test.py: Tests for the Ticket Booking System.

from classes import Ticket, TicketBookingSystem  # Import backend classes

# Step 1: Initialize the TicketBookingSystem
system = TicketBookingSystem()

# Test 1: Add Tickets
print("----- Test 1: Adding Tickets -----")
ticket1 = Ticket("Single-Day Pass", 275, "1 Day")
ticket2 = Ticket("Two-Day Pass", 480, "2 Days", 10)
ticket3 = Ticket("Annual Membership", 1840, "1 Year", 15)
ticket4 = Ticket("Child Ticket", 185, "1 Day")
ticket5 = Ticket("Group Ticket", 220, "1 Day", 20)
ticket6 = Ticket("VIP Experience Pass", 550, "1 Day")

system.add_ticket(ticket1)
system.add_ticket(ticket2)
system.add_ticket(ticket3)
system.add_ticket(ticket4)
system.add_ticket(ticket5)
system.add_ticket(ticket6)

# Display tickets added to the system
print("Tickets added to the system:")
for ticket in system.tickets:
    print(f"{ticket.ticket_type} - Price: {ticket.price}, Validity: {ticket.validity}, Discount: {ticket.discount}%")

# Test 2: Register Users (Composition with Users)
print("\n----- Test 2: Registering Users -----")
system.register_user("hajer", "hajer@gmail.com")
system.register_user("abdullah", "abdullah@gmail.com")
system.register_user("rauda", "rauda@gmail.com")
system.register_user("shekha", "shekha@gmail.com")
system.register_user("mohammed", "mohammed@gmail.com")
system.register_user("sara", "sara@gmail.com")

# Display registered users
print("Registered users:")
for user in system.users:
    print(f"Username: {user.username}, Email: {user.email}")

# Test 3: Purchase Tickets (Aggregation with Tickets)
print("\n----- Test 3: Purchasing Tickets -----")
system.purchase_ticket("hajer", "Single-Day Pass", 2)
system.purchase_ticket("abdullah", "Two-Day Pass", 1)
system.purchase_ticket("rauda", "Annual Membership", 1)
system.purchase_ticket("shekha", "VIP Experience Pass", 1)
system.purchase_ticket("mohammed", "Group Ticket", 3)
system.purchase_ticket("sara", "Child Ticket", 2)

# Display purchases made by each user
print("\nPurchases made:")
for user in system.users:
    print(f"User: {user.username}")
    for purchase in user.view_purchase_history():
        print(f"  Ticket: {purchase['ticket_type']}, Quantity: {purchase['quantity']}, Total: {purchase['total_price']} DHS")

# Test 4: View Admin Sales Data (Composition with Admin)
print("\n----- Test 4: Admin Sales Data -----")
system.view_admin_sales_data()
