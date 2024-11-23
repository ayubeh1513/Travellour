import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("600x600")
root.title("Travellour - Haridwar")

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
tk.Label(scrollable_frame, text="Travellour", bg="bisque", fg="#0A6372", font=('Times New Roman', 26, "bold", "italic")).pack(pady=10)
tk.Label(scrollable_frame, text="Haridwar", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("Haridwar_Ganga_6.JPG")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Haridwar, one of the seven holiest cities in India, is located in Uttarakhand, where the Ganges River enters the plains. Revered for its spiritual significance, it is believed that taking a dip in the Ganges at Haridwar washes away sins and ensures salvation. The city is home to several sacred temples, including Mansa Devi and Chandi Devi, which attract pilgrims throughout the year. The Ganga Aarti, performed at Har Ki Pauri, is a mesmerizing ritual that draws thousands of devotees every evening. Known for its spiritual ambiance, Haridwar is also a hub for yoga, meditation, and other religious practices.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Haridwar, one of the ancient pilgrimage cities of India, has a history that spans thousands of years. Its name is derived from 'Hari' (God) and 'Dwar' (Gateway), signifying it as the gateway to the gods. Historically, it is mentioned in ancient texts like the Vedas and Puranas, establishing its sacred significance. Haridwar was a prominent site during the Kumbh Mela, a mass Hindu pilgrimage held every 12 years. It has witnessed various rulers, including the Mauryas and Guptas, contributing to its cultural and spiritual prominence. Over the centuries, Haridwar has remained a major hub for Hindu rituals, pilgrimage, and spiritual practices.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Haridwar is from October to March, during the cooler months, when the weather is pleasant for sightseeing and participating in religious rituals. The summer months can be quite hot, while the monsoon season brings heavy rainfall, potentially disrupting travel plans.\n"
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

def go_back():
    root.destroy()
    os.system("python ASTP.py")

back_button = tk.Button(scrollable_frame, text="Back", bg="red", fg="white", font=('Arial', 14), command=go_back)
back_button.pack(pady=20)

# Place canvas and scrollbar without any white space
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure grid weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Main loop
root.mainloop()