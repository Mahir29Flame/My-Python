import requests, json

api = "8106a06c15b44919d06dfc151ce2ba81"

def lat_lon(city):
    country = "BD"
    locres = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=5&appid={api}")
    data = locres.json()
    if not data:
        return None, None
    
    loc = data[0]
    lat = loc['lat']
    lon = loc['lon']
    
    return lat, lon

if __name__ == "__main__":
    city = input("Enter the city/area name: ")
    lat, lon = lat_lon(city)
    print(lat, lon)