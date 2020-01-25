# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:32:40 2020

@author: ilian
"""
import numpy as np
import pandas as pd
import io
import networkx as nx

df=pd.read_csv('edges.csv')
tuples = [tuple(x) for x in df.to_numpy()]
G = nx.Graph()
G.add_edges_from(tuples)
print(G)
