import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("600x600")
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
tk.Label(scrollable_frame, text="Travellour", bg="bisque", fg="#0A6372", font=('Times New Roman', 26, "bold", "italic")).pack(pady=10)
tk.Label(scrollable_frame, text="Manali", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("hq720.jpg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "If the state Himachal Pradesh is considered to be the Queen of Hills, Manali can be said to be her Tiara. Located at a height of 6260 feet above the sea level, Manali is the mesmerizing Hill Station surrounded with other alluring hills and woody forests. The most popular hill station of India, Manali captivates the hearts of people all around the world. Blessed with the breathtaking beauty and awestruck aura, Manali is the hill station with heavenly beauty. The spellbinding landscapes, the hilly area, snow covered peaks, and the woody forests add to the charm of this mesmerizing hill station. Manali is not just a place for all travelers, but Manali provides the food to the adventurous souls who seek the adventures places. With plenty of adventurous activities that Manali offers, Manali is the only hill station which is full of hustle-bustle at almost every part of the year. With some major attractions of Manali and the activities that it offer, Manali is considered to be the most loved Hill Station of India and it attracts uncountable number of travelers every year from all over the world.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "The magnificent hill station of India, Manali retains a quiet interesting history. More than the history it would be called as a myth or a belief of the legends of this alluring beauty. As per the say of the legends and the natives, Manali has the home to the Lawgiver Many and while he was searching for his safe house, Manali provided him with the safe shelter and environment. As the days were going, once he found a ting fish in the bathing water and the fish asked him to look after her with devotion and in return, one day she would provide him with a great service. As per the say of the fish, Vaivasvatatava looked after the fish until the fish grew extremely huge and she was departed to the sea. Before the departure, she warned Manu about the deluge where the entire world will be submerged under the water and he would build a sea-worthy ark. As the world was submerged under the water because of the flood, the Seven Sages and the Vaivasvata were provided the safety by the Matsya, the fish who is considered to be the first avatar of Lord Vishnu.As the water level subsided the seventh Manu’s ark came for the rest on hillside and then, this place got its name Manali after him. With the steady process of the drying of the water, the place here came out as a breath taking beauty and the life began again at Manali.The high mountains here were covered with white yet silent snow and the deep boulder strewn gorges, the forests started growing thick with woody trees and the weather with breezy winds with the songs of the birds made this place a legendary cradle for human life and now is the prominent tourist destination of India."
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "It lives in freezing cold in the winters and enjoys the moderately cool summers. One can explore this enthralling town anytime throughout the year except for monsoon months. The interval of March to June and the period of October to February are simply great for exploration."
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