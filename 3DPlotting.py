import numpy as np
import matplotlib.pyplot as plt
from transformData import convertToBinary

name = "stairs"

imgArray = convertToBinary(name)

figure = plt.figure(facecolor='w')
ax = plt.axes(projection ='3d')
ax.invert_xaxis()

ax.set_xlabel('X', linespacing=3.2)
ax.set_ylabel('Y', linespacing=3.2)
ax.set_zlabel('Z', linespacing=3.2)

allpoints = []

for x in range(3):
    for y in range(3):
        for z in range(3):
            allpoints.append([x,y,z])


start = 1 #hard coding this for now, will change once i have working model
spacing = 5 #hard coding this for now, will change once i have working model

#first square, the front view
for x in range(3):
    for y in range(3):
        if imgArray[x * spacing + start,y * spacing + start] == 0:
            for i in range(3):
                point = [i, y, 2-y]
                allpoints.remove(point)

#if imArray[1, 1]  == 0: point A(x, y, z) = (0, 0, 2) & (1, 0, 2) & (2, 0, 2) doesn't exist
#if imArray[6, 1]  == 0: point A(x, y, z) = (0, 1, 2) & (1, 1, 2) & (2, 1, 2) doesn't exist
#if imArray[11, 1] == 0: point A(x, y, z) = (0, 2, 2) & (1, 2, 2) & (2, 2, 2) doesn't exist

#if imArray[1, 6]  == 0: point A(x, y, z) = (0, 0, 1) & (1, 0, 1) & (2, 0, 1) doesn't exist
#if imArray[6, 6]  == 0: point A(x, y, z) = (0, 1, 1) & (1, 1, 1) & (2, 1, 1) doesn't exist
#if imArray[11, 6] == 0: point A(x, y, z) = (0, 2, 1) & (1, 2, 1) & (2, 2, 1) doesn't exist

#if imArray[1, 11]  == 0: point A(x, y, z) = (0, 0, 0) & (1, 0, 0) & (2, 0, 0) doesn't exist
#if imArray[6, 11]  == 0: point A(x, y, z) = (0, 1, 0) & (1, 1, 0) & (2, 1, 0) doesn't exist
#if imArray[11, 11] == 0: point A(x, y, z) = (0, 2, 0) & (1, 2, 0) & (2, 2, 0) doesn't exist

#second square, side view:

#third square, view from above:

X = []
Y = []
Z = []

for point in (allpoints):
    X.append(point[0])
    Y.append(point[1])
    Z.append(point[2])

ax.scatter(X, Y, Z, c = 'black')
plt.show()