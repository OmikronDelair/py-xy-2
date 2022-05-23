#
# please refer to PPT file
# for exercise
#

# Integración numérica

#
import math
from math import sin

# OPERACION 1

def f(x):
    return ((2*sin(math.sqrt(x)))-x)

a=0
b=1.9724

# Regla del Rectángulo
r1=f(a)*(b-a)

print('Regla del rectángulo I=',r1)


# Regla del Punto medio

m=(a+b)/2
r2=f(m)*(b-a)

print('Regla del punto medio I=',r2)

#Regla del Trapecio

r3=((b-a)/2)*(f(a)+f(b))

print('Regla del trapecio I=',r3)

# Regla de Simpson

m=(a+b)/2
r4=((b-a)/6)*(f(a)+4*f(m)+f(b))

print('Regla de Simpson I=',r4,'\n')

# OPERACION 2

def f(x):
    return ((7**(-x))+3)

a=2
b=-1

# Regla del Rectángulo
r1=f(a)*(b-a)

print('Regla del rectángulo I=',r1)


# Regla del Punto medio

m=(a+b)/2
r2=f(m)*(b-a)

print('Regla del punto medio I=',r2)

#Regla del Trapecio

r3=((b-a)/2)*(f(a)+f(b))

print('Regla del trapecio I=',r3)

# Regla de Simpson

m=(a+b)/2
r4=((b-a)/6)*(f(a)+4*f(m)+f(b))

print('Regla de Simpson I=',r4)