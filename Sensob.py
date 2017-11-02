from lib.ultrasonic import Ultrasonic

#SuperClass for SensobObjects
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
