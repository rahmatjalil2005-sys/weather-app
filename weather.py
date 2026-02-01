import tkinter as tk
from tkinter import messagebox

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def get_weather():
    pass


root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.attributes("-alpha", 0.9)


# search box
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(root, image=search_image)
search_image_label.pack(pady=20, side=tk.TOP)

textfield = tk.Entry(root, justify="center", width=17, 
                    font=("poppins", 25, "bold"),
                    bg="#404040",  fg="white", border=0)
textfield.place(x=280, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(root, image=search_icon, borderwidth=0,
                                   cursor="hand2", bg="#404040",
                                   command=get_weather)
search_icon_button.place(x=590, y=34)

# logo
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)

#bottom box
frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(root, image=frame_image)
frame_label.pack(pady=10, side=tk.BOTTOM)

#city name
city_label = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd")
city_label.place(x=120, y=160)

#time
time_label = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
time_label.place(x=120, y=230)

clock = tk.Label(root, font=("Helvetica", 20), fg="#4b4bcc")
clock.place(x=120, y=270)

#labels
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=280, y=400)
label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)
label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=670, y=400)

temp_label = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")
temp_label.place(x=590, y=170)

condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc")
condition_label.place(x=590, y=270)

wind_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
wind_label.place(x=120, y=430)
humidity_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
humidity_label.place(x=280, y=430)
description_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
description_label.place(x=450, y=430)
pressure_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
pressure_label.place(x=670, y=430)

root.mainloop()

