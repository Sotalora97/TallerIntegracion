from sympy import *
import math
import sys
sys.displayhook = pprint
x = Symbol('x')
z=integrate(1/(1+x**2)**3,(x,1,float("inf")))
y=integrate(sin(x)/x,(x,0,1))
print(float(z))
print(float(y))
