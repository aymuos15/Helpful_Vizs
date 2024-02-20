import numpy as np
import matplotlib.pyplot as plt
import cc3d # https://pypi.org/project/connected-components-3d/

# Define dimensions of the array
x_dim = 10
y_dim = 10
z_dim = 10

# Create a 3D numpy array filled with zeros
array_3d = np.zeros((x_dim, y_dim, z_dim), dtype=int)

# Set some arbitrary values to create different connected components
array_3d[2:5, 2:5, 2:5] = 1
array_3d[7:9, 7:9, 7:9] = 2
array_3d[0:3, 0:3, 0:3] = 3

# Get labeled components
labels_out = cc3d.connected_components(array_3d)  # 26-connected
num_features = np.max(labels_out)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each component with different color
colors = plt.get_cmap('Spectral')(np.linspace(0, 1, num_features))
for i, image in cc3d.each(labels_out, binary=False, in_place=True):
    ax.voxels(image == i, facecolors=colors[i-1], edgecolors='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
