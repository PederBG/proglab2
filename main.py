from BBCON import BBCON
from Arbitrator import Arbitrator
from Sensob import LookAhead

bbcon = BBCON()
bbcon.add_behavior()
bbcon.add_behavior()
bbcon.add_sensObj(LookAhead())
bbcon.add_arbitrator(Arbitrator())
bbcon.add_mot_obj()

while(True):
    bbcon.run_one_timestep()
