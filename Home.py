from tkinter import *
import os

def logout(current_window):
    current_window.destroy()
    os.system("python Login.py")

def book(current_window):
    current_window.destroy()
    os.system("python BMS.py")

def about(current_window):
    current_window.destroy()
    os.system("python ASTP.py")

def our(current_window):
    current_window.destroy()
    os.system("python OTP.py")

top = Tk()
top.geometry('800x450')
top.title('Travellour - Home Page')
top.configure(bg="#0A6372")

Label(top, text='Travellour', bg="bisque", fg="#0A6372", font=('Times New Roman', 26, "bold", "italic")).grid(row=0, column=0, columnspan=3, pady=(10, 10))
Label(top, text='Home Page', bg="#0A6372", fg="bisque", font=('Times New Roman', 18, "bold")).grid(row=1, column=0, columnspan=3, padx=100, pady=20)

Button(top, text='Booking System', font=('Arial', 14), fg='black', command=lambda: book(top), width=23, height=2, bg='bisque').grid(row=2, column=0, padx=80, pady=20)
Button(top, text='Our Tour Packages', font=('Arial', 14), fg='black', command=lambda: our(top), width=23, height=2, bg='bisque').grid(row=2, column=1, pady=20)
Button(top, text='About Some Tourist Places', font=('Arial', 14), fg='black', command=lambda: about(top), width=23, height=2, bg='bisque').grid(row=3, column=0, pady=30)
Button(top, text='Log Out', font=('Arial', 14), fg='white', command=lambda: logout(top), width=23, height=2, bg='red').grid(row=3, column=1, pady=30)

top.mainloop()