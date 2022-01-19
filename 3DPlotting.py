import numpy as np
import matplotlib.pyplot as plt
from transformData import convertToBinary

#front, side, up
name = "stairs"

imgArray = convertToBinary(name)

figure = plt.figure(facecolor='w')
ax = plt.axes(projection ='3d')
ax.invert_xaxis()

ax.set_xlabel('X', linespacing=3.2)
ax.set_ylabel('Y', linespacing=3.2)
ax.set_zlabel('Z', linespacing=3.2)

dimensonalX = []
dimensonalY = []
dimensonalZ = []

start = 1 #hard coding this for now, will change once i have working model
spacing = 5 #hard coding this for now, will change once i have working model

mainPoints = np.ones((9, 9))

#first square, the front view
for x in range(3):
    for y in range(3):
        if imgArray[x * spacing + start,y * spacing + start] != 0:
            print(x,y, 2-y)
            dimensonalX.append(x)
            dimensonalY.append(y)
            dimensonalZ.append(2-y)

ax.scatter(dimensonalX, dimensonalY, dimensonalZ, c="black")
plt.show()

#if imArray[1, 1]  == 0: point A(x, y, z) = (0, 0, 2) & (1, 0, 2) & (2, 0, 2) doesn't exist
#if imArray[6, 1]  == 0: point A(x, y, z) = (0, 1, 2) & (1, 1, 2) & (2, 1, 2) doesn't exist
#if imArray[11, 1] == 0: point A(x, y, z) = (0, 2, 2) & (1, 2, 2) & (2, 2, 2) doesn't exist