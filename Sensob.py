from ultrasonic import Ultrasonic

class Sensob(object):
    def __init__(self):
        pass

    def update(self):
        #Temporary code for receiving values from sensors
        for sensor in self.sensors:
            tempValue = sensor.get_value()
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
