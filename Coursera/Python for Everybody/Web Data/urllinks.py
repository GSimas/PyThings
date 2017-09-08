## Python for Everybody Coursera
## Web Data
## Gustavo Simas da Silva - 2017
## Parsing Web Pages, BeautifulSoup4

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input('Enter: ')
url = Request(inp, headers={'User-Agent': 'Chrome/56.0.2924.87'})
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))