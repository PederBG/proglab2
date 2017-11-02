from BBCON import BBCON

bbcon = BBCON()
bbcon.add_behavior()
bbcon.add_behavior()
bbcon.add_sensObj()
bbcon.add_arbitrator()
bbcon.add_mot_obj()

while(True):
    bbcon.run_one_timestep()
