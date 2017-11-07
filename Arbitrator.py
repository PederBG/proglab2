## The motor object (motob) manifests an interface between a behavior and one or more motors (a.k.a. actuators)

import operator

class Arbitrator():

    def __init__(self, active_behaviors):
        self.behaviors = {"Approach": 0, "BackOff": 0}
        self.active_behaviors = active_behaviors

    def update(self):
        for behavior in self.active_behaviors:
            behavior.update()
            self.behaviors[behavior.get_name()] = behavior.get_priority_weight()

    def choose_best(self):
        self.update()
        sorted_behaviors = sorted(self.behaviors.items(), key=operator.itemgetter(1))
        name = sorted_behaviors[-1][0]
        for behavior in self.active_behaviors:
            if behavior.get_name() == name:
                return behavior.get_action_rec()
