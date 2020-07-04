import requests
import geocoder

#api_key = "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie"
def find_cordinates(user):
    geo = geocoder.ip(user)
    lat = geo.latlng[0]
    lng = geo.latlng[1]

    return (lat, lng)

header = {
    'Content-Type': 'application/json',
    'apikey': "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie",
}
(lt, lg) = find_cordinates("me")
fields = ["temp", "feels_like", "humidity", "wind_speed", "precipitation_probability"]
payload = {"lat": lt, 'lon': lg, "location_id": "me", "unit_system" : "us", "fields": fields}

url = "https://api.climacell.co/v3/weather/forecast/realtime"
response = requests.request("GET", url, headers=header, params=payload)

print(response.text)



