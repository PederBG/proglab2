#from lib.imager2 import Imager
from lib.camera import Camera
#import os
from PIL import Image
#import numpy as np

class RedDetect():
    def __init__(self):
        self.value = ("F",0.0)

    def turnVal(self): #Returnerer hoyre r-value / venstre r-value
        cam = Camera()
        im = Image.open(cam.update())
        pix = im.load()
        left = []
        right = []
        all = []
        blueAll = []
        greenAll = []
        blueLeft = []
        greenLeft = []
        blueRight = []
        greenRight = []
        """left = im.crop((0, 0, im.width // 2, im.height))
        right = im.crop((im.width // 2, 0, im.width, im.height))

        leftTurn = np.asarray(left.getdata(0), dtype=np.int, order="C")
        rightTurn = np.asarray(right.getdata(0), dtype=np.int, order="C")"""
        for x in range(0,im.width//2):
            for y in range(im.height):
                left.append(pix[x, y][0])
                blueLeft.append(pix[x, y][2])
                greenLeft.append(pix[x, y][1])
        leftRed = sum(left) // len(left)

        for x in range(im.width//2, im.width):
            for y in range(im.height):
                right.append(pix[x, y][0])
                greenRight.append(pix[x, y][1])
                blueRight.append(pix[x, y][2])
        rightRed = sum(right) // len(right)

        for x in range(im.width):
            for y in range(im.height):
                all.append(pix[x, y][0])
                greenAll.append(pix[x, y][1])
                blueAll.append(pix[x, y][2])
        forward = sum(all) // len(all)

        if leftRed >= 40 and greenLeft < 40 and blueLeft < 40:
            self.value = ("L", leftRed/255)
        elif rightRed >= 40 and greenRight < 40 and blueRight < 40:
            self.value = ("R", rightRed/255)
        elif forward >= 50 and greenAll < 50 and blueAll < 50:
            self.value = ("F", forward/255)
        else:
            self.value = ("F", 0.0)

    def update(self):
        self.turnVal()
        return self.value

    def get_value(self):
        return self.value
