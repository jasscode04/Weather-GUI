from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfeild.get().strip()
    if not city:
        messagebox.showerror("Weather App", "Please enter a city name!")
        return
    
    try:
        geolocator = Nominatim(user_agent="MyWeatherApp_123")
        location = geolocator.geocode(city, timeout=10)

        if location is None:
            messagebox.showerror("Weather App", "City not found! Please enter a valid city.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        if result is None:
            messagebox.showerror("Weather App", "Timezone not found for this location.")
            return
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

       
        api_key = "646824f2b7b86caffec1d0b16ea77f79"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        json_data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Weather App", f"Error fetching weather data: {json_data.get('message', 'Unknown error')}")
            return

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | Feels Like {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description.capitalize())
        p.config(text=f"{pressure} hPa")

    except requests.exceptions.RequestException:
        messagebox.showerror("Weather App", "Network error! Check your internet connection.")
    except Exception as e:
        messagebox.showerror("Weather App", f"Error: {str(e)}")

Search_image = PhotoImage(file="search.png")
myimage = Label(root, image=Search_image)
myimage.place(x=20, y=20)

textfeild = tk.Entry(root, justify="center", width=17, font=("sans-serif", 25, "bold"), bg="#404040", border=0, fg="white")
textfeild.place(x=50, y=40)
textfeild.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)


Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)


Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)


name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=120, y=400)
Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=250, y=400)
Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=430, y=400)
Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef").place(x=650, y=400)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
