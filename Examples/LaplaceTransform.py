import numpy as np
from sympy import *

s,t = symbols("s,t")
w = symbols('w', real=True)
expression = 1/(1 + np.exp(-1))
print(expression)

expression = exp(-t)
r = laplace_transform(expression,t,s)
res = inverse_laplace_transform(1/(1 + s),s,t)
print(res)