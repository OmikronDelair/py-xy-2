#
# select a distribution from random
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

# Distribucion elegida: Uniform

import random 

# Valor probable de un corte de madera con un largo deseado de 30
# al cortarse con sierra de banco

valor_corte = random.uniform(29.7, 30)

print ("El corte resultante fue de", valor_corte, "cm")