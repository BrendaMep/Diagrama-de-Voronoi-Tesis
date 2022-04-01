import scipy.spatial.distance
from scipy.spatial.distance import cityblock
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



X = [2 , -4, -8, -1, 3]
Y = [4,4 ,-3 ,1,-1]
df = np.array([[2,4], [-4,4],[-8,-3],[-1,1],[3,-1]])
plt.scatter(X, Y,marker=".")

print(cityblock(A,B))



#X = [2 , -4, -8, -1, 3]
#Y = [4,4 ,-3 ,1,-1]
#df = np.array([[2,4], [-4,4],[-8,-3],[-1,1],[3,-1]])
#plt.scatter(X, Y,marker=".")
#man = cityblock(df)
#plt.show()