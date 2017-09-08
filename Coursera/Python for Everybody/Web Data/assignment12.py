## Python for Everybody Coursera
## Web Data - Assignment 12 (Week 4)
## Gustavo Simas da Silva - 2017
## Parsing Web Pages, BeautifulSoup4, Urllib

#Program to count sum of all numbers on table in html page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #enter: http://py4e-data.dr-chuck.net/comments_42.html
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
count = 0
tags = soup('span')

for tag in tags:
    count += int(tag.contents[0])

print(count)