import numpy as np
import matplotlib.pyplot as plt
from transformData import convertToBinary, firstSquareHorizontalCheck

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

#now i need to check for diagonal lines

#first sqaure, the front view
for square in range(4):
    for x in range(2):
        for y in range(2):
            if square < 2:
                if imgArray[int(x + (spacing + start)/2 + square*spacing), int(y + (spacing + start)/2)] != 0:
                    for i in range(3):
                        point = [i, round((x+2)*(1/spacing) + firstSquareHorizontalCheck(square), 2), round((3-y)*(1/spacing) + 1, 2)]
                        if point not in allpoints:
                            allpoints.append(point)

            if square >= 2:
                if imgArray[int(x + (spacing + start)/2 + (square-2)*spacing), int(y + (spacing + start)/2) + spacing] != 0:
                    for i in range(3):
                        point = [i, round((x+2)*(1/spacing) + firstSquareHorizontalCheck(square), 2), round((3-y)*(1/spacing), 2)]
                        if point not in allpoints:
                            allpoints.append(point)

# 33 43 => (0, 0.4, 1.6), (0, 0.6, 1.6)
# 34 44 => (0, 0.4, 1.4), (0, 0.6, 1.4)
# 83 93 => (0, 1.4, 1.6). (0, 1.6, 1.6)
# 84 94 => (0, 1.4, 1.4). (0, 1.6, 1.4)

# 38 48 => (0, 0.4, 0.6), (0, 0.6, 0.6)
# 39 49 => (0, 0.4, 0.4), (0, 0.6, 0.4)
# 88 98 => (0, 1.4, 0.6), (0, 1.6, 0.6)
# 89 99 => (0, 1.4, 0.4), (0, 1.6, 0.4)

X = []
Y = []
Z = []

for point in (allpoints):
    X.append(point[0])
    Y.append(point[1])
    Z.append(point[2])

ax.scatter(X, Y, Z, c = 'black')
plt.show()