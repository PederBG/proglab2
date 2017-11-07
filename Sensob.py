from lib.ultrasonic import Ultrasonic
<<<<<<< Updated upstream

#SuperClass for SensobObjects
=======
from lib.reflectance_sensors import ReflectanceSensors
from lib.camera import Camera
from RedDetectorTest import RedDetect
from lib.imager2 import Imager
>>>>>>> Stashed changes
class Sensob(object):
    def __init__(self):
        pass

    def update(self):
        pass

    def get_value(self):
        pass

class LookAhead(Sensob):
    def __init__(self):
        self.sensor = Ultrasonic()
        self.value = 0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()

    def get_value(self):
        return self.value

class IsRed(Sensob):

    def __init__(self):
        self.sensor = RedDetect()
        self.value = 0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.()

    def get_value(self):
        return RedD.meanValue()


class LookUnder(Sensob):

    def __init__(self):
        self.sensor = ReflectanceSensors()
        self.value = 0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()

    def get_value(self):
        return self.value
