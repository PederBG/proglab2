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
        all = []
        red = 0
        green = 0
        blue = 0

        for x in range(im.width):
            for y in range(im.height):
                if pix[x, y][0] > 150 and pix[x, y][1] < 40 and pix[x, y][2] < 40:
                    all.append(pix[x, y][0])
                red += (pix[x, y][0])
                green += (pix[x, y][1])
                blue += (pix[x, y][2])

        red_ratio = len(all) / (im.height*im.width)

        print("RedRatio:", red_ratio, "RGB:", red / (im.height*im.width), green / (im.height*im.width), blue / (im.height*im.width))

        if red_ratio >= 0.3:
            self.value = ("F", red_ratio)
        else:
            self.value = ("F", 0.0)

    def update(self):
        self.turnVal()
        return self.value

    def get_value(self):
        return self.value
