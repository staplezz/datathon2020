import pandas as pd
import itertools

'''
Parte 4: Construcción de las aristas usando el catálogo
de autores filtrados.
'''

#Importamos el catálogo de autores.
filtered_authorships = pd.read_csv('filtered_authorships.csv')

#Diccionario para ir guardando los autores de cada artículo.
article_dict = dict()

#Guardamos los datos del catálogo en el diccionario.
for index, row in filtered_authorships.iterrows():
    article_dict.setdefault(row['id_article'], []).append(row['author'])

#Conjunto de aristas de los autores que han colaborado juntos.
aristas = set()
for key, item in article_dict.items():
    #Combinaciones de autores que han trabajado juntos.
    combinaciones = itertools.combinations(item, 2)
    for tupla in combinaciones:
        aristas.add(tupla)

#Quitamos los autores duplicados.
aristas = {frozenset(autor) for autor in aristas}

#Convertimos a lista de tuplas.
aristas = [tuple(i) for i in aristas]

#Filtramos tuplas con longitud menor a 2.
aristas = [i for i in aristas if len(i) == 2]

#Convertimos a dataframe
aristas = pd.DataFrame(aristas, columns=['source', 'target'])

#Creamos el csv de aristas.
aristas.to_csv("edges.csv", encoding='utf-8', index=False)
