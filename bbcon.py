# pylint: disable=C0301, C0201, R0902
"""Hovedklasse for kontroller"""
from arbitrator import Arbitrator
from motob import Motob
import time


class BBCON:
    """Behavoir-Based Controller-klasse"""

    def __init__(self, config_values, motob):
        """
        Init
        """

        self.config_values = config_values
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motob = motob
        self.arbitrator = Arbitrator(self)
        self.rages = 0

    def add_behavior(self, behavior):
        """ Legger til en nylig lagd handling til behaviors-listen """
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        """ Legger til en nylig lagd sensob til sensob-listen"""
        self.sensobs.append(sensob)
        sensob.bbcon = self

    def active_behavior(self, behavior):
        """Legger til en eksisterende handling til listen med aktive handlinger"""
        self.active_behaviors.append(behavior)

    def deactive_behavior(self, behavior):
        """Fjerner en tidligere aktiv handling fra listen med aktive handliner"""
        self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """Loopen"""
        # 2. Ber alle behavior oppdatere seg selv, og legger til i riktige lister
        #    dersom de nå har endret status fra aktiv til ikke aktiv, eller motsatt.
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
        if result[1]:  # Dersom vinnende handling har halt_request = True, så skal BBCON avslutte og returnere True
            self.motob.update("stop")
            return True  # slik at roboten kjører så lenge
        print("Anbefaler: " + result[0])
        self.motob.update(result[0])  # Oppdaterer alle motob-ene med anbefalingene

        time.sleep(0.1)
