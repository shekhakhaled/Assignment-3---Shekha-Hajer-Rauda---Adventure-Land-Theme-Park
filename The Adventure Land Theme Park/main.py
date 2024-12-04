# main.py: Entry point for running the Ticket Booking System.


from classes import TicketBookingSystem, Ticket  # Import backend classes
from user_gui import UserGUI  # Import the User GUI class
import tkinter as tk


if __name__ == "__main__":
   # Step 1: Initialize the TicketBookingSystem
   system = TicketBookingSystem()


   # Step 2: Load saved data (if any)
   system.load_all_data()


   # Step 3: Check if tickets exist; if not, add default tickets
   if not system.tickets:
       system.add_ticket(Ticket("Single-Day Pass", 275, "1 Day"))
       system.add_ticket(Ticket("Two-Day Pass", 480, "2 Days", 10))
       system.add_ticket(Ticket("Annual Membership", 1840, "1 Year", 15))
       system.add_ticket(Ticket("Child Ticket", 185, "1 Day"))
       system.add_ticket(Ticket("Group Ticket", 220, "1 Day", 20))
       system.add_ticket(Ticket("VIP Experience Pass", 550, "1 Day"))
       print("Default tickets added to the system.")


   # Step 4: Launch the User GUI (Aggregation with UserGUI)
   root = tk.Tk()
   app = UserGUI(root, system)
   root.mainloop()


   # Step 5: Save data when the application closes
   system.save_all_data()


