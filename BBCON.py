import time

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

    def Add_active_behavior(self, behavior): #add an existing behavior onto the active-behaviors list
        if behavior in self.Behaviors:
            self.Active_behaviors.append(behavior)

    def deactive_behavior(self, behavior): #remove an existing behavior from the active behaviors list.
        if behavior in self.Active_behaviors:
            self.Active_behaviors.remove(behavior)

    def run_one_timestep(self): # constitutes the core BBCON activity
        self.update_all_sensObs()
        self.update_all_behaviors()
        self.choose_action()
        self.update_motObs()
        self.wait()
        self.reset_sensObs()

    def update_all_sensObs(self): #These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values
        #stå noe her

    def update_all_behaviors(self): # These updates involve reading relevant sensob values and producing a motor recommendation.
        #stå noe her

    def choose_action(self): # choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        return self.Arbitrator.choose_action()

    def update_motObs(self): #
        #stå noe her

    def wait(self, Secs = 0): # This pause (in code execution) will allow the motor settings to remain active for a short period of time
        time.sleep(Secs)

    def reset_sensObs(self, sensObs): #Each sensob may need to reset itself, or its associated sensor(s), in some way.
        #stå noe her
