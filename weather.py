# Weather Program

# This program gets json info from 2 apis from OpenWeatherMap.org and displays
# weather informationto the user.

import requests # imports the requests module which must be separately 
                # installed.


apikey = "7545be23dce3cfbc78f1895dc0e38158"

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={self.lat}&lon={self.lon}&appid=7545be23dce3cfbc78f1895dc0e38158")
        except:
            print("Error: Internet connection problems.")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.description = self.response_json["weather"][0]["description"]

    def temp_print(self):
        print(f"In {self.name}, it is currently {self.temp}°F")
        print(f"Today's high: {self.temp_max}°F")
        print(f"Today's low: {self.temp_min}°F")
        print(f"Description: {self.description}")
        
 #--------------------------------------------------------------------       
print()
print("*************************")
print("***** Weather App *******")
print("*************************")
city = input("Enter City: ")
state = input("Enter State Code: ")
country = input("Enter Country Code: ")

try:
    georesponse = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=5&appid={apikey}")
except:
    print("Error: Internet connection problems.")

# print(georesponse.json())

print("*************************")
geo_json = georesponse.json()

name = geo_json[0]["name"]
lat = geo_json[0]["lat"]
lon = geo_json[0]["lon"]

print("City: ",name)
print("State: ",state)
print("Country: ",country)
print("Latitude: ", lat)
print("Longitude: ",lon)

my_city = City(name, lat, lon)

my_city.temp_print()

print("*************************")
print()


    



