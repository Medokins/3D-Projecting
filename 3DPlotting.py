import numpy as np
import matplotlib.pyplot as plt
from transformData import *

imgArray = convertToBinary("triangles")
color = "black"
modelOnly = True

figure = plt.figure(facecolor='w')
ax = plt.axes(projection ='3d')
ax.invert_xaxis()

if modelOnly:
    plt.axis('off')
    plt.grid(b=None)

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

#first sqaure, front view
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

#second square, side view
for square in range(4):
    for x in range(2):
        for y in range(2):
            if square < 2:
                if imgArray[int(x + spacing*2 + 2*start + (spacing + start)/2 + square*spacing), int(y + (spacing + start)/2)] != 0:
                    for i in range(3):
                        point = [round(1 - (x+2)*(1/spacing) + secondSquareHorizontalCheck(square), 2),0, round((3-y)*(1/spacing) + 1, 2)]
                        if point not in allpoints:
                            allpoints.append(point)
            if square >= 2:
                if imgArray[int(x + spacing*2 + 2*start + (spacing + start)/2 + (square-2)*spacing), int(y + (spacing + start)/2) + spacing] != 0:
                    for i in range(3):
                        point = [round(1 - (x+2)*(1/spacing) + secondSquareHorizontalCheck(square), 2),i, round((3-y)*(1/spacing), 2)]
                        if point not in allpoints:
                            allpoints.append(point)

#third square, view from above
for square in range(4):
    for x in range(2):
        for y in range(2):
            if square < 2:
                if imgArray[int(y + (spacing + start)/2), int(x + spacing*2 + 2*start + (spacing + start)/2 + square*spacing)] != 0:
                    for i in range(3):
                        point = [round(1 - (x+2)*(1/spacing) + secondSquareHorizontalCheck(square), 2),round(1 - (3-y)*(1/spacing), 2),i]
                        if point not in allpoints:
                            allpoints.append(point)
            if square >= 2:
                if imgArray[int((y + (spacing + start)/2) + spacing), int(x + spacing*2 + 2*start + (spacing + start)/2 + (square-2)*spacing)] != 0:
                    for i in range(3):
                        point = [round(1 - (x+2)*(1/spacing) + thirdSquareHorizontalCheck(square), 2), round(1 - (3-y)*(1/spacing), 2) + 1, i]
                        if point not in allpoints:
                            allpoints.append(point)


#now i need to check squares, the reason I'm doing it in this order is that it's easier to detect diagonal lines in squares and remove them
#first square, front view
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
            for i in np.arange(0, 3.0, round(1/spacing, 2)):
                for xoffset in np.arange(0, 1.0, round(1/spacing, 2)):
                    for yoffset in np.arange(0, 1.0, 1/spacing):
                        point = [x+round(xoffset, 2), y-2 + round(yoffset, 2), round(i, 2)]
                        if point in allpoints:
                            allpoints.remove(point)


X = []
Y = []
Z = []

lineSegments = []

for point in allpoints:
    X.append(point[0])
    Y.append(point[1])
    Z.append(point[2])

for point in allpoints:
    nearest = findNearest(point, allpoints)
    for i in range(len(nearest)):
        ax.plot([point[0], nearest[i][1][0]], [point[1],nearest[i][1][1]],zs=[point[2],nearest[i][1][2]])
        lineSegments.append([point[0], nearest[i][1][0], point[1],nearest[i][1][1], point[2],nearest[i][1][2]])

for line in lineSegments:
    print(findParallel(line, lineSegments))

if modelOnly:
    plt.show()
else:
    ax.scatter(X, Y, Z, c = color)
    plt.show()