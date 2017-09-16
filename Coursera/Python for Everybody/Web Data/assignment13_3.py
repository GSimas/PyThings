## Python for Everybody Coursera
## Assignment 13_json
## Gustavo Simas da Silva - 2017
## JSON files, urllib, parsing web pages, api, geo

import json
import urllib.request, urllib.parse, urllib.error

api_url = "http://py4e-data.dr-chuck.net/geojson?"

address = input('Enter address: ')

if len(address) < 1:
    print("Wrong adress") 

url = api_url + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')

location = js['results'][0]['formatted_address']
place_id = js['results'][0]['place_id']
print("Location: ",location)
print("Place ID: ",place_id)
