import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("600x600")
root.title("Travellour - Amritsar")

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
tk.Label(scrollable_frame, text="Amritsar", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (4).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Amritsar, located in the northwestern state of Punjab, is a city known for its deep religious significance and historical importance. The Golden Temple, or Harmandir Sahib, is the most iconic landmark, drawing millions of pilgrims and visitors annually. Founded in 1577 by Guru Ram Das, Amritsar became the spiritual center of Sikhism. The city also holds historical significance as the site of the Jallianwala Bagh massacre in 1919, a turning point in India's struggle for independence. Amritsar’s vibrant culture, with its rich culinary traditions, bustling markets, and festivals like Baisakhi, makes it a must-visit destination for those seeking history and spirituality.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Amritsar, founded in 1577 by Guru Ram Das, is the spiritual and cultural center of Sikhism. The city grew around the sacred Harmandir Sahib (Golden Temple), built by Guru Arjan in 1581, which became a symbol of Sikh heritage. During the British colonial era, Amritsar witnessed the tragic Jallianwala Bagh massacre in 1919, where hundreds of unarmed Indians were killed by British forces, marking a pivotal moment in India's fight for independence. Over the centuries, Amritsar has been a hub for Sikh religious and cultural life, playing a key role in both the independence movement and in the global Sikh community's growth.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Amritsar is from October to March, during the winter months, when the weather is cool and pleasant, perfect for exploring the Golden Temple and other attractions. Summers can be hot, making the cooler months ideal for sightseeing and enjoying the city's cultural vibrancy.\n"
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