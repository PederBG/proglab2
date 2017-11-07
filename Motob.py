from lib.motors import Motors

motors = Motors()
class Motob:

    def __int__(self):
        self.motors = motors

    def apply_motor_recommendation(self, motor_recommendation):
        if(motor_recommendation[0] == 'L'):
            self.motors.left(motor_recommendation[1], motor_recommendation[2])
        elif(motor_recommendation[0] == 'R'):
            self.motors.right(motor_recommendation[1], motor_recommendation[2])
        elif(motor_recommendation[0] == 'F'):
            self.motors.forward(motor_recommendation[1], motor_recommendation[2])
