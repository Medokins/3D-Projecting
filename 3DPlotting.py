import numpy as np
import matplotlib.pyplot as plt
from transformData import convertToBinary

imgArray = convertToBinary("triangles")

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
                point = [i, x, 2-y]
                if point in allpoints:
                    allpoints.remove(point)


#second square, side view:
for x in range(3):
    for y in range(3):
        if imgArray[x*spacing + 2*spacing + 3*start,y * spacing + start] == 0:
            for i in range(3):
                point = [y, i, 2-y]
                if point in allpoints:
                    allpoints.remove(point)
                    


#third square, view from above:
for x in range(3):
    for y in range(3):
        if imgArray[x * spacing + start,y*spacing + 2*spacing + 3*start] == 0:
            for i in range(3):
                point = [x, y-2, i]
                if point in allpoints:               
                    allpoints.remove(point)

X = []
Y = []
Z = []

for point in (allpoints):
    X.append(point[0])
    Y.append(point[1])
    Z.append(point[2])

ax.scatter(X, Y, Z, c = 'black')
plt.show()