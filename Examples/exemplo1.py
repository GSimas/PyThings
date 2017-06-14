#  -*- coding: utf-8 -*-

'''import requests

response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print(response.text)
print(type(response.text))'''

import matplotlib.pyplot as plt
import numpy as np
from Calculator import Calc
from user import User
from user import Pessoa

#Cria e salva usuarios classe User
eu = User('Gustavo', 20)
eu.save()
tu = User("Ronaldo",32)
tu.save()
print(User.all()) #printa usuarios

#Cria e salva usuarios classe Pessoa
nos = Pessoa('Todos', (1,5,1997))
print(nos.idade((1,4,2017)))

#Converte binario em int
xbit = 0b100
xint = str(xbit)
print(xint)

#Cria variavel de Calculadora
c = Calc(16,2)
print("Soma de {} e {}:".format(c.a, c.b), c.sum())
print("Subtracao de {} e {}:".format(c.a, c.b), c.sub())
print("Divisao de {} e {}:".format(c.a, c.b), c.div())
print("Multiplicacao de {} e {}:".format(c.a, c.b), c.mul())
print("Elevacao de {} na {}:".format(c.a, c.b), c.exp())
print("Raiz #{} de {}:".format(c.b, c.a), c.sqr())

#Sequencia de Fibonacci
def fib(numero, x):
    num = [0,1]
    for i in range(numero):
        print(num)
        num.append(num[i] + num[i+1])
    x = num
    return x

y = []
fib(15,y)
'''
#Plotar Matplotlib
V = 0.08
xmin,xmax,ymin,ymax = 0,1,0,1
xx1 = np.linspace(xmin,xmax)
xx2 = np.linspace(ymin,ymax)
x1, x2 = np.meshgrid(xx1, xx2)
f = 2*(V/x2) + 2*(V/x1) + x1*x2
g1 = (V/(x1*x2)) - 0.6
g2 = (V/(x1*x2)) - 0.8
g3 = x1 - 0.1
g4 = x2 - 0.1
plt.contour(x1, x2, f, cmap="viridis")
#plt.show()'''

