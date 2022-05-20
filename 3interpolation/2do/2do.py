#
# please refer to PPT file
# for exercise
#
import sympy as sym
from sympy import *


print("1. Dados: (-4, -2) y (1, 5) estimar el valor para x cuando y = 3.7")

# Función de interpolación lineal para encontrar X
def int_lineal_x(x0,y0,x1,y1,y):
    x = (((x1-x0)*(y-y0))/(y1-y0))+x0
    print("\nEl resultado es:\nx = " + str(x) + "\n")
#end

int_lineal_x(-4,-2,1,5,3.7)

print("2. Dados: (-2, 4), (-1, -2), (3, 5) y (4.3, 11) estimar el valor para x cuando y = 7.7")

# Función de interpolación de Lagrange de tercer grado
def int_lagrange_y_g3(x0,y0,x1,y1,x2,y2,x3,y3,x):
    l0 = ((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    l1 = ((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    l2 = ((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    l3 = ((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    
    y = ((y0)*(l0))+((y1)*(l1))+((y2)*(l2))+((y3)*(l3))
    print("\nEl resultado por interpolación de Lagrange es:\nx = " + str(y) + "\n")
#end

int_lagrange_y_g3(-2,4,-1,-2,3,5,4.3,11,7.7)

print("3. Dados: (-1, 3), (0, -7), (4, 7) y (5, 11) estimar el polinomio interpolante")

# Función de polinomio interpolante de Newton
def int_newton(x0,y0,x1,y1,x2,y2,x3,y3):
    x = sym.Symbol('x')
    
    b1 = (y1-y0)/(x1-x0)
    b2 = (((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)
    b3 = (((((y3-y2)/(x3-x2))-((y2-y1)/(x2-x1)))/(x3-x1))-((((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)))/(x3-x0)
    
    y = y0 + (b1*(x-x0)) + (b2*(x-x0)*(x-x1)) + (b3*(x-x0)*(x-x1)*(x-x2))
    print("\nEl polinomio interpolante de Newton es:\ny = " + str(simplify(y)) + "\n")
#end

int_newton(-1,3,0,-7,4,7,5,11)