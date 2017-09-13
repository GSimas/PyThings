## Python for Everybody Coursera
## Assignment 13
## Gustavo Simas da Silva - 2017
## Python Web Data, XML Parsing, XSD

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

res = 0
url = input("Enter URL: ")

while True:
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    for value in counts:
        res = res + int(value.text)
    print(res)
    break