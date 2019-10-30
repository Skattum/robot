
"""Hovedklasse for kontroller"""


class BBCON:
    """Behavoir-Based Controller-klasse"""

    def __init__(self, behaviors=None, sensobs=None, motobs=None, arbitrator=None):
        """
        Init
        :param behaviors: liste med alle tilhørende handlinger til roboten
        :param sensobs: liste med alle sensob-ene til roboten
        :param motobs:  liste med alle motobs-ene til roboten
        :param arbitrator: arbitrator-en som BBCON-en knyttes til
        """

        self.behaviors = behaviors
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator

    def add_behavior(self, behavior):
        """ Legger til en nylig lagd handling til behaviors-listen """
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        """ Legger til en nylig lagd sensob til sensob-listen"""
        self.sensobs.append(sensob)

    def active_behavior(self, behavior):
        """Legger til en eksisterende handling til listen med aktive handlinger"""
        self.active_behaviors.append(behavior)

    def deactive_behavior(self,behavior):
        """Fjerner en tidligere aktiv handling fra listen med aktive handliner"""
        self.active_behaviors.remove(behavior)

    def run_one_timestep(self):

        # 1. Ber alle sensob oppdatere seg seg
        for sensob in self.sensobs:
            sensob.update()

        # 2. Ber alle behavior oppdatere seg selv, og legger til i riktige lister dersom de nå har endret status fra aktiv til ikke aktiv, eller motsatt.
        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag and behavior not in self.active_behaviors:
                self.active_behavior(behavior)
            elif not behavior.active_flag and behavior in self.active_behaviors:
                self.deactive_behavior(behavior)
        # 3. Result består av den vinnende handlingen, som arbitrator-en bestemmer i sin choose_action-metode,
        # sin motorandbefaling og halt request flag, av typen, [motorandbefaling, halt request flag =True/False]
        result = self.arbitrator.choose_action()

        # 4. Oppdatere alle motobs
        if result[1]:                   #Dersom den vinnende handlingen har halt_request = True, så skal BBCON avslutte og returnere True
            return True                 #slik at roboten kjører så lenge
        for motob in self.motobs:
            motob.update(result[0])     #Oppdaterer alle motob-ene med andbefalingene

        #




        # TODO: 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        # TODO: 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
        # TODO: 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        # TODO: 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.
        pass



    















