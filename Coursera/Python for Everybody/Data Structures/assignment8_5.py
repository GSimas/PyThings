## Python for Everybody Coursera
## Assignment 8_5
## Gustavo Simas da Silva - 2017
## Python Data Structures, Lists and String Manipulation

#use mbox-short.txt as filename
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line.lstrip()
    splt = line.split()
    if len(splt) > 1 and splt[0] == 'From':
        print(splt[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")