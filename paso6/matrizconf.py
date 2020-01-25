import numpy as np
import pandas as pd
import io
import networkx as nx
import matplotlib.pyplot as plt
import operator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

dfResultadoAlgoritmo=pd.read_csv('resultadoAlgoritmo.csv').set_index(['source','target'])
dfResultadoPropuesto=pd.read_csv('resultadoPropuesto.csv').set_index(['source','target'])

#fp,fn,vp,vn=0

df = pd.merge(dfResultadoAlgoritmo, dfResultadoPropuesto, left_index=True, right_index=True)

actual = df['prediction_x']
predicted = df['prediction_y']

results = confusion_matrix(actual,predicted)

print(results)
print(accuracy_score(actual,predicted))
print(classification_report(actual,predicted))


