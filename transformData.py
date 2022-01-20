from PIL import Image
import numpy as np

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

def firstSquareVerticalCheck(number):
    if number < 2:
        return 1
    if number >= 2:
        return 0

def firstSquareHorizontalCheck(number):
    if number == 1 or number == 3:
        return 1
    if number == 0 or number == 2:
        return 0