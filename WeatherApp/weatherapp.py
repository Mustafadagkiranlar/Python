import tkinter as tk
from tkinter import font
import requests #we make api request

HEIGHT = 375
WIDTH = 475

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \n Temperature (°C): %s ' % (name, desc, temp)
	except:
		final_str = 'Teher was a problem retrieveing that information'

	return final_str

# api.openweathermap.org/data/2.5/weather/hourly?q={city name},{country code}

def get_weather(city):
	Weather_key = '3330900759726c5efbf5ddbb2264b4e8'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': Weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()
#canvas is a container for button
canvas = tk.Canvas(root, height= HEIGHT, width = WIDTH)
canvas.pack()

backgorund_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=backgorund_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=3)#bd for border / fit the height and width of the root dimension
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')# anchor used to make it center n for north / relx and rely centers the square relative w and h show how much of the space takes according to the roots dimensions.

entry = tk.Entry(frame, font=('Courier', 10))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text= "Get Weather", font=('Courier', 9), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 15), anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

root.mainloop()
