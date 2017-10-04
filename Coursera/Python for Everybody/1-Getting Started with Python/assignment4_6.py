## Python for Everybody Coursera
## Assignment 4_6
## Gustavo Simas da Silva - 2017

def computepay(h,r):
    if h > 40:
        pay = 40*r
        pay = pay + (h-40)*1.5*r
        return pay
    else:
    	pay = r*h
    	return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
	print("Enter valid values")
	quit()
p = computepay(hrs, rate)
print(p)