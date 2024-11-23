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
tk.Label(scrollable_frame, text="Shri Mata Vaishno Devi", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (1).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Shri Mata Vaishno Devi, nestled in the Trikuta Mountains of Jammu and Kashmir, is one of India’s most revered pilgrimage sites. Dedicated to the Hindu goddess Vaishno Devi, the shrine attracts millions of devotees annually. The journey to the holy cave involves a 13.5 km trek from Katra, passing through scenic trails and spiritual landmarks like Ardhkuwari and Bhawan. The shrine houses the goddess’s manifestations in the form of three sacred pindis, symbolizing her divine energies. Known for fulfilling wishes, the pilgrimage is a blend of devotion and adventure. The serene ambiance and spiritual significance make it a must-visit destination.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "The history of Shri Mata Vaishno Devi dates back to ancient times, rooted in Hindu mythology. It is believed that Mata Vaishno Devi, an incarnation of Goddess Durga, took refuge in the Trikuta Mountains to escape Bhairavnath, a demon. Guided by Lord Hanuman, she meditated in the cave before slaying Bhairavnath, who sought her forgiveness. His temple, located near the shrine, symbolizes redemption. The sacred site has been a center of devotion for centuries, with references in texts like the Mahabharata. Rediscovered by a devotee named Pandit Sridhar centuries ago, the shrine continues to attract millions, fulfilling their spiritual aspirations.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Shri Mata Vaishno Devi is during March to October, when the weather is pleasant and ideal for the trek. Navratri, a peak season, offers a deeply spiritual experience. Winters, from November to February, attract devotees seeking a serene pilgrimage amidst snowfall and fewer crowds.\n"
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