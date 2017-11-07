#from lib.imager2 import Imager
from lib.camera import Camera
import os
from PIL import Image
import numpy as np

class RedDetect():
    #imager = Imager()
    cam = Camera()
    image = Image.open(os.system(cam.sensor_get_value())) # tar bilde med kameraet og bruker dette
    pixels = image.load()
    meanValue = 0
    turnValue = 0
    def __init__(self):
        self.meanValue = 0
        self.turnValue = 0

    def mean_value(self): #returnerer r-gjennomsnittsverdien til bildet
        im = self.image
        pix = self.pixels
        red = []
        #green = []
        #blue = []
        for x in range(im.width):
            for y in range(im.height):
                red.append(pix[x,y][0])
                #green.append(pix[x, y][1])
                #blue.append(pix[x, y][2])
        self.meanValue = sum(red)//len(red)
        return self.meanValue
        #print("Green:", sum(green)//len(green))
        #print("Blue:", sum(blue)//len(blue))

    def update(self): #Returnerer hoyre r-value / venstre r-value
        im = self.image
        #pix = self.pixels
        #left = []
        #right = []
        left = im.crop((0, 0, im.width // 2, im.height))
        right = im.crop((im.width // 2, 0, im.width, im.height))

        leftTurn = np.asarray(left.getdata(0), dtype=np.int, order="C")
        rightTurn = np.asarray(right.getdata(0), dtype=np.int, order="C")
        '''for x in range(0,im.width//2):
            for y in range(im.height):
                left.append(pix[x, y][0])
        leftTurn = sum(left) // len(left)

        for x in range(im.width//2, im.width):
            for y in range(im.height):
                right.append(pix[x, y][0])
        rightTurn = sum(right) // len(right)
        #print("Right side:", sum(right) // len(right))
        '''
        self.turnValue = rightTurn/leftTurn
        return self.turnValue

    def get_value(self):
        return self.turnValue

        '''if rightTurn/leftTurn > 2:
            print("Turn right (" + str(rightTurn/leftTurn) + ")")
        elif leftTurn/rightTurn > 2:
            print("Turn left (" + str(leftTurn/rightTurn) + ")")
        else:
            print("Straight")'''