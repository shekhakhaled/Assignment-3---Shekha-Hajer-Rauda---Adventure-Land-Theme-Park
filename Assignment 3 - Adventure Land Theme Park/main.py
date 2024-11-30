# main.py: Entry point for running the Ticket Booking System.

from classes import TicketBookingSystem, Ticket  # Import backend classes
from user_gui import UserGUI  # Import the User GUI class
import tkinter as tk

if __name__ == "__main__":
    # Initialize the system
    system = TicketBookingSystem()

    # Add available ticket types
    system.add_ticket(Ticket("Single-Day Pass", 275, "1 Day"))
    system.add_ticket(Ticket("Two-Day Pass", 480, "2 Days", 10))
    system.add_ticket(Ticket("Annual Membership", 1840, "1 Year", 15))
    system.add_ticket(Ticket("Child Ticket", 185, "1 Day"))
    system.add_ticket(Ticket("Group Ticket", 220, "1 Day", 20))
    system.add_ticket(Ticket("VIP Experience Pass", 550, "1 Day"))

    # Launch the GUI
    root = tk.Tk()
    app = UserGUI(root, system)
    root.mainloop()
