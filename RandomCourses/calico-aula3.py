''' This is an assignment code for basic python lists comprehensions, generators, callbacks
    Code sequence based on Calico UFSC python minicourse - class 3
    
    Dependencies
    Python 3.5.x (64bit)
    Developer: Gustavo S.
    Date: July-2017
    References: https://github.com/CalicoUFSC/minicurso-python
'''

import numpy as np

# List Comprehension

#Normal Example
squares = []
for i in range(10):
    squares.append(i**2)

print("Normal example is:", squares)

#Optimized example
squares = [i**2 for i in range(10)]
print("Optimized example is:", squares)

# 1) Map function
# receives a function and list ( [x1, x2, ..., xn]), returns list ([func(x1), func(x2), ..., func(xn)])

def map(function, lista):
    result = [function(lista[i]) for i in range(len(lista))]
    return result

o = map(print, ['a','b','d'])

# 2) Zip function




# 3) Fib_gen function
# fibonacci numbers through generator

# 4) Add by

def add_by(x):
    def func(y):
        return x+y
    return func

increment = add_by(1)
print("Increment of 3:", increment(3))
print("Increment of 10:", increment(10))

# 5) Function n times

def apply(f, n):
	def func(x):
		h = f(x)
		for _ in range(n-1):
			h = f(h)
		return h
	return func

def sum(x):
    x+=1
    return x

yah = apply(sum, 5)
print("Applied function (closure):", yah(5))