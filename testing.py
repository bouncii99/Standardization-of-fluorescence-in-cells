from PIL import Image
import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')

# xpos = [1,2,3,4,5,6,7,8,9,10]
# ypos = [2,3,4,5,1,6,2,1,7,2]
# num_elements = len(xpos)
# zpos = [0,0,0,0,0,0,0,0,0,0]
# dx = np.ones(10)
# dy = np.ones(10)
# dz = [1,2,3,4,5,6,7,8,9,10]

# ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
# plt.show()

file = Image.open("Cells_KB.jpg")
width, height = file.size

print(width, height)