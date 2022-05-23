#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#

# Lanzar 10mil tiradas y contar cuantas son aguila y cuantos son sello

def volado():
    tiradas = [random.randint(1,2) for i in range(10000)]
    cara = tiradas.count(1)
    sello = tiradas.count(2)
    
    print ("Cara: ", cara, "Sello:", sello)
    
volado()
