## Python for Everybody Coursera
## Assignment 6_5
## Gustavo Simas da Silva - 2017
## Python Data Structures, String Manipulation, File handling

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())