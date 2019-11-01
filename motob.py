from PLAB.motors import Motors
from arbitrator import Arbitrator
"""Motob klassen"""

class Motob:
    """Motob klassen"""

    def __init__(self, motors):
        """
        :param motors - a list of the motors whose settings will be determined by the motob.
        : value - a holder of the most recent motor recommendation sent to the motob
        """
        motors = []
        self.value = None

    def update(self, new_motor_recommendation):
        """
        Update - receive a new motor recommendation, load it into the value slot, and operationalize it.
        """
        self.value = new_motor_recommendation
        self.operationalize()

    def operationalize(self):
        """
        Operationalize - convert a motor recommendation into one or more motor settings, which
        are sent to the corresponding motor(s).
        """
        motor = Motors()
        motor.set_value(self.value, 0.5)

        for i in range len(self.motors):


"""
    def recommendation_to_motor(self, motor_reccomendation):
        Appropriate motor reccomendations are sent to appropriate motor

        if motor_reccomendation[0] == ''
        elif motor_reccomendation[0] == ''
        elif motor_reccomendation[0] == ''
"""

