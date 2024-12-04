# main.py: Entry point for running the Ticket Booking System.

from classes import TicketBookingSystem, Ticket  # Import backend classes
from user_gui import UserGUI  # Import the User GUI class
import tkinter as tk

if __name__ == "__main__":
    """
    Composition Relationship: TicketBookingSystem and Admin.
    The Admin instance is created and owned by the TicketBookingSystem.

    Aggregation Relationship: TicketBookingSystem and Tickets.
    Tickets are added externally but managed within the system.
    """

    # Step 1: Initialize the TicketBookingSystem
    system = TicketBookingSystem()

    # Step 2: Add available ticket types (Aggregation with Tickets)
    system.add_ticket(Ticket("Single-Day Pass", 275, "1 Day"))
    system.add_ticket(Ticket("Two-Day Pass", 480, "2 Days", 10))
    system.add_ticket(Ticket("Annual Membership", 1840, "1 Year", 15))
    system.add_ticket(Ticket("Child Ticket", 185, "1 Day"))
    system.add_ticket(Ticket("Group Ticket", 220, "1 Day", 20))
    system.add_ticket(Ticket("VIP Experience Pass", 550, "1 Day"))

    # Step 3: Launch the User GUI (Aggregation with UserGUI)
    root = tk.Tk()
    app = UserGUI(root, system)
    root.mainloop()

