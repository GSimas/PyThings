## Python for Everybody Coursera
## Assignment 5_2
## Gustavo Simas da Silva - 2017

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
	    break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    if largest == None:
        largest = number
    if number > largest:
        largest = number
    if smallest == None:
        smallest = number
    if number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)