import numpy as np
from scipy.spatial import distance
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.uniform(1,100,, columns=list('XY'))
plt.scatter(df.X, df.Y,marker=".")
plt.show()



def fijo(a,wa,b,wb):
  f = b*(wa**2)/(wa**2-wb**2)+a*(wb**2)/(wa**2-wb**2)
  print(f)

def radio(a,wa,b,wb):
  r = (wa*wb) * (distance.euclidean(a, b))/(wa**2-wb**2)
  print(r)



