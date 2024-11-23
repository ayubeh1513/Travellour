from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
import sqlite3
import random
import string
import os

# Main window setup
top = Tk()
top.geometry('600x350')
top.title('Travellour - Hotel Booking Management')
top.configure(bg="#0A6372")

# Connect to database and update table structure
conn = sqlite3.connect('Hotel.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ticket (
        name TEXT,
        train_no INTEGER,
        ticket_id INTEGER PRIMARY KEY,
        ticket_date TEXT,
        check_date TEXT,
        source TEXT,
        destination TEXT,
        price INTEGER
    )
""")
conn.commit()

# Fetch database contents
cursor.execute('SELECT * FROM ticket')
tickets = cursor.fetchall()

# Store ticket IDs
tickets_id = [i[2] for i in tickets]

Label(top, text='Hotel Booking Management', bg="#0A6372", fg="bisque", font=('Arial', 18, "bold")).grid(row=0, column=0, columnspan=2, padx=80, pady=20)

# Helper function to display messages
def show_message(title, message):
    messagebox.showerror(title, message)

# Booking function
def Book():
    top1 = Tk()
    top1.geometry('400x500')
    top1.title('Book Ticket')
    top1.configure(bg="#0A6372")

    name = StringVar(top1)
    train_no = IntVar(top1)
    ticket_id = IntVar(top1)
    ticket_date = StringVar(top1)
    ticket_date.set(date.today())
    check_date = StringVar(top1)
    check_date.set(date.today())
    source = StringVar(top1)
    destination = StringVar(top1)
    price = IntVar(top1)

    # Unique room number generation
    def generate_room_number():
        conn = sqlite3.connect("Hotel_Ticket.db")
        cursor = conn.cursor()

        # Ensure the table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ticket (
                name TEXT,
                train_no INTEGER,
                ticket_id INTEGER PRIMARY KEY,
                ticket_date TEXT,
                check_date TEXT,
                source TEXT,
                destination TEXT,
                price INTEGER
            )
        """)

        cursor.execute("SELECT ticket_id FROM ticket")
        booked_rooms = [row[0] for row in cursor.fetchall()]
        conn.close()

        all_rooms = set(range(1, 101))  # Room numbers 1 to 100
        available_rooms = list(all_rooms - set(booked_rooms))

        if available_rooms:
            return random.choice(available_rooms)
        else:
            return None

    def BookNow():
        if len(name.get()) < 5 or len(source.get()) < 3 or len(destination.get()) < 3 or price.get() <= 0:
            show_message('Error', 'Enter valid details')
            return
        try:
            # Generate a room number (ticket_id) before inserting the record
            room_number = generate_room_number()  # Get a unique room number
            if room_number is None:
                show_message('Error', 'No rooms available')
                return

            conn = sqlite3.connect("Hotel_Ticket.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ticket (
                    name TEXT,
                    train_no INTEGER,
                    ticket_id INTEGER PRIMARY KEY,
                    ticket_date TEXT,
                    check_date TEXT,
                    source TEXT,
                    destination TEXT,
                    price INTEGER
                )
            """)
            cursor.execute("""
                INSERT INTO ticket (name, train_no, ticket_id, ticket_date, check_date, source, destination, price)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name.get(), train_no.get(), room_number, ticket_date.get(), check_date.get(), source.get(),
                  destination.get(),
                  price.get()))
            conn.commit()
            show_message('Successful', f'Your booking is successful, your room number is {room_number}')
            top1.destroy()
        except sqlite3.Error as e:
            show_message('Error', str(e))
        finally:
            conn.close()

    Label(top1, text='Enter details',bg="#0A6372",fg="bisque", font=('Arial', 14, "bold")).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    Label(top1, text='Name',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=name).grid(row=1, column=1)

    Label(top1, text='Phone Number', bg="#0A6372", fg="bisque", font=('Arial', 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=train_no).grid(row=2, column=1)

    Label(top1, text='Room Number',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=ticket_id, state='disabled').grid(row=3, column=1)

    Label(top1, text='Start Date',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=4, column=0, padx=10, sticky='w', pady=10)
    DateEntry(top1, selectmode='day', textvariable=ticket_date).grid(row=4, column=1)

    Label(top1, text='End Date', bg="#0A6372", fg="bisque", font=('Arial', 12, "bold")).grid(row=5, column=0, padx=10, sticky='w', pady=10)
    DateEntry(top1, selectmode='day', textvariable=check_date).grid(row=5, column=1)

    Label(top1, text='Home City',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=6, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=source).grid(row=6, column=1)

    Label(top1, text='Payment By',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=7, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=destination).grid(row=7, column=1)

    Label(top1, text='Price (INR)',bg="#0A6372",fg="bisque", font=('Arial', 12, "bold")).grid(row=8, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=price).grid(row=8, column=1)

    Button(top1, text='Confirm', bg='bisque', fg='black', font=('Arial', 17, "bold"), width=9, command=BookNow).grid(row=9, column=1, pady=10)

# Function to display ticket history
def ViewHistory():
    top2 = Tk()
    top2.geometry('1500x300')
    top2.title('View Ticket Booking History')
    top2.configure(bg="#0A6372")

    headers = ['Customer Name', 'Phone Number', 'Room Number', 'Start Date','End Date', 'Home City', 'Payment By', 'Price (INR)']
    for idx, header in enumerate(headers):
        Label(top2, text=header,bg="bisque",fg="black", font=('Arial', 12, "bold"), borderwidth=1, relief="solid", width=15).grid(row=1, column=idx, pady=20)

    conn = sqlite3.connect('Hotel_Ticket.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()

    for i, ticket in enumerate(tickets):
        for j, info in enumerate(ticket):
            Label(top2, text=info, borderwidth=1, relief="solid", width=20).grid(row=i+2, column=j, pady = 10)

    top2.mainloop()
    conn.close()

def home(current_window):
    current_window.destroy()
    os.system("python Home.py")

# Function to delete a ticket
def DeleteBooking():
    top3 = Tk()
    top3.geometry('1550x300')
    top3.title('Delete Ticket Booking')
    top3.configure(bg="#0A6372")

    headers = ['Customer Name', 'Phone Number', 'Room Number', 'Start Date','End Date', 'Home City', 'Payment By', 'Price (INR)']
    for idx, header in enumerate(headers):
        Label(top3, text=header,bg="bisque",fg="black", font=('Arial', 12, "bold"), borderwidth=1, relief="solid", width=15).grid(row=0, column=idx, pady=20)

    def delete_rows(ticket_id):
        try:
            conn = sqlite3.connect("Hotel_Ticket.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ticket WHERE ticket_id = ?", (ticket_id,))
            conn.commit()
            show_message('Success', 'Customer Checked Out Successfully')
            conn.close()
            top3.destroy()  # Refresh the window to show updated list
            DeleteBooking()
        except sqlite3.Error as e:
            show_message('Sqlite error', str(e))

    conn = sqlite3.connect('Hotel_Ticket.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()

    for i, ticket in enumerate(tickets):
        for j, info in enumerate(ticket):
            Label(top3, text=info, borderwidth=1, relief="solid", width=20).grid(row=i+1, column=j, pady=10)
        Button(top3, text='Check Out', bg="bisque", fg="black", command=lambda current_id=ticket[2]: delete_rows(current_id)).grid(row=i+1, column=len(ticket), padx=30)

    top3.mainloop()
    conn.close()

def open_home_page():
    top.destroy()  # Close the current window
    os.system("python Home.py")  # Execute the Home_Page.py file


# Define main window buttons
Button(top, text='Check IN', font=('Arial', 14), fg='black', command=Book, width=12, height=2, bg='bisque').grid(row=1, column=0, padx=80, pady=20)
Button(top, text='See Guest List', font=('Arial', 14), fg='black', command=ViewHistory, width=12, height=2, bg='bisque').grid(row=1, column=1, pady=20)
Button(top, text='Check Out', font=('Arial', 14), fg='black', command=DeleteBooking, width=12, height=2, bg='bisque').grid(row=2, column=0, pady=30)
Button(top, text='Home Page', font=('Arial', 14), fg='white', command=lambda: open_home_page(), width=12, height=2, bg='red').grid(row=2, column=1, pady=30)

# Main loop
top.mainloop()