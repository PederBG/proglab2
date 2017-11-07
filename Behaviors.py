from abc import abstractmethod
import random
from Sensob import LookAhead
from Sensob import IsRed
from Sensob import LookUnder

def recommended(command, speed=0.25, duration=0.1):
        return [command, speed, duration]

look_ahead = LookAhead()
is_red = IsRed()
look_under = LookUnder()

class Behavior():
    def __init__(self):
        self.action_rec = None
        self.priority_weight = None
        self.sens_obs =[]

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_action_recs(self):
        pass

    @abstractmethod
    def get_priority_weight(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Approach(Behavior):
    def __init__(self):
        super().__init__()
        self.sens_obs.append(look_ahead)

    def update(self):
        for element in self.sens_obs:
            element.update()
        self.calculate()

    def calculate(self):
        a = ["L", "R"]
        distance = self.sens_obs[0].get_value()
        if distance < 10:
            self.priority_weight = 1
            self.action_rec = recommended(a[random.randint(0,2)])
        else:
            self.priority_weight = self.set_priority_weight()
            self.action_rec = recommended("F")

    def get_name(self):
        return "Approach"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

    def set_priority_weight(self):
        dist = self.sens_obs[0].get_value()
        if dist > 100:
            return 1
        else:
            return dist / 100

class BackOff(Behavior):
    def __init__(self):
#        super().__init__()
#        self.sens_obs.append(look_ahead)
#
#    def update(self):
#        for obs in self.sens_obs:
#            obs.update()
#
#        self.action_rec = recommended('L')
#        self.priority_weight = 1

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

    def get_name(self):
        return "BackOff"

class DetectEdge(Behavior):
    pass

class Approachred(Behavior):
    pass