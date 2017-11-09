from abc import abstractmethod
import random
from Sensob import LookAhead
from Sensob import LookUnder
from Sensob import CheckForRed

def recommended(command, speed=0.25, duration=0):
        return [command, speed, duration]

look_ahead = LookAhead()
is_red = CheckForRed()
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
        left_or_right = ["L", "R"]
        distance = self.sens_obs[0].get_value()
        print(distance)
        if distance < 10:
            self.priority_weight = 0.99
            self.action_rec = recommended("T",0.5,2)
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

    #Denne funksjonen er jallaballa
    def calculate(self):
        light_values = self.sens_obs[0].get_value()
        try:
            if sum(light_values) < 1.2:
                self.priority_weight = 1
                self.action_rec = recommended("T",0.5,2)
            elif sum(light_values[0:2]) < 0.4:
                self.priority_weight = 1
                self.action_rec = recommended("R",0.5,1)
            elif sum(light_values[4:]) < 0.4:
                self.priority_weight = 1
                self.action_rec = recommended("L",0.5,1)
            else:
                self.priority_weight = 0.2
                self.action_rec = recommended("F")
        except:
            print("Calculate crashed")

    def get_name(self):
        return "DetectEdge"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        #return self.priority_weight
        return 1

class ApproachRed(Behavior):
    def __init__(self):
        super().__init__()
        self.sens_obs.append(check_for_red)

    def update(self):
        for sens_obj in self.sens_obs:
            sens_obj.update()
        self.calculate()

    def calculate(self):
        try:
            sens_ob_values = self.sens_obs[0].get_value()
            if sens_ob_values[0][0].get_value == "R" and sens_ob_values[0][1] > 0.6:
                self.action_rec = recommended("R")
                self.priority_weight = 0.9
            elif sens_ob_values[0][0].get_value == "L" and sens_ob_values[0][1] > 0.6:
                self.action_rec = recommended("L")
                self.priority_weight = 0.9
            elif sens_ob_values[0][0].get_value == "F" and sens_ob_values[0][1] > 0.6:
                self.action_rec = recommended("F")
                self.priority_weight = 0.9
            else:
                self.action_rec = recommended("F")
                self.priority_weight = 0.5
        except:
            pass

    def get_name(self):
        return "ApproachRed"

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight
