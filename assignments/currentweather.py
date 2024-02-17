# a program that prints out the current temperature and wind direction on the console

# by Rachel King

import requests
import json

# to store the url for the api for weather forecast for Galway 
url = "https://api.open-meteo.com/v1/forecast?latitude=53.270668&longitude=-9.056790&current=temperature_2m,wind_direction_10m"
# to retrieve the dataset from the url above and convert it to json format
response = requests.get(url)
data = response.json()


currentObject = data["current"]
current_temp = currentObject["temperature_2m"]
current_wind = currentObject["wind_direction_10m"]
print("Current temperature = ",current_temp,"°C", sep = "")
print("Current wind direction = ",current_wind,"°", sep = "") 