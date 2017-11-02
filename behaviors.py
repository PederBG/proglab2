from abc import abstractmethod

def recommended(command, speed=0.25, duration=0.1):
        return [command, speed, duration]

class Behavior():
    def __init__(self, controller):
        self.controller = controller

    @abstractmethod
    def get_action_recs(self):
        pass

    @abstractmethod
    def get_priority_weight(self):
        pass

class Approach(Behavior):
    def __init__(controller):
        super().__init__(controller)

    def get_action_recs(self):
        return recommended('L')

    def get_priority_weight(self):
        dist = self.controller.lookAhed.get_value()
        return dist


class BackOff(Behavior):
    def __init__(controller):
        super().__init__(controller)

    def get_action_recs(self):
        return recommended('B')

    def get_priority_weight(self):
        dist = self.controller.lookAhed.get_value()
        return 100 - dist
