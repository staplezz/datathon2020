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
def adamic_Adar(autor1, autor2, listaGraficas, graficaAutores):
    #Primero verificamos si podemos llegar desde el autor 1 al autor 2.
    if not nx.has_path(graficaAutores, autor1, autor2):
        return False

    #buscamos la subgráfica en la lista de gráficas
    G = buscaGrafica(listaGraficas, autor1)

    #Obtenemos la subgráfica inducida.
    induced_subgraph = encuentraSubGrafica(autor1, autor2, G)

    #Realizamos los puntajes
    puntajes = list(nx.adamic_adar_index(induced_subgraph))

    #Si la lista de puntajes es vacía quiere decir que ya existe una arista.
    if not puntajes:
        return True

    #Ordenamos los puntajes de mayor a menor.
    puntajes.sort(key=operator.itemgetter(2), reverse = True)

    #Obtenemos el puntaje más alto.
    puntaje_maximo = puntajes[0][2]

    #Buscamos el puntaje de la arista que queremos predecir.
    for puntaje in puntajes:
        if puntaje[0] in [autor1, autor2] and puntaje[1] in [autor1, autor2]:
            puntaje_prediccion = puntaje[2]
    print(puntajes)
    print(puntaje_prediccion)

    #Vemos si existe probabilidad de que exisa la arista con base al puntaje máximo.
    #Por defecto tomamos un 60% de rango del puntaje máximo.
    if puntaje_prediccion >= puntaje_maximo * 0.40:
        return True
    else:
        return False

#Leémos el catálogo de aristas y lo convertimos a una gráfica de networkx.
catalogo_aristas = pd.read_csv('edges.csv')
aristas = [tuple(x) for x in catalogo_aristas.to_numpy()]
graficaAutores = nx.Graph()
graficaAutores.add_edges_from(aristas)

#Obtenemos las subgráficas.
connected_components = connected_component_subgraphs(graficaAutores)

#Aplicación del primer modelo de predicción.
print(adamic_Adar('Sanjay Jain 0001','A. David Marshall', connected_components, graficaAutores))
