
## The motor object (motob) manifests an interface between a behavior and one or more motors (a.k.a. actuators)

from Proglab2.Øving6.Proglab6.BBCON import BBCON
import operator

class arbitrator():

    def __init__(self):
        self.behaviors = {"Approche": 0, "Back Off": 0}
        self.BBCONsActive_behaviors = BBCON.Active_behaviors




    def uppdate(self):
        for behaveObj in self.BBCONsActive_behaviors:
            self.behaviors[behaveObj.getname] += behaveObj.getValue

    def chooseBest(self):
        sortedBehaviors = sorted(self.behaviors.items(), key=operator.itemgetter(1))
        name = sortedBehaviors[-1][0]
        for behavior in self.BBCONsActive_behaviors:
            if behavior.getName() == name:
                return behavior.recomondation()





