import tkinter as tk
import os
from PIL import Image, ImageTk  # Import from Pillow

root = tk.Tk()
root.geometry("615x600")
root.title("Travellour - AMRITSAR01")

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
tk.Label(scrollable_frame, text="Travellour", bg="bisque", fg="#0A6372",
         font=('Times New Roman', 26, "bold", "italic")).pack(pady=10)
tk.Label(scrollable_frame, text="Amritsar (3N/4D)", bg="#0A6372", fg="bisque",
         font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (4).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Amritsar, the spiritual and cultural center of the Sikh religion, is a city of deep historical significance. Located in the state of Punjab, it is famous for the Golden Temple (Harmandir Sahib), a sacred place of worship for Sikhs, surrounded by a serene pool. The city is also home to many important Sikh landmarks, vibrant markets, and delicious Punjabi cuisine. Amritsar offers a blend of spirituality, history, and vibrant culture, making it a must-visit destination."
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580,
         justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10,
                                                                                                                padx=10)
t2 = '''
1. Golden Temple (Harmandir Sahib): The most iconic and revered Sikh Gurudwara, known for its stunning golden architecture and tranquil surroundings.

2. Jallianwala Bagh: A historical site that commemorates the massacre of hundreds of Indians during British rule in 1919.

3. Wagah Border: The ceremonial border between India and Pakistan, known for its dramatic daily flag-lowering ceremony.

4. Durgiana Temple: A beautiful Hindu temple similar in architecture to the Golden Temple, dedicated to Goddess Durga.

5. Mata Lal Devi Temple: A unique temple dedicated to the Goddess Lal Devi with narrow tunnels and passageways to explore.

6. Partition Museum: A museum dedicated to the history and events surrounding the partition of India in 1947.

7. Sikh Museum: A museum located in the Golden Temple complex, showcasing the history of Sikhism.

8. Hall Bazaar: A lively market for shopping local handicrafts, textiles, and traditional Punjabi items.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Amritsar & Local Sightseeing

* Arrival: Arrive in Amritsar and check-in at the hotel.

* Morning: Visit the iconic Golden Temple, spend time offering prayers and explore the serene complex.

* Afternoon: Head to Jallianwala Bagh to witness the historical site of the 1919 massacre and learn about its significance.

* Evening: Enjoy the spiritual atmosphere at Durgiana Temple, a beautiful Hindu temple located nearby.

* Overnight Stay: Return to the hotel for the night.


Day 2: Wagah Border & More Local Sightseeing

* Morning: After breakfast, depart for the Wagah Border, located about 30 km from Amritsar, to witness the famous flag-lowering ceremony.

* Afternoon: Return to Amritsar and visit the Mata Lal Devi Temple, an unusual temple with winding tunnels and a spiritual experience.

* Evening: Spend time exploring Hall Bazaar, perfect for shopping local souvenirs and traditional handicrafts.

* Overnight Stay: Stay overnight at the hotel.


Day 3: Partition Museum & Sikh Museum

* Morning: After breakfast, visit the Partition Museum, dedicated to the history of the Partition of India in 1947, and the events that changed the country’s history.

* Afternoon: Explore the Sikh Museum located within the Golden Temple complex. Learn about the history and evolution of Sikhism.

* Evening: Enjoy a relaxing evening at the Golden Temple for the Evening Prayers and the mesmerizing view of the temple illuminated by lights.

* Overnight Stay: Return to your hotel for an overnight stay.


Day 4: Departure & Enroute Sightseeing

* Morning: After breakfast, check out from the hotel.

* Enroute: If time permits, visit Ram Bagh Garden or relax at a café before departing.

* Departure: Drop-off at Amritsar Railway Station or Airport for onward journey.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''
1. Winter (October to March): Ideal for sightseeing with pleasant weather, making it the most popular time to visit.

2. Summer (April to June): Hot weather, but fewer crowds; visit in the early morning or evening to avoid the heat.

3. Monsoon (July to September): Rainy season, which may cause disruptions in travel, though the city looks lush and green.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''
1. By Air: The nearest airport is Sri Guru Ram Dass Jee International Airport, located about 11 km from the city center.

2. By Train: Amritsar is well-connected by rail with major cities. The Amritsar Junction is the main railway station.

3. By Road: Amritsar is well-connected by bus and road with major cities like Delhi (450 km), Chandigarh (230 km), and other parts of Punjab.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''
1. ID Proof: Carry a valid ID proof for hotel check-ins and visiting the Golden Temple.

2. Clothing: Modest clothing is required to visit religious places like the Golden Temple. Guests are expected to cover their heads (scarves are provided).

3. Weather: Carry appropriate clothing based on the season. Summers can be very hot, while winters can get chilly, especially in the evenings.

4. Health & Safety: Carry necessary medications and essentials. Always stay hydrated and protect yourself from the sun in summer.

5. Advance Bookings: Make sure to book your hotels and transportation in advance, especially during peak tourist seasons (November to March).

6. Respect Local Traditions: Be mindful of local customs, especially when visiting religious sites.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left",
         anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''
1. Reporting Point: Amritsar Railway Station, Amritsar Bus Stand, or Sri Guru Ram Dass Jee International Airport.

2. Dropping Point: Amritsar Railway Station, Amritsar Bus Stand, or Sri Guru Ram Dass Jee International Airport, based on the guest’s travel preferences.
'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)


def go_back():
    root.destroy()
    os.system("python OTP.py")

back_button = tk.Button(scrollable_frame, text="Price: 32000/Head", bg="yellow", fg="black", font=('Arial', 14), width=20, height=2)
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