import requests
import geocoder

#api_key = GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie

#url = "https://api.climacell.co/v3/weather/forecast/hourly"

#response = requests.request("GET", url)

#print(response)


geo = geocoder.ip('me')
lat = geo.latlng[0]
lng = geo.latlng[1]

print(lat)
print(lng)
print("what is a printf")