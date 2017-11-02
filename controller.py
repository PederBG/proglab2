from lib.ultrasonic import Ultrasonic

class Controller():

    def __init__(self):
        self.lookAhed = LookAhed( Ultrasonic() )
