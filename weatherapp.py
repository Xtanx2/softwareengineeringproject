import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_weather(city):
    weather_key = 'e496c4f1f7e7f7300f08630a566dc4e5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}

    try:
        response = requests.get(url, params)
        response.raise_for_status()
        weather = response.json()
        display_weather(weather)
    except requests.exceptions.RequestException as e:
        result.config(text="Error retrieving weather data.")

def display_weather(weather):
    try:
        city_name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        result.config(text=f"City: {city_name}\nDescription: {description}\nTemperature: {temperature}°F")
    except KeyError:
        result.config(text="Error displaying weather data.")

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        return f"City: {city}\nDescription: {condition}\nTemperature: {temperature}°F"
    except KeyError:
        return "Error formatting weather data."

root = tk.Tk()
root.title("Weather App")
root.geometry("600x500")

img = Image.open('bg.png')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)
bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

heading_title = tk.Label(bg_lbl, text='Earth including over 200,000 cities!', fg='red', bg='sky blue',
                         font=('times new roman', 18, 'bold'))
heading_title.place(x=80, y=18)

frame_one = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new roman', 25), width=17)
txt_box.grid(row=0, column=0)

btn = tk.Button(frame_one, text='Get Weather', fg='green', font=('times new roman', 16, 'bold'),
                command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(frame_two, font=('times new roman', 16), bg='white', justify='left')
result.place(relwidth=1, relheight=1)

root.mainloop()