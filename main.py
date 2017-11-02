from BBCON import BBCON
from Arbitrator import Arbitrator
from Sensob import LookAhead
from Motob import Motob
from Behaviors import Approach, BackOff

bbcon = BBCON()

bbcon.add_behavior(Approach())
bbcon.add_behavior(BackOff())

bbcon.add_sensObj(LookAhead())

bbcon.add_arbitrator(Arbitrator())
bbcon.add_mot_obj(Motob())

while(True):
    bbcon.run_one_timestep()
    motor_recommendation = bbcon.Arbitrator.chooseBest()
    bbcon.Mot_Objs.apply_motor_recommendation()
