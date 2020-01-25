import numpy as np
import pandas as pd
import io
import networkx as nx
import matplotlib.pyplot as plt

#Leémos la gráficas del catálogo de aristas.
df=pd.read_csv('edges.csv')
tuples = [tuple(x) for x in df.to_numpy()]
#Creamos la gráfica.
G = nx.Graph()
G.add_edges_from(tuples)

#Función auxiliar que nos ayuda a obtener las subgráficas conexas de la gráfica.
#Regresa una lista de gráficas conexas.
def connected_component_subgraphs(G):
    subgraphs_connected = []
    for c in nx.connected_components(G):
        subgraphs_connected.append(G.subgraph(c))

    return subgraphs_connected

#TEST.
#Subgráfica monstruo
testGraph = subg[0]

#Camino más corto entre dos nodos.
shortest_path = nx.shortest_path(testGraph, source='Hassan Bezzazi', target='Randall L. Geiger') 

#Aquí crearíamos la subgráfica más completa entre dos nodos.
subgraf = testGraph.subgraph(shortest_path)

#Mostramos en pantalla.
nx.draw(subgraf, with_labels=True)
plt.show()
