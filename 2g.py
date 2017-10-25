from sympy import *
import math

x = Symbol('x')

expr=4+cos(x+1)
expr2=exp(x)*sin(x)

def trapecios(f,a,b,m):
    h=(b-a)/m
    s=0
    for i in range(1,m):
        s=s+f.evalf(a+i*h)
    #print("s="+str(s))
    r=(h/2)*(f.evalf(a)+(2*s)+f.evalf(b))
    #print("r="+str(r))
    return r

y=trapecios(expr,1.2615,2.9703,10)
z=trapecios(expr2,1.2615,2.9703,10)
a=y-z
print(a)
