''' This is an example code for python lists, strings and methods
    Repetitions structures, loops and conditions. Tutorial description.
    Code sequence based on Calico UFSC python minicourse - class 2
    
    Dependencies
    Python 3.5.x (64bit)
    numpy
    Developer: Gustavo S.
    Date: June-2017
    References: https://github.com/CalicoUFSC/minicurso-python
'''

import numpy as np

##  LISTS   and     STRINGS ##

## Creates a list
lista1 = []

## Inserts elements in the list
lista1.append("x")
lista1.append("y")
lista1.append('z')

print("List is:", lista1)

## Removes 'x' element from the list
lista1.remove('x')

print("List with 'x' removed is:", lista1)

#inserts 'x' element again at the end of the list
lista1.append('x')

print("List with 'x' inserted is:", lista1)

# removes the element with index '1' (starting index = 0)
lista1.pop(1)

print("List with index 1 elemen removed is:", lista1)

# creates a new list having a list as an element
lista2 = [lista1, 'x', 'x', 'z', 'x', 'y']

# prints last element of the list
print("Last element of new list is:", lista2.pop(len(lista2)-1))

# prints the index of the first occurence of 'x'
print("First index of 'x' is:",lista2.index('x'))

# created a string
palavra = "agora"

#print string created
print("Word is:", palavra)

# removes char 'a' from string
print(palavra.strip('a'))

#test if string endswith 'a'
print(palavra.endswith('a'))

# creates a list from string
lista3 = list(palavra)
print(lista3)

##  LOOPS   and     ITERATIONS  ##

# for-loop that prints chars on list
for element in lista3:
    print(element)

## for-loop that prints i squared from 0 to 4 (integers)
for i in range(5):
    print(i**2)

## for-loop that prints i squared from 0 to 4 (step = 2; not valid for float) 
for i in range(0, 5, 2):
    print(i**2)

# enumerate function returns a tuple with element and index
string = 'python'
for index, char in enumerate(string):
	print(index, char)

# joins 'lista1' string with list elements
for c1 in lista1:
    print(c1 + ' lista1')

print(np.linspace(1,10,4))