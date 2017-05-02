

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x= np.array([22,22,23,21,22,23,23,21])
y=np.array([73,75,79,82,79,80,77,79])
z=np.array([56,57,59,56,58,59,55,53])

ax1.scatter(x,y,z)
plt.show()
