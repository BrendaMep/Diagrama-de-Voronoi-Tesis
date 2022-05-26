import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np


datos = pd.read_csv('C:/Users/Home/Documents/TESIS DIAGRAMA DE VORONOI/Diagrama-de-Voronoi-Tesis/'
                   'iris.data',header= None)
#print(datos.head())

df= pd.DataFrame(datos)

#elimino columnas
df = df.drop(df.columns[[2, 3,4]], axis='columns')

plt.scatter(df[0], df[1],marker=".")
vor = Voronoi(df)
voronoi_plot_2d(vor)
plt.show()