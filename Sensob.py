from lib.ultrasonic import Ultrasonic
#SuperClass for SensobObjects
from lib.reflectance_sensors import ReflectanceSensors
from lib.camera import Camera
from RedDetectorTest import RedDetect
from lib.imager2 import Imager

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
        return self.value # returnerer avstand til objekt i cm

class CheckForRed(Sensob):

    def __init__(self):
        self.sensor = RedDetect()
        self.value = 0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.update()

    def get_value(self):
        return self.sensor.get_value() # returnerer hoyre side / venstre side


class LookUnder(Sensob):

    def __init__(self):
        self.sensor = ReflectanceSensors()
        self.value = 0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()

    def get_value(self):
        return self.value # returnerer en liste av lengde 6 med verdier mellom 0 og 1 der 1 er hvit
