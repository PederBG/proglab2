from abc import abstractmethod
import random
from Sensob import LookAhead
from Sensob import CheckForRed
from Sensob import LookUnder

def recommended(command, speed=0.25, duration=0.1):
        return [command, speed, duration]

look_ahead = LookAhead()
is_red = CheckForRed()
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
        for sens_obj in self.sens_obs:
            sens_obj.update()
        self.calculate()

    def calculate(self):
        a = ["L", "R"]
        distance = self.sens_obs[0].get_value()
        if distance < 10:
            self.priority_weight = 1
            self.action_rec = recommended(a[random.randint(0, 1)])
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

class DetectEdge(Behavior):
    def __init__(self):
        super().__init__()
        self.sens_obs.append(look_under)

    def update(self):
        for sens_obj in self.sens_obs:
            sens_obj.update()
        self.calculate()

    def calculate(self):
        light_values = self.sens_obs[0]
        darkest = min(light_values)
        index = light_values.index(darkest)
        if darkest < 0.2:
            self.priority_weight = 1
            if index == 0: self.action_rec = recommended("R")
            elif index == 1: self.action_rec = recommended("R",0.20,0.1)
            elif index == 2: self.action_rec = recommended("R",0.15,0.1)
            elif index == 3: self.action_rec = recommended("L",0.15,0.1)
            elif index == 4: self.action_rec = recommended("L",0.20,0.1)
            elif index == 5: self.action_rec = recommended("L")
        else:
            self.priority_weight = 0.5
            self.action_rec = recommended("F")


    def get_name(self):
        return "DetectEdge"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

class ApproachRed(Behavior):
    pass