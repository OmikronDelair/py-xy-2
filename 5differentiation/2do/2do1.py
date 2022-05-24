#
# please refer to PPT file
# for exercise
#

#Dado f(x)=(sen^(3)2x)/(x^(4)+1) obtener f(2.45)

from math import sin

def f(x):
    return ((sin(2*x)**(3))/((x**(4)))+1)

# Diferencias finitas progresivas

print("Método: Diferencias finitas progresivas\n")

x0 = 2.45

h1 = 0.5
r1 = (f(x0+h1)-f(x0))/h1
print('r1 =',r1)

h2 = 0.3
r2 = (f(x0+h2)-f(x0))/h2
print('r2 =', r2)

h3 = 0.1
r3 = (f(x0+h3)-f(x0))/h3
print('r3 =', r3)

h4 = 0.00001
r4 = (f(x0+h4)-f(x0))/h4
print('r4 =',r4)

h5 = 0.00000001
r5 = (f(x0+h5)-f(x0))/h5
print('r5 =',r5)