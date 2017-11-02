from ultrasonic import Ultrasonic

class Sensob(object):
    def __init__(self):
        pass

    def update(self):
<<<<<<< HEAD
        #Temporary code for receiving values from sensors
        for sensor in self.sensors:
            tempValue = sensor.get_value()
=======
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
>>>>>>> acdb69d952214fa3886c15cd0f1ff1a556e3bc1a
