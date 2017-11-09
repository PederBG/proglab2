import time

class BBCON():

    def __init__(self, behaviors = [], active_behaviors = [], motob = None, arbitrator = None):
        self.behaviors = behaviors # a list of all the behavior objects used by the bbcon
        self.active_behaviors = active_behaviors # a list of all behaviors that are currently active.
        self.motob = motob # motorobjektet brukt av BBCON
        self.arbitrator = arbitrator # the arbitrator object that will resolve actuator requests produced by the behaviors.


    def add_behavior(self, behavior): #append a newly-created behavior onto the behaviors list.
        self.behaviors.append(behavior)

    def add_active_behavior(self, behavior): #add an existing behavior onto the active-behaviors list
        if behavior in self.behaviors:
            self.active_behaviors.append(behavior)
            self.arbitrator.add_active_behavior(behavior)

    def remove_active_behavior(self, behavior): #remove an existing behavior from the active behaviors list.
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
            self.arbitrator.remove_active_behavior(behavior)

    def set_arbitrator(self, arbitrator): #append a newly-created sensob onto the sensobs list.
        self.arbitrator = arbitrator

    def set_motob(self, motob): #append a newly-created sensob onto the sensobs list.
        self.motob = motob

    def run_one_timestep(self): # constitutes the core BBCON activity
        self.arbitrator.update()
        motor_recommendation = self.arbitrator.choose_action()
        print("Active motor recommendation: " , motor_recommendation)
        for x in range(0, len(motor_recommendation)):
            self.update_motob(motor_recommendation)

    def update_motob(self, motor_recommendation): #
        self.motob.apply_motor_recommendation(motor_recommendation)

    def wait(self, secs = 0.5): # This pause (in code execution) will allow the motor settings to remain active for a short period of time
        time.sleep(secs)
