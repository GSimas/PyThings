''' This is an assignment code for basic python lists, strings, repetition structures
    Logical and arithmetic operations, functions, control and repetition structures
    Code sequence based on Calico UFSC python minicourse - class 2
    
    Dependencies
    Python 3.5.x (64bit)
    Developer: Gustavo S.
    Date: June-2017
    References: https://github.com/CalicoUFSC/minicurso-python
'''

import numpy as np

# 1) Who likes - Facebook
def likes(lista):
    x = len(lista)
    if x == 0:
        return "Ninguem curtiu isso"
    elif x == 1:
        return lista[0] + " curtiu isso"
    elif x == 2:
        return  lista[0] + " e " + lista[1] + " curtiram isso"
    elif x == 3:
        return lista[0] + ", " + lista[1] + " e " + lista[2] + " curtiram isso"
    elif x >= 4:
        return lista[0] + " e " + lista[1] + " e {} outros curtiram isso".format(x-2)

test = ["Joao", "Pablo", "Guilherme", "Mateus", "Juan"]
print(likes(test))

# 2) Detect domain name by URL
def domain_name(url):
    y = url.split("://")
    if y[1].count("www") > 0:
        x = y[1].split(".")
        return x[1]
    else:   
        z = y[1].split(".")
        return z[0]

print(domain_name("http://github.com/calicoufsc/minicurso-python"))
print(domain_name("http://www.facebook.com"))
print(domain_name("https://ufsc.br"))

# 3) Remove duplicate elements on a list
def remove_duplicates(x): #not valid for non-alphanumeric characters
    i = 0
    
    while i < len(x):
        if x.count(x[0]) > 1:
            x.remove(x[0])
            i = 0
        else:
            i += 1
    return x

print(remove_duplicates([1,2,1,3,1,2]))
print(remove_duplicates([5,4,3,2,1,2,3,4,5]))

#or...

def remove_duplicates2(arr):
	for e in arr:
		while arr.count(e) > 1:
			arr.remove(e)
	return arr


# 4) Detect index of element with different eveness
def different_evenness(strg): #not valid for n > 10

    lista = list(strg)
    even = 0
    odd = 0
    index = 0

    while lista.count(' ') > 0:
        lista.remove(' ')

    for i in range(len(lista)):
        if int(lista[i]) % 2 == 0:
            even += 1
        else:
            odd += 1

    if even >= odd:
        for i in range(len(lista)):
            if int(lista[i]) % 2 != 0:
                return i

    elif odd > even:
        for i in range(len(lista)):
            if int(lista[i]) % 2 == 0:
                return i
                

print(different_evenness("2 1 8"))
print(different_evenness("7 1 3 2 9 1"))
print(different_evenness("11 3 0 19 1"))

#or...

def different_evenness2(s):
    n = [int(i) % 2 for i in s.split()]
    if n.count(0)>1:
        return n.index(1)
    else:
        return n.index(0)

print(different_evenness2("2 1 8"))
print(different_evenness2("7 1 3 2 9 1"))
print(different_evenness2("11 3 0 19 1"))