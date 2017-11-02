## The motor object (motob) manifests an interface between a behavior and one or more motors (a.k.a. actuators)

import operator

class Arbitrator():

    def __init__(self, BBCONActiveBehaviors):
        self.behaviors = {"Approach": 0, "Back Off": 0}
        self.BBCONsActive_behaviors = BBCONActiveBehaviors

    def update(self):
        for behaveObj in self.BBCONsActive_behaviors:
            self.behaviors[behaveObj.getname] = behaveObj.getValue

    def chooseBest(self):
        self.update()
        sortedBehaviors = sorted(self.behaviors.items(), key=operator.itemgetter(1))
        name = sortedBehaviors[-1][0]
        for behavior in self.BBCONsActive_behaviors:
            if behavior.getName() == name:
                return behavior.recomondation()
