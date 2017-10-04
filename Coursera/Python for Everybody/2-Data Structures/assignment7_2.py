## Python for Everybody Coursera
## Assignment 6_5
## Gustavo Simas da Silva - 2017
## Python Data Structures, String Manipulation, File handling

# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
result = 0
n = 0
for line in fh:
    line = line.rstrip()
    if 'X-DSPAM-Confidence:' in line:
        index = line.find(':')
        result = result + float(line[index+1:])
        n = n + 1
value = result/n
print("Average spam confidence:",value)