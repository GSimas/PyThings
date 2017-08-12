## Python for Everybody Coursera
## Assignment 8_4
## Gustavo Simas da Silva - 2017
## Python Data Structures, Lists and String Manipulation

#use romeo.txt as filename
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    splt = line.split()
    for word in splt:
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)
