from random import seed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


X = [2 , -4, -8, -1, 3]
Y = [4,4 ,-3 ,1,-1]
df = np.array([[2,4], [-4,4],[-8,-3],[-1,1],[3,-1]])
plt.scatter(X, Y,marker=".")
vor = Voronoi(df)
voronoi_plot_2d(vor)
plt.show()



