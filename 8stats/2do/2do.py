#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
#

import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

# Lista

print (iris)

list_sepall = iris['sepal length'].tolist()
print('Sepal Length (Column List)\n')
print(list_sepall)
print("\n{}\n".format(type(list_sepall)))

# Diccionario
dic_sepalw = iris['sepal length'].to_dict()

print('Sepal Width (Column Dictionary)\n')
print(dic_sepalw)
print("\n{}\n".format(type(dic_sepalw)))

# Tupla

tup_petall = tuple(iris['petal length'].tolist())

print('Petal Length (Column Tuple)\n')
print(tup_petall)
print("\n{}\n".format(type(tup_petall)))