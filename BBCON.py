import time
from library.irproximity_sensor import IRProximitySensor
from library.reflectance_sensors import ReflectanceSensors
from library.ultrasonic import Ultrasonic
from library.camera import Camera
from Sensob import Sensob

class BBCON():

    def __init__(self, behave = [], act_Behave = [], sens_Objs = [], mot_Objs = [], arbitrator = None):
        self.Behaviors = behave # a list of all the behavior objects used by the bbcon
        self.Active_behaviors = act_Behave # a list of all behaviors that are currently active.
        self.Sens_Objs = sens_Objs # a list of all sensory objects used by the bbcon
        self.Mot_Objs = mot_Objs # a list of all motor objects used by the bbcon
        self.Arbitrator = arbitrator # the arbitrator object that will resolve actuator requests produced by the behaviors.

    def add_behavior(self, behavior): #append a newly-created behavior onto the behaviors list.
        self.Behaviors.append(behavior)

    def add_sensObj(self, sensObj): #append a newly-created sensob onto the sensobs list.
        self.Sens_Objs.append(sensObj)

    def add_arbitrator(self, arbitrator): #append a newly-created sensob onto the sensobs list.
        self.Arbitrator = arbitrator

    def add_mot_obj(self, mot_obj): #append a newly-created sensob onto the sensobs list.
        self.Mot_Objs = mot_obj

    def Add_active_behavior(self, behavior): #add an existing behavior onto the active-behaviors list
        if behavior in self.Behaviors:
            self.Active_behaviors.append(behavior)
            self.Arbitrator.BBCONsActive_behaviors = self.Active_behaviors

    def deactive_behavior(self, behavior): #remove an existing behavior from the active behaviors list.
        if behavior in self.Active_behaviors:
            self.Active_behaviors.remove(behavior)

    def run_one_timestep(self): # constitutes the core BBCON activity
        self.update_all_sensObs()
        motorRecommendation = self.choose_action()
        self.update_motObs(motorRecommendation)
        self.wait()

    def update_all_sensObs(self): #These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values
        for sensObj in self.Sens_Objs:
            sensObj.update()

    def choose_action(self): # choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        return self.Arbitrator.chooseBest()

    def update_motObs(self, motorRecommendation): #
        self.Mot_Objs.apply_motor_recommendation(motorRecommendation)

    def wait(self, Secs = 0.5): # This pause (in code execution) will allow the motor settings to remain active for a short period of time
        time.sleep(Secs)

    def reset_sensObs(self, sensObs): #Each sensob may need to reset itself, or its associated sensor(s), in some way.
        pass
