from lib.motors import Motors

class Motob:
    def __init__(self):
        self.motors = Motors()

    def apply_motor_recommendation(self, motor_recommendation):
        if(motor_recommendation[0] == 'L'):
            self.motors.left(motor_recommendation[1], motor_recommendation[2])
        elif(motor_recommendation[0] == 'R'):
            self.motors.right(motor_recommendation[1], motor_recommendation[2])
        elif(motor_recommendation[0] == 'F'):
            self.motors.forward(motor_recommendation[1], motor_recommendation[2])
        elif(motor_recommendation[0] == 'T'):
            self.motors.turn180()
        elif(motor_recommendation[0] == 'TL'):
            self.motors.turn90_left()
        elif(motor_recommendation[0] == 'TR'):
            self.motors.turn90_right()
