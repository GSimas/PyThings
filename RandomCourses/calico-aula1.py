''' This is an assignment code for basic python variables input/print
    Logical and arithmetic operations, functions, control structures
    Code sequence based on Calico UFSC python minicourse - class 1
    
    Dependencies
    Python 3.5.x (64bit)
    Developer: Gustavo S.
    Date: June-2017
    References: https://github.com/CalicoUFSC/minicurso-python
'''

# 1) Write a function named 'factorial' that receives 'n' and returns n!
def factorial(num):
    x = 1
    if num == 0:
        return 1
    for i in range(1,num+1):
        x *= i
    return x

print("Factorial of 5 is: ",factorial(5))
print("Factorial of 1 is: ",factorial(1))
print("Factorial of 0 is: ",factorial(0))

#or...

def fact(num):
    if num == 0:
        return 1
    
    elif num < 0:
        return "Value is not valid"

    else:
        x = num * fact(num-1)
    return x

print("Factorial (recursive) of 6 is: ",fact(6))
print("Factorial (recursive) of 0 is: ",fact(0))
print("Factorial (recursive) of -4 is: ",fact(-4))

# 2) Write a Fibonacci series function
def fibonacci(num):
    x, y = 0, 1
    if num < 0:
        return None
    if num == 0:
        return 0
    if num == 1:
        return 1
    for i in range(1,num+1):
        l = x + y
        y, x = l, y
    return l

print("Fibonacci of 5 is: ", fibonacci(5))
print("Fibonacci of 0 is: ", fibonacci(0))
print("Fibonacci of -2 is: ", fibonacci(-2))


# 3) Write an Euclides Algorithm function (maximum common divisor)
def mcd(a,b):
    max = 0
    if a >= b:
        for i in range(1,a+1):
            if a % i == 0 and b % i == 0:
                max = i
    if a < b:
        for i in range(1,b+1):
            if a % i == 0 and b % i == 0:
                max = i
    return max

print ("Maximum commond divisor of 10 and 5 is: ", mcd(10, 5))
print ("Maximum commond divisor of 17 and -2 is: ", mcd(17, -2))  
print ("Maximum commond divisor of 20 and 2 is: ", mcd(20, 2))

# 4) Check if a number is prime
def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

print("Check if 10 is prime: ", is_prime(10))
print("Check if 383 is prime: ", is_prime(383))
print("Check if -7 is prime: ", is_prime(10))