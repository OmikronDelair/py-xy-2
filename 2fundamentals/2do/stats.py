import numpy as np 
from scipy import stats 

lst = np.array([1,2,3,4,5,6,7,8,9,10])
lst_2 = np.array([11,12,13,14,15,16,17,18,19,20])

#
# select and write 
# one of the following stat functions
#

# Funciones

def lst_sum(l):
    print ("Sumatoria:", np.sum(l))

def lst_avg(l):
    print ("Promedio:", np.average(l))

def lst_min(l):
    print ("Valor mínimo:", np.min(l))

def lst_max(l):
    print ("Valor máximo:", np.max(l))

def lst_range(minv,maxv,step):
    print ("Valores de funcion arange", np.arange(minv,maxv,step))

def lst_std(l1,l2):
    array = np.array([l1,l2])
    print ("Desviación estándar de valores:", np.std(array))

def lst_mode(l1,l2):
    array = np.array([l1,l2])
    mode = stats.mode(array)
    print ("Moda:", mode[0])

# Ejecución

print (type(lst))
lst_sum(lst)
lst_avg(lst)
lst_min(lst)
lst_max(lst)
lst_range(0,10.1,0.1)
lst_std(lst,lst_2)
lst_mode(lst,lst_2)