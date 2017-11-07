from BBCON import BBCON
from Arbitrator import Arbitrator
from Motob import Motob
from Behaviors import Approach, BackOff

bbcon = BBCON()
arbitrator = Arbitrator()
motob = Motob()
approach = Approach()
back_off = BackOff()

bbcon.set_arbitrator(arbitrator)
bbcon.set_motob(motob)
bbcon.add_behavior(approach)
bbcon.add_behavior(back_off)
bbcon.add_active_behavior(approach)
bbcon.add_active_behavior(back_off)

while(True):
    bbcon.run_one_timestep()

