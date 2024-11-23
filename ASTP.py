import tkinter as tk
import os

root = tk.Tk()
root.geometry("550x600")
root.title("Travellour - About Some Tourist Places")

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
tk.Label(scrollable_frame, text="About Some Tourist Places", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10, padx=100)

def manali_func():
    root.destroy()
    os.system("python Manali.py")

manali = tk.Button(scrollable_frame, text=" Manali", bg="bisque", fg="black", font=('Arial', 14), command=lambda: manali_func(), width=40, height=4)
manali.pack(pady=(50,10), padx=20)

def shimla_func():
    root.destroy()
    os.system("python Shimla.py")

shimla = tk.Button(scrollable_frame, text="Shimla", bg="bisque", fg="black", font=('Arial', 14), command=lambda: shimla_func(), width=40, height=4)
shimla.pack(pady=10, padx=20)

def vd_func():
    root.destroy()
    os.system("python VD.py")

vd = tk.Button(scrollable_frame, text="Shri Mata Vaishno Devi", bg="bisque", fg="black", font=('Arial', 14), command=lambda: vd_func(), width=40, height=4)
vd.pack(pady=10, padx=20)

def jaipur_func():
    root.destroy()
    os.system("python Jaipur.py")

jaipur = tk.Button(scrollable_frame, text="Jaipur", bg="bisque", fg="black", font=('Arial', 14), command=lambda: jaipur_func(), width=40, height=4)
jaipur.pack(pady=10, padx=20)

def udaipur_func():
    root.destroy()
    os.system("python Udaipur.py")

udaipur = tk.Button(scrollable_frame, text="Udaipur", bg="bisque", fg="black", font=('Arial', 14), command=lambda: udaipur_func(), width=40, height=4)
udaipur.pack(pady=10, padx=20)

def odisha_func():
    root.destroy()
    os.system("python Odisha.py")

odisha = tk.Button(scrollable_frame, text="Odisha", bg="bisque", fg="black", font=('Arial', 14), command=lambda: odisha_func(), width=40, height=4)
odisha.pack(pady=10, padx=20)

def jodhpur_func():
    root.destroy()
    os.system("python Jodhpur.py")

jodhpur = tk.Button(scrollable_frame, text="Jodhpur", bg="bisque", fg="black", font=('Arial', 14), command=lambda: jodhpur_func(), width=40, height=4)
jodhpur.pack(pady=10, padx=20)

def amritsar_func():
    root.destroy()
    os.system("python Amritsar.py")

amritsar = tk.Button(scrollable_frame, text="Amritsar", bg="bisque", fg="black", font=('Arial', 14), command=lambda: amritsar_func(), width=40, height=4)
amritsar.pack(pady=10, padx=20)

def dharamshala_func():
    root.destroy()
    os.system("python Dharamshala.py")

dharamshala = tk.Button(scrollable_frame, text="Dharamshala", bg="bisque", fg="black", font=('Arial', 14), command=lambda: dharamshala_func(), width=40, height=4)
dharamshala.pack(pady=10, padx=20)

def haridwar_func():
    root.destroy()
    os.system("python Haridwar.py")

haridwar = tk.Button(scrollable_frame, text="Haridwar", bg="bisque", fg="black", font=('Arial', 14), command=lambda: haridwar_func(), width=40, height=4)
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