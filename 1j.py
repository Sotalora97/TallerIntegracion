from math import *
import matplotlib.pyplot as plt
import numpy as np
def f(x):return x*exp(x)
r=5.436563656918091
h=0.1
vh=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0]
ve=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0]
for i in range(15):
    d=(f(1+h)-f(1))/h
    e=abs(r-d)
    print('%18.15f %18.15f %18.15f %18.15f'%(h,r,d,e))
    vh.insert(i,h)
    ve.insert(i,e)
    h=h/10

print(vh)
print(ve)
plt.plot(vh,ve)
plt.plot(vh,ve,'o')
plt.show()
