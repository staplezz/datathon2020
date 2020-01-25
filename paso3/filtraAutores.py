import pandas as pd

'''
Parte 3 del proyecto de Datathon.
-En esta parte nos encargamos de unir los autores sin repetir
y que tengan más de tres autorías con los id de los artículos.
'''

#Archivo csv del catálogo de autores.
unfiltered_authorships = pd.read_csv('nodes_catalogue.csv')
#Archivo csv del catálogo de autores con sus ids.
authorships = pd.read_csv('authorships.csv')
#Unimos los autores y su id con el catálogo de autores.
filtered_autorships = pd.merge(authorships, unfiltered_authorships, on = 'author', how = 'left')
#Creamos el archivo csv filtrado.
filtered_autorships.to_csv("filtered_authorships.csv", encoding='utf-8', index=False)
