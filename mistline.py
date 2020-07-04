import requests
import geocoder

#api_key = GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie

#url = "https://api.climacell.co/v3/weather/forecast/hourly"

#response = requests.request("GET", url)

#print(response)

def find_cordinates(user):
    geo = geocoder.ip(user)
    lat = geo.latlng[0]
    lng = geo.latlng[1]

    return (lat, lng)


(lt, lg) = find_cordinates("me")
print(lt)
print(lg)


