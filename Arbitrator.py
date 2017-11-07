## The motor object (motob) manifests an interface between a behavior and one or more motors (a.k.a. actuators)

import operator

class Arbitrator():

    def __init__(self, active_behaviors = []):
        self.behaviors = {"Approach": 0, "DetectEdge": 0, "ApproachRed": 0}
        self.active_behaviors = active_behaviors

    def update(self):
        for behavior in self.behaviors:
            self.behaviors[behavior] = 0
        for behavior in self.active_behaviors:
            behavior.update()
            self.behaviors[behavior.get_name()] = behavior.get_priority_weight()

    def choose_action(self):
        self.update()
        sorted_behaviors = sorted(self.behaviors.items(), key=operator.itemgetter(1))
        name = sorted_behaviors[-1][0]
        for behavior in self.active_behaviors:
            if behavior.get_name() == name:
                return behavior.get_action_rec()

    def add_active_behavior(self, behavior):
        if(not behavior in self.active_behaviors):
            self.active_behaviors.append(behavior)

    def remove_active_behavior(self, behavior):
        if(behavior in self.active_behaviors):
            self.active_behaviors.remove(behavior)
