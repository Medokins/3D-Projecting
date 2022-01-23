from re import A
from PIL import Image
import numpy as np
import math

def convertToBinary(name):
    im = Image.open(f"Images/{name}.png")
    imArr = np.zeros(im.size)

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            coordinate = y, x
            if im.getpixel(coordinate) == (0, 0, 0):
                imArr[y][x] = 1
            else:
                imArr[y][x] = 0
    return imArr

def findNearest(point, allPoints):
    nearest = []
    adjacent = 1

    for currentPoint in allPoints:
        distance = round(math.sqrt(pow(point[0] - currentPoint[0], 2) + pow(point[1] - currentPoint[1], 2) + pow(point[2] - currentPoint[2], 2)), 3)
        if distance <= adjacent:
            nearest.append([distance, currentPoint])
    return nearest

def findParallel(lineSegment, lineSegments): #this is so that program will later fill 2 adjacent parallel lines with plane
    parallel = []
    lineSegments.remove(lineSegment)

    if lineSegment[:2] == [0,1] or lineSegment[:2] == [1,2]: #all lines in X direction
        for line in lineSegments:
            if line[:2] == lineSegment[:2]: #if in same X direction and have same start/end
                if line[2] == line [3] and line[4] == line[5]: #if not diagonal
                    if line[4] == lineSegment[4] or line[4] <= lineSegment[4] + 1 or line[4] <= lineSegment[4] - 1: #if they're same heights or one lower/higher
                        parallel.append(line)

    elif lineSegment[2:4] == [0,1] or lineSegment[2:4] == [1,2]: #all lines in Y direction
        for line in lineSegments:
            if line[2:4] == lineSegment[2:4]: #if in same Y direction and have same start/end
                if line[0] == line [1] and line[4] == line[5]: #if not diagonal
                    if line[4] == lineSegment[4] or line[4] <= lineSegment[4] + 1 or line[4] <= lineSegment[4] - 1: #if they're same heights or max one lower/higher
                        parallel.append(line)

    elif lineSegment[4:6] == [0,1] or lineSegment[4:6] == [1, 2]: #all lines in Z direction
        pass
    return parallel

def firstSquareHorizontalCheck(number):
    if number == 1 or number == 3:
        return 1
    if number == 0 or number == 2:
        return 0

def secondSquareHorizontalCheck(number):
    if number == 0 or number == 2 or number == 3:
        return 1
    if number == 1:
        return 0

def thirdSquareHorizontalCheck(number):
    if number == 0 or number == 1 or number == 2:
        return 1
    if number == 3:
        return 0