import pandas as pd
import networkx as nx
import operator
import matplotlib.pyplot as plt

'''
Paso 5: En este archivo se harán diversos modelos de predicción
de aristas usando el catálogo de aristas que obtuvimos en el paso
4.
'''

#Función auxiliar que nos ayuda a obtener las subgráficas
#conexas del catálogo de aristas.
def connected_component_subgraphs(G):
    subgraphs_connected = []
    for c in nx.connected_components(G):
        subgraphs_connected.append(G.subgraph(c))

    return subgraphs_connected

#Función auxiliar que nos ayuda a encontrar una subgráfica entre dos
#nodos usando los caminos más cortos entre ellos.
def encuentraSubGrafica(autor1, autor2, G):
    #Caminos más cortos entre dos autores.
    shortest_path = nx.all_shortest_paths(G, source=autor1, target=autor2)
    #En donde guardamos los vértices.
    nodos_path = set()

    #Los agregamos usando el camino más corto
    for path in shortest_path:
        for author in path:
            nodos_path.add(author)

    #Obtenemos la subgráfica inducida        
    induced_subg = nx.induced_subgraph(G, list(nodos_path))

    return induced_subg

#Función auxiliar que nos ayuda a buscar a un autor dentro de la lista
#de gráficas.
def buscaGrafica(listaGraf, autor):
    for grafica in listaGraf:
        if grafica.has_node(autor):
            return grafica
    return None

'''
Modelo de predicción 1:
Usando la subgráfica inducida por caminos más cortos entre dos vértices
aplicaremos el algorítmo de predicción Adamic-Adar y regresaremos el
puntaje obtenido de ambos autores en una gráfica o subgráfica.
'''
def adamic_Adar(autor1, autor2, listaGraficas):
    #buscamos la subgráfica en la lista de gráficas
    G = buscaGrafica(listaGraficas, autor1)

    #Obtenemos la subgráfica inducida.
    induced_subgraph = encuentraSubGrafica(autor1, autor2, G)

    #Realizamos los puntajes
    puntajes = list(nx.adamic_adar_index(induced_subgraph))

    for puntaje in puntajes:
        if puntaje[0] == autor1 and puntaje[1] == autor2:
            return puntaje[2]

    #Si no lo encontramos quiere decir que ya está la arista.
    return 0

#Leémos el catálogo de aristas y lo convertimos a una gráfica de networkx.
catalogo_aristas = pd.read_csv('edges.csv')
aristas = [tuple(x) for x in catalogo_aristas.to_numpy()]
graficaAutores = nx.Graph()
graficaAutores.add_edges_from(aristas)

#Obtenemos las subgráficas.
connected_components = connected_component_subgraphs(graficaAutores)

#Aplicación del primer modelo de predicción.
print(adamic_Adar('Ronald M. Lee', 'Richard C. T. Lee', connected_components))

#nx.draw(connected_components[0], with_labels=True)
#plt.show()
