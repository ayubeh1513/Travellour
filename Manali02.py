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
tk.Label(scrollable_frame, text="Manali (6N/7D)", bg="#0A6372", fg="bisque", font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("hq720.jpg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Manali, nestled in the Kullu Valley of Himachal Pradesh, is a charming hill station known for its snow-capped peaks, lush valleys, gushing rivers, and vibrant cultural heritage. It is a popular destination for adventure enthusiasts, honeymooners, and families, offering activities like trekking, paragliding, and skiing alongside serene landscapes and spiritual retreats.\n"
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10, padx=10)
t2 = '''
1. Hadimba Devi Temple: A serene wooden temple surrounded by cedar forests, dedicated to Goddess Hadimba.

2. Solang Valley: A hub for adventure activities like paragliding, skiing, and zorbing.

3. Rohtang Pass (subject to availability): A snow-laden paradise offering breathtaking views.

4. Manikaran Sahib: A spiritual Gurudwara with natural hot springs.

5. Vashisht Village: Known for its sulfur hot springs and ancient temples.

6. Naggar Castle: A historical castle offering stunning views of the Kullu Valley.

7. Mall Road: A vibrant marketplace with local handicrafts and food options.

8. Old Manali: A quaint area with cafes, shops, and a glimpse of Himachali culture.

9. Jogini Waterfalls: A serene trek to stunning waterfalls amidst lush greenery.

10. Kullu: Famous for river rafting, apple orchards, and shawl factories.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Manali & Local Exploration

* Arrival: Check-in to your hotel in Manali.

* Sightseeing: Visit the Hadimba Devi Temple, Vashisht Hot Springs, and the Club House.

* Evening: Stroll along Mall Road, exploring shops and enjoying local cuisine.

* Stay: Overnight at the hotel.


Day 2: Solang Valley Adventure

* Morning: Post breakfast, head to Solang Valley.

* Activities: Experience paragliding, skiing, snow scooter rides, and other adventure sports.

* Leisure: Enjoy picturesque views and take photographs.

* Evening: Return to the hotel for relaxation.

* Stay: Overnight at the hotel.


Day 3: Excursion to Rohtang Pass

* Morning: Begin your day early to visit Rohtang Pass (permits required).

* Activities: Witness snow-covered landscapes and enjoy snow-related activities.

* Alternate: If Rohtang is inaccessible, visit nearby areas like Marhi or Gulaba.

* Stay: Overnight at the hotel.


Day 4: Naggar Castle & Jogini Waterfalls

* Morning: Visit the Naggar Castle, a historical marvel with stunning architecture.

* Afternoon: Embark on a trek to Jogini Waterfalls, enjoying nature at its best.

* Evening: Explore Old Manali, famous for its cafes and tranquil vibe.

* Stay: Overnight at the hotel.


Day 5: Kullu & Manikaran Sahib

* Morning: Drive to Kullu, known for its river rafting and Shawl Factories.

* Afternoon: Visit Manikaran Sahib Gurudwara, famous for its hot springs and spiritual significance.

* Evening: Return to Manali for leisure time.

* Stay: Overnight at the hotel.


Day 6: Departure

* Morning: Check out from the hotel after breakfast.

* Enroute Sightseeing: Visit attractions like Bijli Mahadev Temple or enjoy scenic views during the journey.

* Drop-off: Proceed to the bus stand, airport, or railway station for departure.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''1. Summer (March to June): Pleasant weather, ideal for sightseeing and outdoor activities.

2. Winter (October to February): Snowfall and winter sports.

3. Monsoon (July to September): Lush greenery but prone to landslides; less recommended.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''1. By Air: The nearest airport is Bhuntar, about 50 km from Manali.

2. By Train: Chandigarh or Ambala is the nearest railway station, followed by a road journey.

3. By Road: Well-connected by buses and private vehicles from major cities like Delhi and Chandigarh.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''1. Carry a valid ID proof for hotel check-ins and permits.

2. Pack warm clothing, especially during winters.

3. Keep necessary medications and personal essentials handy.

4. Book Rohtang Pass permits in advance to avoid last-minute hassles.

5. Follow local guidelines and respect the natural surroundings.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left", anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''1. Reporting Point: Delhi ISBT, Chandigarh, or Bhuntar Airport.

2. Dropping Point: Manali Bus Stand, Bhuntar Airport, or other specified locations.

'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(pady=10, padx=10)

def go_back():
    root.destroy()
    os.system("python OTP.py")

back_button = tk.Button(scrollable_frame, text="Price: 96000/Head", bg="yellow", fg="black", font=('Arial', 14), width=20, height=2)
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