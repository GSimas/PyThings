## Python for Everybody Coursera
## Assignment 3_3
## Gustavo Simas da Silva - 2017

score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Error. Enter a valid number between 0.0 and 1.0")
    quit()
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")