from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = [22,22,23,21,22,23,23,21],[73,75,79,82,79,80,77,79],[56,57,59,56,58,59,55,53]
ax.plot_wireframe(X, Y, Z)

plt.show()
