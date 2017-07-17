## Python for Everybody Coursera
## Assignment 3_1
## Gustavo Simas da Silva - 2017

hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
try:
	h = float(hrs)
	r = float(rate)
except:
    print("Not a number")
    quit()
if h > 40:
    pay = 40*r
    pay = pay + (h-40)*1.5*r
else:
	pay = h*r
print(pay)