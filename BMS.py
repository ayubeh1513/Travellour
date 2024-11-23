from tkinter import *
import os

def home(current_window):
    current_window.destroy()
    os.system("python Home.py")

def bus(current_window):
    current_window.destroy()
    os.system("python Bus.py")

def train(current_window):
    current_window.destroy()
    os.system("python Train.py")

def cab(current_window):
    current_window.destroy()
    os.system("python Cab.py")

def hotel(current_window):
    current_window.destroy()
    os.system("python Hotel.py")

def flight(current_window):
    current_window.destroy()
    os.system("python Flight.py")

top = Tk()
top.geometry('800x550')
top.title('Travellour - Booking Management System')
top.configure(bg="#0A6372")

Label(top, text='Travellour', bg="bisque", fg="#0A6372", font=('Times New Roman', 26, "bold", "italic")).grid(row=0, column=0, columnspan=3, pady=(10, 10))
Label(top, text='Booking System', bg="#0A6372", fg="bisque", font=('Times New Roman', 18, "bold")).grid(row=1, column=0, columnspan=3, padx=100, pady=20)

Button(top, text='Bus Ticket Management', font=('Arial', 14), fg='black', command=lambda: bus(top), width=23, height=2, bg='bisque').grid(row=2, column=0, padx=80, pady=20)
Button(top, text='Train Ticket Management', font=('Arial', 14), fg='black', command=lambda: train(top), width=23, height=2, bg='bisque').grid(row=2, column=1, pady=20)
Button(top, text='Flight Ticket Management', font=('Arial', 14), fg='black', command=lambda: flight(top), width=23, height=2, bg='bisque').grid(row=3, column=0, pady=30)
Button(top, text='Cab Booking Management', font=('Arial', 14), fg='black', command=lambda: cab(top), width=23, height=2, bg='bisque').grid(row=3, column=1, pady=30)
Button(top, text='Hotel Booking Management', font=('Arial', 14), fg='black', command=lambda: hotel(top), width=23, height=2, bg='bisque').grid(row=4, column=0, pady=30)
Button(top, text='Home Page', font=('Arial', 14), fg='white', command=lambda: home(top), width=23, height=2, bg='red').grid(row=4, column=1, pady=30)

top.mainloop()