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
#Obtenemos las subgráficas.
subg = connected_component_subgraphs(G)
#Dibujamos una subgráfica aleatoria.
nx.draw(subg[1],with_labels=True)
plt.show()
