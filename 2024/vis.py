import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colormaps
import random
np.seterr(divide='ignore', invalid='ignore')

# Create a figure and axes
fig, ax = plt.subplots()
print(list(colormaps))
# Generate some initial data
# matrix = np.ones((5, 5))
# matrix = np.matrix([[0,0,0,0,0],
          # [0,0,0,0,0],
          # [0,0,0,0,0],
          # [0,0,0,0,0],
          # [0,0,0,0,0]])
# matrix = np.random.rand(5, 5)
matrix = np.zeros((5, 5), dtype=int)
matrix[0][0] = 4
# matrix = np.random.randint(2, size=(5, 5))
print(matrix)

# Create an image plot
im = ax.imshow(matrix, cmap='cividis')

# Update function for animation
def update(frame):
    # Update the matrix data
    # matrix = np.random.rand(5, 5)
    # matrix = np.random.randint(2, size=(5, 5))
    
    # matrix = np.empty((5, 5))
    i = random.randint(0,4);
    j = random.randint(0,4);

    matrix[i][j] = i
    matrix[j][i] = 0
    # print(matrix)
    im.set_data(matrix)
    return [im]

# Create the animation
ani = FuncAnimation(fig, update, frames=500, interval=200, blit=True)

# Show the animation
plt.show()