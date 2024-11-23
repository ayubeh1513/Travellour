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
tk.Label(scrollable_frame, text="Rajasthan (7N/8D)", bg="#0A6372", fg="bisque",
         font=('Times New Roman', 22, "bold")).pack(pady=10)

image = Image.open("Mehrangarh_Fort_sanhita.jpg")  # Open the image

# Resize the image to fit the window size (600x600 in this case)
image = image.resize((500, 300))  # Resize to fit within 600x400 (adjust height/width as needed)
image = ImageTk.PhotoImage(image)  # Convert it to a Tkinter-compatible photo image

# Display the resized image in the Label widget
image_label = tk.Label(scrollable_frame, image=image, bg="#0A6372")
image_label.pack(pady=20)

# Add some long text to show the scrolling effect
h1 = "About"
tk.Label(scrollable_frame, text=h1, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t1 = "Rajasthan, the land of kings, is a vibrant state in India known for its rich history, majestic palaces, grand forts, and royal culture. This desert state offers an enchanting mix of traditional music, dance, cuisine, and architecture. Rajasthan is home to various UNESCO World Heritage Sites, including beautiful forts and palaces. Popular cities like Jaipur, Udaipur, Jodhpur, and Jaisalmer make it one of the most sought-after tourist destinations in India."
tk.Label(scrollable_frame, text=t1, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580,
         justify="center").pack(pady=10, padx=10)

h2 = "Places Covered in the Package"
tk.Label(scrollable_frame, text=h2, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10,
                                                                                                                padx=10)
t2 = '''
1. Jaipur (The Pink City): The capital city of Rajasthan, famous for its architectural wonders like Amber Fort, City Palace, and Hawa Mahal.

2. Udaipur (The City of Lakes): Known for its beautiful lakes and palaces, especially the Lake Palace, City Palace, and Jag Mandir.

3. Jodhpur (The Blue City): Famous for its Mehrangarh Fort, Umaid Bhawan Palace, and vibrant blue-painted houses.

4. Jaisalmer (The Golden City): Known for its Golden Fort, Sam Sand Dunes, and beautiful havelis.

5. Pushkar: A sacred town with the famous Pushkar Lake and Brahma Temple.

6. Mount Abu: The only hill station in Rajasthan, offering cool weather and attractions like Dilwara Temples and Nakki Lake.
'''
tk.Label(scrollable_frame, text=t2, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h3 = "Day-Wise Itinerary"
tk.Label(scrollable_frame, text=h3, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=20)
t3 = '''
Day 1: Arrival in Jaipur

* Arrival: Arrive in Jaipur and check-in at the hotel.

* Afternoon: Visit the City Palace and Jantar Mantar, an astronomical observatory.

* Evening: Explore Hawa Mahal and enjoy shopping in Johari Bazaar.

* Overnight Stay: Stay overnight at the hotel.


Day 2: Jaipur Sightseeing

* Morning: After breakfast, head to the Amber Fort. Enjoy an elephant ride or jeep ride to the fort and explore the intricate architecture.

* Afternoon: Visit Jal Mahal (Water Palace) and Nahargarh Fort for panoramic views of Jaipur.

* Evening: Enjoy a cultural evening at Chokhi Dhani, a traditional Rajasthani village-themed resort.

* Overnight Stay: Stay overnight at the hotel.


Day 3: Jaipur to Jodhpur

* Morning: After breakfast, drive to Jodhpur (approximately 6-7 hours).

* Afternoon: Check-in at the hotel in Jodhpur.

* Evening: Explore Clock Tower and Sardar Market for local handicrafts.

* Overnight Stay: Stay overnight at the hotel.


Day 4: Jodhpur Sightseeing

* Morning: Visit Mehrangarh Fort, one of the largest and most magnificent forts in India.

* Afternoon: Explore the Umaid Bhawan Palace and its museum.

* Evening: Relax and enjoy the views from Mandore Gardens.

* Overnight Stay: Stay overnight at the hotel.


Day 5: Jodhpur to Jaisalmer

* Morning: After breakfast, drive to Jaisalmer (approximately 5-6 hours).

* Afternoon: Check-in at the hotel in Jaisalmer.

* Evening: Visit the Jaisalmer Fort and explore the colorful lanes and markets within the fort.

* Overnight Stay: Stay overnight at the hotel.


Day 6: Jaisalmer Sightseeing

* Morning: Visit Patwon Ki Haveli and Sam Sand Dunes for a camel ride and cultural performances.

* Afternoon: Explore Bada Bagh and Jain Temples within the fort complex.

* Evening: Witness the sunset at Kuldhara Village, an abandoned village near Jaisalmer.

* Overnight Stay: Stay overnight at the hotel.


Day 7: Jaisalmer to Udaipur

* Morning: After breakfast, drive to Udaipur (approximately 9-10 hours).

* Afternoon: Check-in at the hotel in Udaipur.

* Evening: Relax at Lake Pichola and take a boat ride to Jag Mandir.

* Overnight Stay: Stay overnight at the hotel.


Day 8: Udaipur Sightseeing & Departure

* Morning: Visit the City Palace and explore the nearby Jagdish Temple.

* Afternoon: Visit the Saheliyon ki Bari (Garden of Maidens) and Fateh Sagar Lake.

* Evening: Departure from Udaipur to your onward destination.
'''
tk.Label(scrollable_frame, text=t3, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10)

h4 = "Best Time to Visit"
tk.Label(scrollable_frame, text=h4, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t4 = '''
1. Winter (October to March): Ideal time for sightseeing and exploring the palaces, forts, and desert landscapes with pleasant weather.

2. Summer (April to June): Extremely hot, especially in desert areas like Jaisalmer and Jodhpur; not recommended for sightseeing.

3. Monsoon (July to September): The landscape turns lush and green, but travel can be challenging due to rains, especially in desert regions.
'''
tk.Label(scrollable_frame, text=t4, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h5 = "How to Reach"
tk.Label(scrollable_frame, text=h5, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t5 = '''
1. By Air: Rajasthan has several airports, including Jaipur International Airport, Udaipur Maharana Pratap Airport, Jodhpur Airport, and Jaisalmer Airport, connecting major cities across India.

2. By Train: Rajasthan is well-connected by rail with major cities in India. Jaipur Junction, Udaipur City Railway Station, and Jodhpur Junction are the main railway stations.

3. By Road: Rajasthan is well-connected by road to cities like Delhi, Mumbai, and Ahmedabad. Regular buses and private taxis are available for travel within the state.
'''
tk.Label(scrollable_frame, text=t5, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)

h6 = "Important Notes"
tk.Label(scrollable_frame, text=h6, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t6 = '''
1. ID Proof: Carry a valid ID proof for hotel check-ins and sightseeing.

2. Clothing: Pack light cotton clothes for summer and warm clothing for winter, especially for desert regions at night.

3. Health & Safety: Carry necessary medications, stay hydrated, and wear sunscreen to protect from the sun. Be cautious of the heat in summer.

4. Advance Bookings: Book your accommodations, transport, and popular attractions like Amber Fort and Jaisalmer Camel Rides well in advance, especially during peak season (November to February).

5. Respect Local Culture: Rajasthan is culturally rich, and it’s important to respect local customs, especially when visiting temples and palaces.
'''
tk.Label(scrollable_frame, text=t6, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left",
         anchor="w").pack(pady=10, padx=10, fill="x")

h7 = "Reporting and Dropping Points for Guests"
tk.Label(scrollable_frame, text=h7, bg="#0A6372", fg="bisque", font=('Arial', 14, "bold"), wraplength=580).pack(pady=10)
t7 = '''
1. Reporting Point: Jaipur Railway Station, Jaipur Airport, or specified locations in other cities.

2. Dropping Point: Udaipur Railway Station, Udaipur Airport, or other designated locations for onward travel.
'''
tk.Label(scrollable_frame, text=t7, bg="#0A6372", fg="bisque", font=('Arial', 12), wraplength=580, justify="left").pack(
    pady=10, padx=10)


def go_back():
    root.destroy()
    os.system("python OTP.py")

back_button = tk.Button(scrollable_frame, text="Price: 98000/Head", bg="yellow", fg="black", font=('Arial', 14), width=20, height=2)
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