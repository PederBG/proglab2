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
        blueAll = []
        greenAll = []
        blueLeft = []
        greenLeft = []
        blueRight = []
        greenRight = []
        '''left = im.crop((0, 0, im.width // 2, im.height))
        right = im.crop((im.width // 2, 0, im.width, im.height))

        leftTurn = np.asarray(left.getdata(0), dtype=np.int, order="C")
        rightTurn = np.asarray(right.getdata(0), dtype=np.int, order="C")
        for x in range(0,im.width//2):
            for y in range(im.height):
                left.append(pix[x, y][0])
                blueLeft.append(pix[x, y][2])
                greenLeft.append(pix[x, y][1])
        leftRed = sum(left) // len(left)
        greenLeftTurn = sum(greenLeft) // len(greenLeft)
        blueLeftTurn = sum(blueLeft) // len(blueLeft)


        for x in range(im.width//2, im.width):
            for y in range(im.height):
                right.append(pix[x, y][0])
                greenRight.append(pix[x, y][1])
                blueRight.append(pix[x, y][2])
        rightRed = sum(right) // len(right)
        greenRightTurn = sum(greenRight) // len(greenRight)
        blueRightTurn = sum(blueRight) // len(blueRight)'''

        for x in range(im.width):
            for y in range(im.height):
                if pix[x, y][0] > 150 and pix[x, y][1] < 40 and pix[x, y][2] < 40:
                    all.append(pix[x, y][0])
                #greenAll.append(pix[x, y][1])
                #blueAll.append(pix[x, y][2])
        red_ratio = len(all) / (im.height*im.width)
        #blueForward = sum(blueAll) // len(blueAll)
        #greenForward = sum(greenAll) // len(greenAll)

        '''if leftRed >= 40 and greenLeftTurn < 40 and blueLeftTurn < 40:
            self.value = ("L", leftRed/255)
        elif rightRed >= 40 and greenRightTurn < 40 and blueRightTurn < 40:
            self.value = ("R", rightRed/255)'''
        print("RedRatio:", red_ratio)
        if red_ratio >= 0.3:
            self.value = ("F", red_ratio)
        else:
            self.value = ("F", 0.0)

    def update(self):
        self.turnVal()
        return self.value

    def get_value(self):
        return self.value
