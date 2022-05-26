import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np


datos = pd.read_csv('C:/Users/Home/Documents/TESIS DIAGRAMA DE VORONOI/Diagrama-de-Voronoi-Tesis/'
                   'Ejemplo.data')
#print(datos.head())

df= pd.DataFrame(datos)

#elimino columnas
df = df.drop(df.columns[[2]], axis='columns')

plt.scatter(df.X, df.Y,marker=".")
vor = Voronoi(df)
voronoi_plot_2d(vor)
plt.show()