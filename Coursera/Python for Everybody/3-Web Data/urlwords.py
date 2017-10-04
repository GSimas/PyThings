## Python for Everybody Coursera
## Web Data
## Gustavo Simas da Silva - 2017
## Retrieving Web Pages, Unicode, UTF-8, urllib, request, parsing, system time

import time
import urllib.request, urllib.parse, urllib.error
import re

# PART 1 - retrieve text from website

tic = time.time()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()
    print(line.decode().strip() + '\n')
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

## PART 2 - retrieve url from website

fhand2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

m = list()

for line in fhand2:
    words = line.decode().split()
    if(len(m) == 0):
        m = [re.findall('\"(http.+htm|html|)\"',word) for word in words if 'href' in word]

url = m[0][0]
print('\n' + "URL detected: " + url)

# PART 3 - print website

fhand3 = urllib.request.urlopen(url)

for line in fhand3:
    print(line.decode().strip())
toc = time.time()
print("Time: ", toc - tic, 's')