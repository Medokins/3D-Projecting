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

def findNearest(point, allPoints): #connect to at least 2 in the same height if height == 0, 1 or 2
    nearest = []
    #height = point[2]
    min = 10

    for currentPoint in allPoints:
        distance = math.sqrt(pow(point[0] - currentPoint[0], 2) + pow(point[1] - currentPoint[1], 2) + pow(point[2] - currentPoint[2], 2))
        if distance <= min:
            min = distance
            nearest.append(currentPoint)

    return nearest

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