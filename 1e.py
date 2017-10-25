import math
h = [0.1,0.01,0.0011,0.0001,0.00001]
x0= 1.8
for z in h:
    fder = (1/(2*z))*(-3*math.log(x0)+4*math.log(x0+z)-math.log(x0+z)-math.log(x0+2*z))+((z**2)/3)*(2/(((x0+2*z)-x0)**3))
    print(" usando h= "+str(z))
    print("fder ="+str(fder))
