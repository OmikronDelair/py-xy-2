#
# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

# Distribucion elegida: Binomial

import numpy as np
import matplotlib.pyplot as plt

# Se haran 100 pruebas de 10 intentos cada una para un volado

n = 10 # Número de intentos
p = .5 # Probabilidad de cada intento

resultados = np.random.binomial(n, p, 100)

for index, intento in enumerate(resultados):
    print ("En la prueba", index, "hubo", intento, "volado(s) exitoso(s)")