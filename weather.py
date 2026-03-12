from datetime import datetime as dt
import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

api_key = ""
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Sunrise:", data["sys"]["sunrise"])
    print("Sunset:", data["sys"]["sunset"])
    print("Cloudiness:", data["clouds"]["all"], "%")
    print("Visibility:", data["visibility"], "meters")
    print("Coordinates:", data["coord"]["lat"], "°N", data["coord"]["lon"], "°E")
    print("Timezone:", data["timezone"], "seconds from UTC")
    print("Weather Icon:", data["weather"][0]["icon"])
    print("Weather ID:", data["weather"][0]["id"])
else:
    print("Error fetching data")