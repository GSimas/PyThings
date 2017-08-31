## Python for Everybody Coursera
## Assignment 11_1
## Gustavo Simas da Silva - 2017
## Python Acessing Web Data - Regular Expressions

import re

print(sum(int(x) for x in (re.findall('[0-9]+',open("regex_sum_9017.txt").read()))))

'''
Or, alternatively...

fh = open("regex_sum_9017.txt")

for line in fh:
    x = re.findall('[0-9]+',line)
    if len(x) != 0:
        for num in x:
            soma = soma + int(num)
            
print(soma)
'''