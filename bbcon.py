


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

    def run_one_timestep(self):
        # TODO
        # 1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along with any pre-processing of those values (as described below)
        # 2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor recommendation.
        # 3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and return that behavior’s motor recommendations and halt request flag.
        # 4. Update the motobs based on these motor recommendations. The motobs will then update the settings of all motors.
        # 5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
        # 6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.
        pass















