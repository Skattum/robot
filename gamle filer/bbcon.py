"""Hovedklasse for kontroller"""
from arbitrator import Arbitrator
from behavior import *
from PLAB.camera_sensob import CameraSensob
from PLAB.irproximity_sensor import irproximity_sensor
from motob import Motob
from PLAB.motors import Motors
from PLAB.reflectance_sensob import ReflectanceSensob
from PLAB.ultrasonic import Ultrasonic
from PLAB.zumo_button import ZumooButton


class BBCON:
    """Behavoir-Based Controller-klasse"""

    def __init__(self):
        """
        Init
        :param behaviors: liste med alle tilhørende handlinger til roboten
        :param sensobs: liste med alle sensob-ene til roboten
        :param motobs:  liste med alle motobs-ene til roboten
        :param arbitrator: arbitrator-en som BBCON-en knyttes til
        """

        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self)
        self.behavior_prios = {'goPri': 1, 'whitePri': 2, 'collitionPri': 4}

        self.behavior_values = {
                                'motor_duration': 0.5,
                                'min_distance': 5.0,
                                'backwards': [-1,-1],
                                'forward': [1,1],
                                'blue_tresh': 0.95
                                }



    def add_behavior(self, behavior):
        """ Legger til en nylig lagd handling til behaviors-listen """
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        """ Legger til en nylig lagd sensob til sensob-listen"""
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def active_behavior(self, behavior):
        """Legger til en eksisterende handling til listen med aktive handlinger"""
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactive_behavior(self,behavior):
        """Fjerner en tidligere aktiv handling fra listen med aktive handliner"""
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):

        # 1. Ber alle sensob oppdatere seg seg
        for sensob in self.sensobs:
            sensob.update()

        # 2. Ber alle behavior oppdatere seg selv, og legger til i riktige lister dersom de nå har endret status fra aktiv til ikke aktiv, eller motsatt.
        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag:
                self.active_behavior(behavior)
            else:
                self.deactive_behavior(behavior)
        recommendations, stop = self.arbitrator.choose_action()
        print("recommendations from arbitrator", recommendations[i])
        for i in range(len(self.motobs)):
            print("recommendations i", recommendations[i])
        for sensob in self.sensobs:
            sensob.reset()



    def add_motob(self):
        print("Inside add motod")
        motor = Motors()
        motor.forward(0.25, 1.0)
        print("drive forward")
        motob = Motob(motor, self)
        self.motobs.append(motob)

    def main(self):
        zumo = ZumooButton()
        zumo.wait_for_press()
        print("main:))")
        self.add_motob()
        ultrasonic = Ultrasonic()
        irsensor = ReflectanceSensob()
        camera = CameraSensob()
        go = Go(self)
        collide = AvoidCollision(self, ultrasonic)
        white = AvoidWhiteline(self, irsensor)
        stop = Stop(camera)
        self.sensobs.append(ultrasonic)
        self.sensobs.append(irsensor)
        self.sensobs.append(camera)
        self.behaviors.append(go)
        self.behaviors.append(collide)
        self.behaviors.append(white)
        self.behaviors.append(stop)
        while True:
            self.run_one_timestep()
            print("run")


if __name__ == "__main__":
    bbcon == BBCON()
    bbcon.main()




    















