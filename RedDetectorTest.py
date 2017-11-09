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
        im = cam.update()
        pix = im.load()
        left = []
        right = []
        all = []
        """left = im.crop((0, 0, im.width // 2, im.height))
        right = im.crop((im.width // 2, 0, im.width, im.height))

        leftTurn = np.asarray(left.getdata(0), dtype=np.int, order="C")
        rightTurn = np.asarray(right.getdata(0), dtype=np.int, order="C")"""
        for x in range(0,im.width//2):
            for y in range(im.height):
                left.append(pix[x, y][0])
        leftTurn = sum(left) // len(left)

        for x in range(im.width//2, im.width):
            for y in range(im.height):
                right.append(pix[x, y][0])
        rightTurn = sum(right) // len(right)

        for x in range(im.width):
            for y in range(im.height):
                all.append(pix[x, y][0])
        forward = sum(all) // len(all)
        print("Leftturn :", leftTurn, "Rightturn: ", rightTurn)
        if leftTurn/rightTurn > 2:
            self.value = ("L", leftTurn/255)
        elif rightTurn/leftTurn > 2:
            self.value = ("R", rightTurn/255)
        elif forward > 50 and leftTurn/rightTurn < 3 and rightTurn/leftTurn < 3:
            self.value = ("F", forward/255)

    def update(self):
        self.turnVal()
        return self.value

    def get_value(self):
        return self.value
