from BBCON import BBCON
from Arbitrator import Arbitrator
from Motob import Motob
from Behaviors import Approach, DetectEdge, ApproachRed
from lib.zumo_button import ZumoButton

bbcon = BBCON()
arbitrator = Arbitrator()
motob = Motob()
approach = Approach()
button = ZumoButton

bbcon.set_arbitrator(arbitrator)
bbcon.set_motob(motob)
bbcon.add_behavior(approach)

bbcon.add_active_behavior(approach)

button.wait_for_press()
while(True):
    bbcon.run_one_timestep()

