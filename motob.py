"""Motob klassen"""


class Motob:
    """Motob klassen"""

    def __init__(self, motors=()):
        """
        1. motors - a list of the motors whose settings will be determined by the motob.
        2. value - a holder of the most recent motor recommendation sent to the motob
        """
        self.value = None
        self.motors = motors

    def update(self):
        """
        Update - receive a new motor recommendation, load it into the value slot, and operationalize it.
        """
        # TODO: Skrive metoden

    def operationalize(self):
        """
        Operationalize - convert a motor recommendation into one or more motor settings, which
        are sent to the corresponding motor(s).
        """
        # TODO: Skrive metoden