# test.py: Tests for the Ticket Booking System.


from classes import Ticket, TicketBookingSystem  # Import backend classes


# Step 1: Initialize the TicketBookingSystem
system = TicketBookingSystem()


# Step 2: Load saved data (if any)
system.load_all_data()


# Test 1: Add Tickets
print("----- Test 1: Adding Tickets -----")
if not system.tickets:  # Only add tickets if not already present
   system.add_ticket(Ticket("Single-Day Pass", 275, "1 Day"))
   system.add_ticket(Ticket("Two-Day Pass", 480, "2 Days", 10))
   system.add_ticket(Ticket("Annual Membership", 1840, "1 Year", 15))
   system.add_ticket(Ticket("Child Ticket", 185, "1 Day"))
   system.add_ticket(Ticket("Group Ticket", 220, "1 Day", 20))
   system.add_ticket(Ticket("VIP Experience Pass", 550, "1 Day"))
   print("Default tickets added.")


# Display tickets added to the system
print("Tickets in the system:")
for ticket in system.tickets:
   print(f"{ticket.ticket_type} - Price: {ticket.price}, Validity: {ticket.validity}, Discount: {ticket.discount}%")


# Test 2: Register Users
print("\n----- Test 2: Registering Users -----")
if not system.users:  # Only add users if not already present
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


# Test 3: Purchase Tickets
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


# Test 4: View Admin Sales Data
print("\n----- Test 4: Admin Sales Data -----")
system.view_admin_sales_data()


# Step 3: Save data at the end of the test
system.save_all_data()


