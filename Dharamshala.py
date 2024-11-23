import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("600x600")
root.title("Travellour - Dharamshala")

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
tk.Label(scrollable_frame, text="Dharamshala", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("top-day-trip-ideas-from-dharamshala-explore-the-hidden-gems.jpg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Dharamshala, nestled in the Kangra Valley of Himachal Pradesh, is a peaceful town known for its scenic beauty and Tibetan influence. It serves as the headquarters of the Tibetan government-in-exile and is home to the Dalai Lama. Surrounded by the majestic Dhauladhar mountain range, Dharamshala offers stunning landscapes, serene monasteries, and a vibrant Buddhist culture. McLeod Ganj, a suburb of Dharamshala, is famous for its Tibetan market, Buddhist temples, and meditation centers. The town also attracts trekkers with nearby trails like Triund. Dharamshala's tranquil atmosphere, coupled with its spiritual significance, makes it a popular destination for travelers seeking peace and spirituality.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Dharamshala, established as a hill station in the 19th century, gained prominence during British rule when it was developed as a military cantonment. The town's significance increased in 1959 when the 14th Dalai Lama, after fleeing Tibet, chose Dharamshala as his home in exile. The Dalai Lama's arrival led to the growth of Tibetan culture and Buddhism in the region, with McLeod Ganj becoming a hub for Tibetan refugees and their traditions. Over time, Dharamshala transformed into a center for spirituality, meditation, and Tibetan culture. The town’s historical association with Tibetan politics and its scenic beauty attract visitors from around the world.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Dharamshala is from March to June and September to November, during the spring and autumn months when the weather is pleasant and ideal for sightseeing, trekking, and exploring monasteries. Winters can be cold, with snowfall, while monsoon rains can disrupt travel plans.\n"
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