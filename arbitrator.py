"""Arbitrator-klassen"""


class Arbitrator:
    """Arbitrator-klassen"""

    def __init__(self, bbcon):
        """Init"""
        self.bbcon = bbcon

    def choose_action(self):
        """
        Sekker alle active_behaviors og velger en vinner.
        # TODO: Bestemme oss for deterministisk eller stokastisk metode.
        """
        for behavior in self.bbcon.active_behaviors:


