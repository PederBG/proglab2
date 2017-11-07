import time
start_time = time.time()

from PIL import Image
import numpy as np
im = Image.open("redTest2.jpg")

left = im.crop((0, 0, im.width//2, im.height))
right = im.crop((im.width//2, 0, im.width, im.height))

npLeft = np.asarray(left.getdata(0), dtype=np.int, order="C")
npRight = np.asarray(right.getdata(0), dtype=np.int, order="C")

print("Left: ", int(npLeft.mean()), "\nRight: " , int(npRight.mean()))

print("--- %s seconds ---" % (time.time() - start_time))
