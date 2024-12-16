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



# matrix = np.zeros((YTILE, XTILE), dtype=int)
# fig, ax = plt.subplots()
# im = ax.imshow(matrix, cmap='cividis')

# # print(matrix)
# # Create the animation
# ani = FuncAnimation(fig, visualize, frames=500, interval=1000, blit=False)

# # Show the animation
# plt.show()

# def visualize(frame):
    # global matrix, ani,plt
    # global i, maxCluster
    # # print(matrix)
    # # clus = (0,0)
    # for robot in robots:
        # clusterCount = getNumCluster(matrix,robot[0])
        # if clusterCount > maxCluster:
            # print("found higher cluster at ",i, clusterCount, robot[0])
            # # clus = robot[0]
            # # input("press enter to continue")
            # maxCluster = clusterCount
    # if i == 8149:
        # input("press enter to continue")
        # # ani.event_source.pause()
        # # plt.close()
    # i += 1
    # matrix = np.zeros((YTILE, XTILE), dtype=int)
    # for j in range(len(robots)):
        # (x,y) = robots[j][0]
        # v = robots[j][1]
        # (newX, newY) = ((x+v[0])%XTILE, (y+v[1])%YTILE)
        # robots[j] = ((newX, newY),v)
        # matrix[newY][newX] = 50
    # # for r in range(len(matrix)):
        # # for c in range(len(matrix[r])):
            # # if matrix[r][c] > 0:
                # # matrix[r][c] = matrix[r][c] - 25
    
    # if i % 100 == 0:
        # print("i:",i)
    # # print(i,np.count_nonzero(matrix))
    # im.set_data(matrix)
    # return [im]