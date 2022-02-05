from random import seed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

seed(89)
df = pd.DataFrame(np.random.uniform(1,100,size=(30, 2)), columns=list('XY'))
plt.scatter(df.X, df.Y,marker=".")
vor = Voronoi(df)
voronoi_plot_2d(vor)
#print(vor.points)
#print(vor.vertices)
#print(vor.ridge_points)
#n = vor.regions
#print(n)
plt.show()



