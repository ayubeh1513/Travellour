import tkinter as tk
import os

root = tk.Tk()
root.geometry("510x600")
root.title("ScrollBar Example")

# Set background color
root.configure(bg="#0A6372")

# Create a canvas and scrollbar for scrolling
canvas = tk.Canvas(root, bg="#0A6372")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the content
scrollable_frame = tk.Frame(canvas, bg="#0A6372")
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))  # Update scroll region when the frame is resized
)

# Add the scrollable frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add content to the scrollable frame (example: labels and text)
tk.Label(scrollable_frame, text="Travellour", bg="bisque", fg="#0A6372", font=('Times New Roman', 26, "bold", "italic")).pack(pady=10, padx=100)
tk.Label(scrollable_frame, text="Our Tour Packages", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10, padx=100)

def manali_func():
    root.destroy()
    os.system("python Manali01.py")

manali = tk.Button(scrollable_frame, text=" MANALI01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: manali_func(), width=40, height=4)
manali.pack(pady=(50,10), padx=20)

def shimla_func():
    root.destroy()
    os.system("python Manali02.py")

shimla = tk.Button(scrollable_frame, text="MANALI02", bg="bisque", fg="black", font=('Arial', 14), command=lambda: shimla_func(), width=40, height=4)
shimla.pack(pady=10, padx=20)

def vd_func():
    root.destroy()
    os.system("python Amritsar01.py")

vd = tk.Button(scrollable_frame, text="AMRITSAR01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: vd_func(), width=40, height=4)
vd.pack(pady=10, padx=20)

def jaipur_func():
    root.destroy()
    os.system("python Shimla01.py")

jaipur = tk.Button(scrollable_frame, text="SHIMLA01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: jaipur_func(), width=40, height=4)
jaipur.pack(pady=10, padx=20)

def udaipur_func():
    root.destroy()
    os.system("python Rajasthan01.py")

udaipur = tk.Button(scrollable_frame, text="RAJASTHAN01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: udaipur_func(), width=40, height=4)
udaipur.pack(pady=10, padx=20)

def odisha_func():
    root.destroy()
    os.system("python Rajasthan02.py")

odisha = tk.Button(scrollable_frame, text="RAJASTHAN02", bg="bisque", fg="black", font=('Arial', 14), command=lambda: odisha_func(), width=40, height=4)
odisha.pack(pady=10, padx=20)

def jodhpur_func():
    root.destroy()
    os.system("python Odisha01.py")

jodhpur = tk.Button(scrollable_frame, text="ODISHA01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: jodhpur_func(), width=40, height=4)
jodhpur.pack(pady=10, padx=20)

def amritsar_func():
    root.destroy()
    os.system("python Odisha02.py")

amritsar = tk.Button(scrollable_frame, text="ODISHA02", bg="bisque", fg="black", font=('Arial', 14), command=lambda: amritsar_func(), width=40, height=4)
amritsar.pack(pady=10, padx=20)

def dharamshala_func():
    root.destroy()
    os.system("python Odisha03.py")

dharamshala = tk.Button(scrollable_frame, text="ODISHA03", bg="bisque", fg="black", font=('Arial', 14), command=lambda: dharamshala_func(), width=40, height=4)
dharamshala.pack(pady=10, padx=20)

def haridwar_func():
    root.destroy()
    os.system("python SMVD01.py")

haridwar = tk.Button(scrollable_frame, text="SMVD01", bg="bisque", fg="black", font=('Arial', 14), command=lambda: haridwar_func(), width=40, height=4)
haridwar.pack(pady=(10,50), padx=20)

def go_back():
    root.destroy()
    os.system("python Home.py")

back_button = tk.Button(scrollable_frame, text="Home", bg="red", fg="white", font=('Arial', 14), command=go_back)
back_button.pack(pady=20)

# Place canvas and scrollbar without any white space
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure grid weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Main loop
root.mainloop()