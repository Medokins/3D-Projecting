from PIL import Image
import numpy as np

def convertToBinary(name):
    im = Image.open(f"Images/{name}.png")
    imArr = np.zeros(im.size)

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            coordinate = y, x
            if im.getpixel(coordinate) == (0, 0, 0):
                imArr[x][y] = 1
            else:
                imArr[x][y] = 0
    return imArr