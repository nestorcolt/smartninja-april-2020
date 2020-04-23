from urllib.request import urlopen
from pprint import pprint
import json

"""
RESOURCES 
Web scraping:
https://realpython.com/beautiful-soup-web-scraper-python/
"""

##############################################################################################
# reading a .json file

with open("people.json") as file:
    data = json.load(file)

for dictionary in data:
    for key, val in dictionary.items():
        # print(key, val)
        pass

##############################################################################################

# Query an API Getting the weather from my city
api_key = "f57f78b88df782edef2d267985a11166"  # insert your own API key!!!
city = "Barcelona,es"
units = "metric"
link_to_query = r"http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(city, units, api_key)

# Making an API call
print(link_to_query)
response = urlopen(link_to_query).read()
data = json.loads(response)

# custom weather message
weather_message = \
    """
        City: {}
        Temperature: {}
        feels like {}
        weather: {}
    """.format(data["name"], data["main"]["temp"], data["main"]["feels_like"], data["weather"][0]["description"])

# output
print(weather_message)

##############################################################################################
