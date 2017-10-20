import math
h = [0.1,0.01,0.0011,0.0001,0.00001]
x0= 1.8
for z in h:
    fder = (1/(12*z))*(math.log(x0-2*z)-8*math.log(x0-z)+8*math.log(x0+z)-math.log(x0+2*z))
    print(" usando h= ")
    print(z)
    print(fder)
