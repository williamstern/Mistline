import re
import requests
import geocoder

#api_key = "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie"
def find_cordinates(user):
    geo = geocoder.ip(user)
    lat = geo.latlng[0]
    lng = geo.latlng[1]

    return (lat, lng)

def parse(weather_data):    
    matches = re.findall(':(-?[0-9]+.?[0-9]*),', weather_data)
    for i in range(len(matches)):
        matches[i] = float(matches[i])
    precip_type = re.search('"[a-z]+_[a-z]}+":{"[a-z]+":"([a-z]+])"},', weather_data)
    matches.append(precip_type)
    
    print(matches)
    return matches


# lets change this to a dict

def input_dict(list_t,field_t, lat, lon):
    input_dict["lat"] = lat
    input_dict["lon"] = lon
    
    for i, j in zip(list_t, field_t): 
        input_dict[j] = i
    return input_dict

class realtime:
    def __init__(self, data_dict):
        self.data = data_dict

    def display(self):
        for x in self.data:
            print(str(x) + " :" + str(self.data[x]))
    
header = {
    'apikey': "GA8VgLQpB0Whf3D7KDuHwbvii1LBmyie",
}
(lt, lg) = find_cordinates("me")

fields = ["temp", "feels_like","precipitation","precipitation_type"]

payload = {"lat": lt, 'lon': lg, "location_id": "me", "unit_system" : "us", "fields": fields}

url = "https://api.climacell.co/v3/weather/realtime"
response = requests.request("GET", url, headers=header, params=payload)

print(response.text)
list_t = parse(response.text)  
print(type(list_t))
 


