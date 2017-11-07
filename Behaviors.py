from abc import abstractmethod
import operator

def recommended(command, speed=0.25, duration=0.1):
        return [command, speed, duration]

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
    def __init__(self, look_ahead):
        super().__init__()
        super.sens_obs.append(look_ahead)

    def update(self):
        for element in self.sens_obs:
            element.update()

    def get_name(self):
        return "Approach"

    def get_action_rec(self):
        return recommended('L')

    def get_priority_weight(self):
        dist = self.controller.lookAhed.get_value()
        if dist > 100:
            return 1
        else:
            return dist / 100

class BackOff(Behavior):
    def __init__(self, look_ahead, look_under):
        super().__init__()
        super.sens_obs.append(look_ahead, look_under)

    def update(self):
        for obs in self.sens_obs:
            obs.update()

        self.action_rec = recommended('L')
        self.priority_weight = 1

    def get_action_rec(self):
        return self.action_rec

    def get_priority_weight(self):
        return self.priority_weight

    def get_name(self):
        return "BackOff"
