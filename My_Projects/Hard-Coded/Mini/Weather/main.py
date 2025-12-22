import requests, json
from getloc import lat_lon

api = "8106a06c15b44919d06dfc151ce2ba81"
print("Welcome to the Weather App! 🌤️")
city = input("Enter the city/area name: ")

lat, lon = lat_lon(city)

if lat is None or lon is None:
    print(f"Error: Could not find location for '{city}'. Please check the city name and try again.")
    exit()

def get_weather():
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric").json()
    status = weather['weather'][0]['description']
    temp = weather['main']['temp']
    feel = weather['main']['feels_like']
    humidity = weather['main']['humidity']
    return status, temp, feel, humidity


status, temp, feel, humidity = get_weather()
print (f"The current weather status in {city} is {status}")
print (f"The current temperature in {city} is {temp}°C")
print (f"The current feels like in {city} is {feel}°C")
print (f"The current humidity in {city} is {humidity}%")
