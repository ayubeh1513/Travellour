import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("600x600")
root.title("Travellour - Jaipur")

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
tk.Label(scrollable_frame, text="Jaipur", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("East_facade_Hawa_Mahal_Jaipur_from_ground_level_(July_2022)_-_img_01.jpg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Jaipur, the capital of Rajasthan, is famously known as the 'Pink City' for its distinct terracotta-colored buildings and rich cultural heritage. Founded in 1727 by Maharaja Sawai Jai Singh II, Jaipur is a harmonious blend of history, architecture, and tradition. Iconic landmarks like the Hawa Mahal, Amer Fort, and City Palace showcase its royal legacy. The bustling bazaars, such as Johari Bazaar, offer vibrant textiles, jewelry, and handicrafts. Jaipur is also known for its cultural festivals and traditional cuisine, including dal baati churma. With its blend of ancient charm and modern amenities, Jaipur is a top destination for travelers worldwide.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Jaipur, founded in 1727 by Maharaja Sawai Jai Singh II, is India's first planned city. Designed by architect Vidyadhar Bhattacharya, it follows Vastu Shastra principles, ensuring harmony and prosperity. Initially built to accommodate the growing population and facilitate trade, Jaipur became the capital of the princely state of Amber. In 1876, during Prince Albert's visit, the city was painted pink to symbolize hospitality, earning its nickname, 'Pink City.' Jaipur's historical landmarks, like Amer Fort, Jantar Mantar, and City Palace, reflect its royal legacy. Its strategic location and vibrant culture made Jaipur a significant center for politics, trade, and art over centuries.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Jaipur is from October to March, during the winter season, when the weather is cool and ideal for exploring its forts, palaces, and vibrant markets. This period also features cultural festivals like Jaipur Literature Festival and Kite Festival, enhancing the city’s charm for travelers.\n"
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