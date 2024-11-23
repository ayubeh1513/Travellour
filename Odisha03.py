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
tk.Label(scrollable_frame, text="Odisha (7N/8D)", bg="#0A6372", fg="bisque",
         font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("images (3).jpeg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Odisha, located on the eastern coast of India, is a land of cultural heritage, stunning temples, and scenic beaches. Known for its rich history, ancient temples, and unique art and craft, Odisha offers a perfect mix of spiritual retreats, historical exploration, and natural beauty. The state is home to the famous Jagannath Temple in Puri, the Konark Sun Temple, and beautiful beaches like Chilika Lake and Gopalpur. Odisha is also known for its classical dance form, Odissi, and vibrant festivals."
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580,
         justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10,
                                                                                                                padx=10)
t2 = '''
1. Bhubaneswar: The capital city, known as the "Temple City of India," home to several ancient temples like Lingaraj Temple, Mukteswar Temple, and Rajarani Temple.

2. Puri: Famous for the Jagannath Temple, one of the Char Dhams, and the beautiful Puri Beach.

3. Konark: Home to the famous Konark Sun Temple, a UNESCO World Heritage site, and the nearby Chandrabhaga Beach.

4. Chilika Lake: Asia’s largest brackish water lagoon, a hotspot for migratory birds and peaceful boat rides.

5. Cuttack: Known for its Barabati Fort and Cuttack Chandi Temple.

6. Gopalpur: A serene beach town on the southern coast, known for its peaceful atmosphere and scenic beach.

7. Raghurajpur: A heritage crafts village known for Pattachitra painting and traditional handicrafts.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Bhubaneswar

* Arrival: Arrive in Bhubaneswar, the capital city of Odisha, and check-in at the hotel.

* Afternoon: Visit the Lingaraj Temple, a prime example of Kalinga architecture.

* Evening: Explore the Mukteswar Temple, Rajarani Temple, and the Nandankanan Zoo if time permits.

* Overnight Stay: Stay overnight at the hotel in Bhubaneswar.


Day 2: Bhubaneswar Sightseeing

* Morning: Visit the Kedar Gouri Temple and Dhauli Peace Pagoda, a significant Buddhist site.

* Afternoon: Explore the Odisha State Museum and Ekamra Haat for handicrafts.

* Evening: Relax at Bindusagar Lake and the Nandankanan Zoo for a nature walk.

* Overnight Stay: Stay overnight at the hotel in Bhubaneswar.


Day 3: Bhubaneswar to Puri (65 km, 1.5 hours drive)

* Morning: After breakfast, drive to Puri.

* Afternoon: Check-in at the hotel and visit the famous Jagannath Temple, an important pilgrimage destination.

* Evening: Relax at Puri Beach or enjoy the evening aarti at the Jagannath Temple.

* Overnight Stay: Stay overnight at the hotel in Puri.


Day 4: Puri and Konark Excursion

* Morning: Visit the Chilika Lake, known for migratory birds and scenic boat rides.

* Afternoon: Proceed to Konark to visit the UNESCO-listed Konark Sun Temple, also known as the Black Pagoda.

* Evening: Explore Chandrabhaga Beach, a quiet beach ideal for relaxation.

* Overnight Stay: Stay overnight at the hotel in Puri.


Day 5: Puri to Cuttack (35 km, 1-hour drive)

* Morning: After breakfast, drive to Cuttack.

* Afternoon: Visit Barabati Fort, Cuttack Chandi Temple, and explore the bustling Cuttack Bazar.

* Evening: Visit Mahanadi Barrage and enjoy the views of the river.

* Overnight Stay: Stay overnight at the hotel in Cuttack.


Day 6: Cuttack to Gopalpur (180 km, 4-5 hours drive)

* Morning: After breakfast, head to Gopalpur, a serene beach town.

* Afternoon: Check-in at the hotel and relax at Gopalpur Beach.

* Evening: Enjoy the sunset at Gopalpur Beach and explore the peaceful atmosphere.

* Overnight Stay: Stay overnight at the hotel in Gopalpur.


Day 7: Gopalpur to Raghurajpur (90 km, 2-3 hours drive)

* Morning: After breakfast, drive to Raghurajpur, a heritage village known for its traditional crafts and art.

* Afternoon: Explore the handicrafts village, known for Pattachitra paintings and other Odisha crafts.

* Evening: Return to Bhubaneswar for the final night.

* Overnight Stay: Stay overnight at the hotel in Bhubaneswar.


Day 8: Departure from Bhubaneswar

* Morning: After breakfast, check-out from the hotel and proceed to the Bhubaneswar Railway Station or Bhubaneswar Airport for departure.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''
1. Winter (October to March): The best time for sightseeing and enjoying the pleasant weather, especially for beach visits and temple tours.

2. Summer (April to June): Hot and humid, less ideal for outdoor activities, especially near the coast.

3. Monsoon (July to September): While the monsoon season adds lush greenery, it may cause some travel disruptions due to rains.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''
1. By Air: Bhubaneswar has the Biju Patnaik International Airport, which is well-connected to major cities across India.

2. By Train: Bhubaneswar, Puri, and Cuttack are major railway stations with good connectivity from across India.

3. By Road: Odisha is well-connected by road, with regular buses and private taxis available from cities like Kolkata, Visakhapatnam, and Ranchi.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''
1. ID Proof: Carry a valid government-issued ID proof for hotel check-ins and temple visits.

2. Clothing: Light cotton clothes are recommended for summer, and warm clothes during the winter season, especially during evenings and early mornings.

3. Health & Safety: Carry necessary medications and stay hydrated, particularly in the coastal regions.

4. Advance Bookings: Book accommodations and temple darshan tickets in advance during the peak season (December to January) to avoid any inconvenience.

5. Respect Local Culture: Odisha is a culturally rich state, so it is important to dress modestly while visiting temples and respect local traditions.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left",
         anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''
1. Reporting Point: Bhubaneswar Railway Station, Bhubaneswar Airport, or any specified location.

2. Dropping Point: Bhubaneswar Railway Station, Bhubaneswar Airport, or any other location as per guest preference.
'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)


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