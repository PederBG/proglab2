from lib.ultrasonic import Ultrasonic

class Controller():

    def __init__(self):
        self.LookAhead = LookAhead(Ultrasonic())
