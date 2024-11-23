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
tk.Label(scrollable_frame, text="Shimla", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images.jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "ABOUT"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Shimla, the capital of Himachal Pradesh, is a serene hill station nestled in the majestic Himalayas. Known as the 'Queen of Hills,' it captivates visitors with its colonial charm, pleasant climate, and breathtaking landscapes. Shimla's iconic Mall Road offers a delightful mix of shops, cafes, and scenic views, while the Ridge provides a panoramic vista of the surrounding snow-capped peaks. The lush greenery of the Jakhoo Temple and the historic Christ Church add to its allure. Adventure enthusiasts can explore nearby trekking trails or enjoy winter sports. Shimla’s tranquil environment and vibrant culture make it a year-round tourist destination.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h2 = "HISTORY"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t2 = "Shimla, the summer capital of British India, has a rich history that blends colonial heritage with local traditions. Originally a quiet village, it gained prominence after the British discovered its pleasant climate in the early 19th century. Lord Amherst, the Governor-General of India, visited Shimla in 1827, marking the beginning of its transformation. By the mid-1800s, it became the British administrative retreat, with colonial architecture like the Viceregal Lodge and Christ Church emerging as landmarks. Shimla also played a significant role in Indian history, hosting the 1945 Simla Conference. Today, it stands as a vibrant reminder of its storied past.\n"
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10)

h3 = "BEST TIME TO VISIT"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = "The best time to visit Shimla is from March to June, when the weather is pleasant and ideal for sightseeing and outdoor activities. Winters, from November to February, are perfect for snow enthusiasts, offering picturesque snowfall and winter sports. Monsoons, from July to September, bring lush greenery but occasional landslides.\n"
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