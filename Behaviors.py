from abc import abstractmethod
import random
from Sensob import LookAhead
from Sensob import LookUnder
from Sensob import CheckForRed

def recommended(command, speed=0.15, duration=0):
        return [command, speed, duration]

look_ahead = LookAhead()
look_under = LookUnder()
check_for_red = CheckForRed()

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
        distance = self.sens_obs[0].get_value()
        if distance < 10:
            self.priority_weight = 0.98
            self.action_rec = [recommended("T", 0.5, 1.6)]
        else:
            self.priority_weight = 0.5
            self.action_rec = [recommended("F")]

    def get_name(self):
        return "Approach"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

class DetectEdge(Behavior):
    def __init__(self):
        super().__init__()
        self.sens_obs.append(look_under)

    def update(self):
        for sens_obj in self.sens_obs:
            sens_obj.update()
        self.calculate()

    #Denne funksjonen er jallaballa
    def calculate(self):
        light_values = self.sens_obs[0].get_value()

        if sum(light_values) < 2.2:
            self.priority_weight = 1
            self.action_rec = [recommended("B", 0.15, 1.5), recommended("T",0.5, 1.6)]
        elif light_values[0] < 0.3:
            self.priority_weight = 1
            self.action_rec = [recommended("B", 0.15, 1.5), recommended("TR",0.5,0.8)]
        elif light_values[5] < 0.3:
            self.priority_weight = 1
            self.action_rec = [recommended("B", 0.15, 1.5), recommended("TL",0.5,0.8)]
        else:
            self.priority_weight = 0.2
            self.action_rec = [recommended("F")]


    def get_name(self):
        return "DetectEdge"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

class ApproachRed(Behavior):
    def __init__(self):
        super().__init__()
        self.sens_obs.append(check_for_red)

    def update(self):
        for sens_obj in self.sens_obs:
            sens_obj.update()
        self.calculate()

    def calculate(self):
        sens_ob_values = self.sens_obs[0].get_value()
        if sens_ob_values[0] == "F" and sens_ob_values[1] > 0.05:
            self.action_rec = [recommended("F", 0.25)]
            self.priority_weight = 0.99
        else:
            self.action_rec = [recommended("F")]
            self.priority_weight = 0.1

    def get_name(self):
        return "ApproachRed"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight
