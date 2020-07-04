import requests
import geocoder

#api_key = "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie"
def find_cordinates(user):
    geo = geocoder.ip(user)
    lat = geo.latlng[0]
    lng = geo.latlng[1]

    return (lat, lng)

class real_time:
    def __init__(self, lat, lon, temp, feel_like, precipitation, precipitation_type,observation_time):
        self.lat = lat
        self.lon = lon 
        self.temp =temp
        self.feel_like = feel_like
        self.precipitation = precipitation
        self.precipitation_type =precipitation_type
        self.observation_time = observation_time
    
    def display(self):
        print("Day/time : " + str(self.observation_time))
        print("location : " + str(self.lat) + str(self.lon))
        print("temp: " + str(self.temp))
        print("feel_like " + str(self.feel_like))
        print("precipitation : " + str(self.precipitation))
        print("precipitation : " + str(self.precipitation_type))



header = {
    'Content-Type': 'application/json',
    'apikey': "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie",
}
(lt, lg) = find_cordinates("me")
fields = ["temp", "feels_like","precipitation_type","precipitation"]
payload = {"lat": lt, 'lon': lg, "location_id": "me", "unit_system" : "us", "fields": fields}

url = "https://api.climacell.co/v3/weather/realtime"
response = requests.request("GET", url, headers=header, params=payload)

print(response.text)



