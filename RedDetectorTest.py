from lib.camera import Camera
from lib.imager2 import Imager

from PIL import Image
cam = Camera()

im = Image.open(cam.update())
red = []
green = []
blue = []
left = []
right = []
pix = im.load()
for x in range(im.width):
    for y in range(im.height):
        red.append(pix[x,y][0])
        green.append(pix[x, y][1])
        blue.append(pix[x, y][2])
print("Red:", sum(red)//len(red))
print("Green:", sum(green)//len(green))
print("Blue:", sum(blue)//len(blue))

for x in range(0,im.width//2):
    for y in range(im.height):
        left.append(pix[x, y][0])
leftTurn = sum(left) // len(left)
print("Left side:", sum(left) // len(left))

for x in range(im.width//2, im.width):
    for y in range(im.height):
        right.append(pix[x, y][0])
rightTurn = sum(right) // len(right)
print("Right side:", sum(right) // len(right))

if rightTurn/leftTurn > 2:
    print("Turn right (" + str(rightTurn/leftTurn) + ")")
elif leftTurn/rightTurn > 2:
    print("Turn left (" + str(leftTurn/rightTurn) + ")")
else:
    print("Straight")
