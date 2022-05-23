#
# please refer to PPT file
# for exercise
#

from math import e
import matplotlib.pyplot as plt

print("Resolver usando uno de los métodos a elegir e^(2-x) -7x = 0")

#Respuesta: x=0.586934

# Método elegido: Sustitución sucesiva

def met_ss(x):
     f = -e**(2-x)/(-7)
     return f
#end

# Solución: se encontró la raíz hasta la iteración 25

ult_ite = float(0)
fx = [0]

for vez in range(1,26):
    ult_ite = met_ss(ult_ite)
    fx.append(ult_ite)

# Resultado
        
print ("Raíz:", ult_ite)

# Graficación

plt.plot(fx)