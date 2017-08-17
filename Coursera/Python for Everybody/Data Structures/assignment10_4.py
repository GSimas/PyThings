## Python for Everybody Coursera
## Assignment 10_4
## Gustavo Simas da Silva - 2017
## Python Data Structures, Dictionaries and Tuples

#use mbox-short.txt as filename
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

hours = list()

for line in handle:
    if 'From ' in line:
        words = line.split()
        hours.append((words[5].split(':'))[0])

count = dict()
for hour in hours:
    count[hour] = count.get(hour,0) + 1

tmp = list()
tmp = sorted([(k,v) for (k,v) in count.items()])

for k,v in tmp:
    print(k,v)

        
