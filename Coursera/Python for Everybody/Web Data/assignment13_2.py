## Python for Everybody Coursera
## Assignment 13_json
## Gustavo Simas da Silva - 2017
## JSON files, urllib, parsing web pages, api

import json
import urllib.request, urllib.parse, urllib.error

#use http://py4e-data.dr-chuck.net/comments_9022.json as url

count = 0

url = input("Enter url: ")
uh = urllib.request.urlopen(url)
data = uh.read().decode()

try:
    js = json.loads(data)
    print("JSON loaded")
except:
    js = None
    print('==== Failure To Retrieve ====')

print(data)

for item in js['comments']:
    count += int(item['count'])

print(count)