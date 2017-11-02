class Sensob:

    def __init__(self, name, sensors = [], value = 0):
        self.name = name
        self.sensors = sensors
        self.value = value

    def update(self):
        #Temporary code for receiving values from sensors
        for sensor in self.sensors:
            tempValue = sensor.get_value()

