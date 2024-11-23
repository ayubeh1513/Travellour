import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Setup
def setup_database():
    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            username TEXT UNIQUE, 
            digit1 TEXT, digit2 TEXT, digit3 TEXT, digit4 TEXT, 
            digit5 TEXT, digit6 TEXT, digit7 TEXT, digit8 TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Utility function to get full PIN from separate digit entries
def get_pin_from_entries(entries):
    return ''.join(entry.get() for entry in entries)

# Login Function
import os  # Add this import at the top of the file


def login():
    username = username_entry.get()
    pin = get_pin_from_entries(pin_entries)

    if len(pin) != 8 or not pin.isdigit():
        messagebox.showerror("Invalid Input", "Please enter an 8-digit PIN with only numbers.")
        return

    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users 
        WHERE username=? 
        AND digit1=? AND digit2=? AND digit3=? AND digit4=? 
        AND digit5=? AND digit6=? AND digit7=? AND digit8=?
    ''', (username, *pin))
    result = cursor.fetchone()
    conn.close()

    if result:
        root.destroy()
        os.system("python Home.py")
    else:
        messagebox.showerror("Error", "Invalid Username or PIN.")

# Signup Function
def signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("300x400")
    signup_window.configure(bg="#0A6372")

    # Fields
    tk.Label(signup_window, bg="#0A6372", fg="bisque",font=('Times New Roman', 13, "bold"), text="Name").pack(pady=(10, 10))
    name_entry = tk.Entry(signup_window)
    name_entry.pack()

    tk.Label(signup_window, bg="#0A6372", fg="bisque",font=('Times New Roman', 13, "bold"), text="Username").pack(pady=(10, 10))
    username_entry = tk.Entry(signup_window)
    username_entry.pack()

    tk.Label(signup_window, bg="#0A6372", fg="bisque",font=('Times New Roman', 13, "bold"), text="Enter 8-digit PIN (1 digit per box)").pack(pady=(10, 10))
    
    # Frame for PIN entry boxes
    pin_frame_signup = tk.Frame(signup_window)
    pin_frame_signup.pack(pady=(10, 10))
    
    pin_entries_signup = []
    for i in range(8):
        entry = tk.Entry(pin_frame_signup, width=2)
        entry.grid(row=0, column=i, padx=2)
        pin_entries_signup.append(entry)

    def create_user():
        name = name_entry.get()
        username = username_entry.get()
        pin = get_pin_from_entries(pin_entries_signup)
        
        if len(pin) != 8 or not pin.isdigit():
            messagebox.showerror("Invalid Input", "Please enter an 8-digit PIN with only numbers.")
            return
        
        conn = sqlite3.connect('Login.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO users (name, username, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, username, *pin))
            conn.commit()
            messagebox.showinfo("Success", "User Created Successfully!")
            signup_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        
        conn.close()

    tk.Button(signup_window, bg="bisque", fg="black", text="Create", command=create_user).pack(pady=10)

# GUI Setup
root = tk.Tk()
root.title("Login")
root.geometry("300x400")
root.configure(bg="#0A6372")

# Login Form
tk.Label(root, bg="bisque", fg="#0A6372", font=('Times New Roman', 22, "bold", "italic"), text="Travellour").pack(pady=(10, 10))
tk.Label(root,bg="#0A6372", fg="bisque",font=('Times New Roman', 18, "bold"), text="Log into your Account").pack(pady=(10, 10))

tk.Label(root, bg="#0A6372", fg="bisque", font=('Times New Roman', 13), text="Username").pack(pady=(10, 10))
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, bg="#0A6372", fg="bisque", font=('Times New Roman', 13), text="Enter 8-digit PIN (1 digit per box)").pack(pady=(10, 10))

# Frame for PIN entry boxes in Login
pin_frame = tk.Frame(root)
pin_frame.pack(pady=10)

# PIN entry boxes
pin_entries = []
for i in range(8):
    entry = tk.Entry(pin_frame, width=2)
    entry.grid(row=0, column=i, padx=5)
    pin_entries.append(entry)

# Login and Signup buttons
tk.Button(root,bg="bisque", fg="black", text="Login", command=login).pack(pady=(10, 5))
tk.Button(root,bg="bisque", fg="black", text="New User? Signup", command=signup).pack()

# Initialize Database and Run Application
setup_database()
root.mainloop()