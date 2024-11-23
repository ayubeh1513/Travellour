import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("615x600")
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
tk.Label(scrollable_frame, text="Shri Mata Vaishno Devi (3N/4D)", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (1).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Shri Mata Vaishno Devi, nestled in the Trikuta Hills of Jammu and Kashmir, is one of India's most revered pilgrimage sites. The shrine, dedicated to Goddess Vaishno Devi, attracts millions of devotees annually. The trek to the sacred cave offers breathtaking views of the surrounding mountains, blending spirituality with natural beauty.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10, padx=10)
t2 = '''
1. Katra: The base town for the Vaishno Devi pilgrimage.

2. Ardhkuwari Temple: A midway point on the trek, considered sacred for resting during the journey.

3. Vaishno Devi Shrine: The main cave temple where the goddess resides.

4. Bhairon Temple: Located 2 km uphill from the shrine, considered essential for completing the pilgrimage.

5. Shiv Khori (Optional): A naturally formed cave dedicated to Lord Shiva.

6. Patnitop (Optional): A scenic hill station with stunning views and serene landscapes.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Katra

* Arrival: Reach Katra by train, road, or flight.

* Check-in: Settle into your hotel and relax.

* Evening: Explore the local market for traditional handicrafts and local cuisine.

* Stay: Overnight at the hotel.


Day 2: Vaishno Devi Yatra

* Early Morning: Begin your trek or pony ride to Ardhkuwari Temple.

* Journey to the Shrine: Continue trekking to the Vaishno Devi Shrine.

* Darshan: Pay homage to Goddess Vaishno Devi and experience divine tranquility.

* Optional: Visit Bhairon Temple before descending (accessible by foot or ropeway).

* Evening: Return to Katra.

* Stay: Overnight at the hotel.


Day 3: Local Excursions (Optional)

* Option 1: Shiv Khori
    
    * Explore this sacred cave known for its naturally formed Shivling.
    
    * Suitable for those interested in mythology and spiritual experiences.

* Option 2: Patnitop
    
    * Visit this picturesque hill station for sightseeing and relaxation.
    
    * Enjoy activities like paragliding and photography.

* Return: Back to Katra by evening.

* Stay: Overnight at the hotel.


* Day 4: Departure

* Morning: Check out from the hotel.

* Optional Sightseeing: Visit Jhajjar Kotli or other nearby attractions during the journey back.

* Drop-off: Proceed to the bus stand, railway station, or airport for departure.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''
1. March to October: Ideal weather with comfortable conditions for trekking.

2. November to February: Experience snowfall, but the cold weather makes the trek more challenging.

3. Navratri Season: Special decorations, religious fervor, and vibrant atmosphere.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''
1. By Air: Jammu Airport (approx. 50 km from Katra) is the nearest airport.

2. By Train: Katra Railway Station is well-connected to major cities like Delhi and Mumbai.

3. By Road: Regular buses and taxis are available from Jammu, Srinagar, and other neighboring regions.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''
1. Carry a valid ID proof for registration at Katra.

2. Wear comfortable trekking shoes and dress appropriately.

3. Keep essentials like water bottles, first aid kits, and personal medications handy.

4. Book a Yatra Slip online or at the Katra registration counter before starting the trek.

5. Respect the sanctity of the place by following local rules and guidelines.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left", anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''
1. Reporting Points: Jammu Airport, Katra Railway Station, or Katra Bus Stand.

2. Dropping Points: Katra Railway Station, Jammu Airport, or any pre-decided location.
'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

def go_back():
    root.destroy()
    os.system("python OTP.py")

back_button = tk.Button(scrollable_frame, text="Price: 38000/Head", bg="yellow", fg="black", font=('Arial', 14), width=20, height=2)
back_button.pack(pady=20)
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