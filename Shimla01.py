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
tk.Label(scrollable_frame, text="Travellour", bg="bisque", fg="#0A6372",
         font=('Times New Roman', 26, "bold", "italic")).pack(pady=10)
tk.Label(scrollable_frame, text="Shimla (3N/4D)", bg="#0A6372", fg="bisque",
         font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images.jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Shimla, the capital of Himachal Pradesh, is a picturesque hill station located in the northwestern part of India. Surrounded by snow-capped mountains, lush green forests, and colonial-era architecture, Shimla offers a perfect blend of natural beauty and cultural heritage. Famous for its pleasant climate, scenic landscapes, and historical attractions, Shimla is an ideal destination for nature lovers, honeymooners, and families. Popular activities include sightseeing, trekking, and shopping on the vibrant Mall Road."
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580,
         justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10,
                                                                                                                padx=10)
t2 = '''
1. The Ridge and Mall Road: Shimla’s bustling marketplace, perfect for shopping, dining, and enjoying local cuisine.

2. Jakhoo Temple: A hilltop temple dedicated to Lord Hanuman, offering panoramic views of Shimla.

3. Kufri: A famous spot for adventure sports like skiing and tobogganing in winter, and a serene getaway for nature lovers.

4. Christ Church: One of the oldest churches in North India, known for its gothic architecture and beautiful stained glass windows.

5. Summer Hill: A peaceful spot offering scenic views of the Shimla town and the surrounding mountains.

6. Chail: A beautiful hill station near Shimla, known for the world’s highest cricket ground and the Chail Palace.

7. Tattapani Hot Springs: Natural sulfur springs offering a relaxing experience.

8. Naldehra: A scenic golf course surrounded by lush greenery, ideal for a peaceful retreat.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Shimla & Local Sightseeing

* Arrival: Arrive in Shimla and check-in at your hotel.

* Morning: Start your sightseeing with a visit to The Ridge and Mall Road, where you can shop for local handicrafts and try local delicacies.

* Afternoon: Visit the Jakhoo Temple, which is located on a hill and offers panoramic views of the town.

* Evening: Explore Shimla’s vibrant Mall Road and indulge in local street food.

* Overnight Stay: Relax and enjoy a peaceful night at the hotel.


Day 2: Kufri & Fagu Excursion

* Morning: After breakfast, visit Kufri, famous for its adventure activities. Enjoy skiing (winter) or indulge in nature walks and visit the Himalayan Nature Park.

* Afternoon: Visit Fagu, a charming village surrounded by apple orchards and pine forests.

* Evening: Return to Shimla and relax.

* Overnight Stay: Stay at your hotel in Shimla.


Day 3: Chail, Naldehra & Tattapani

* Morning: After breakfast, head to Chail, known for its world's highest cricket ground and Chail Palace.

* Afternoon: Proceed to Naldehra, a scenic golf course with beautiful views of the hills and valleys. Then visit Tattapani to experience the natural hot springs.

* Evening: Return to Shimla and enjoy a relaxed evening.

* Overnight Stay: Stay at your hotel in Shimla.


Day 4: Departure with Enroute Sightseeing

* Morning: After breakfast, check out from your hotel.

* Enroute: Visit Summer Hill and enjoy the scenic beauty. Optionally, stop at Chadwick Falls if time permits.

* Departure: Guests are dropped off at Shimla Railway Station or Bus Stand for their onward journey.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''
1. Summer (March to June): Ideal for sightseeing and outdoor activities, with pleasant weather.

2. Winter (October to February): Experience snowfall and indulge in winter sports.

3. Monsoon (July to September): Lush greenery but prone to landslides; not the best time for travel.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''
1. By Air: The nearest airport is Shimla Airport (Jubbarhatti), located around 23 km from Shimla.

2. By Train: The nearest major railway station is Kalka Railway Station. From Kalka, you can take a toy train to Shimla.

3. By Road: Shimla is well-connected by roads to cities like Delhi (350 km), Chandigarh (120 km), and other parts of Himachal Pradesh. Regular buses and taxis are available.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''
1. ID Proof: Carry a valid ID proof for hotel check-ins and permits.

2. Clothing: Pack warm clothing, especially if you’re visiting in winter.

3. Health & Safety: Carry necessary medications and personal essentials. Take caution when visiting high-altitude areas.

4. Advance Bookings: Make advance bookings for transportation and hotels during peak season (March to June, December to January).

5. Permits: Check if any attractions require permits, like skiing in Kufri or visiting certain temples.

6. Respect Local Culture: Be mindful of local customs and traditions, particularly when visiting religious sites.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left",
         anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''
1. Reporting Point: Shimla Railway Station, Shimla Bus Stand, or specified locations in nearby cities.

2. Dropping Point: Shimla Railway Station, Shimla Bus Stand, or other designated locations for onward travel.
'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)


def go_back():
    root.destroy()
    os.system("python OTP.py")

back_button = tk.Button(scrollable_frame, text="Price: 48000/Head", bg="yellow", fg="black", font=('Arial', 14), width=20, height=2)
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