"""Motob klassen"""


class Motob:
    """Motob klassen"""

    def __init__(self, motors=None):
        """
        :param motors - a list of the motors whose settings will be determined by the motob.
        : value - a holder of the most recent motor recommendation sent to the motob
        """
        if motors is None:
            motors = []
        self.value = None
        self.motors = motors

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
        # TODO: Skrive metoden
