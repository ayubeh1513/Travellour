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
tk.Label(scrollable_frame, text="Odisha", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (3).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Odisha, located on the eastern coast of India, is a state known for its rich cultural heritage, stunning temples, and diverse landscapes. It is home to the famous Konark Sun Temple, a UNESCO World Heritage site, and the ancient Jagannath Temple in Puri, which attracts millions of devotees annually. Odisha boasts beautiful beaches like Puri, Chandrabhaga, and Gopalpur, as well as the serene Chilika Lake, Asia's largest brackish water lagoon. The state’s vibrant festivals, including Rath Yatra and Durga Puja, reflect its spiritual significance. Odisha is also renowned for its classical dance form, Odissi, and its intricate handicrafts like silver filigree and applique work.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Odisha, one of India's oldest regions, has a rich history that dates back to the Maurya and Gupta periods. Ancient Odisha was known as Kalinga, famous for the Kalinga War in 261 BCE, fought between Emperor Ashoka of the Maurya Empire and the Kalinga Kingdom. After the war, Ashoka embraced Buddhism, leading to the spread of the religion in the region. Over centuries, Odisha saw the rise and fall of various dynasties, including the Eastern Ganga dynasty, under which the Jagannath Temple in Puri was built. The state witnessed cultural and architectural growth, preserving its unique heritage, temples, and traditions.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Odisha is from October to March, during the winter months, when the weather is pleasant and ideal for sightseeing. This period also coincides with major festivals like Rath Yatra and Durga Puja, offering an immersive cultural experience in the state’s rich traditions.\n"
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