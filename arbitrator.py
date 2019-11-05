# pylint: disable=C0301,C0201
"""Arbitrator-klassen"""
import random


class Arbitrator:
    """Arbitrator-klassen"""

    def __init__(self, bbcon):
        """Init"""
        self.bbcon = bbcon

    def choose_action(self):
        """
        Sekker alle active_behaviors og velger en vinner.
        """

        # Lager et dictionary med alle aktive behaviors og deres vekter, anbefalinger og halt_request.
        recommendations = {}
        for bhv_id in range(0, len(self.bbcon.active_behaviors)):
            behavior = self.bbcon.active_behaviors[bhv_id]
            recommendations[bhv_id] = (behavior.weight, behavior.motor_recommendations, behavior.halt_request)
        # Lager en liste med intervaller av lengde lik vekten av hver anbefaling, samt ID'en til anbefalingen.
        intervals = [[0, 0, 0]]
        for key in recommendations.keys():
            start = intervals[-1][1]
            stop = start + recommendations[key][0]
            intervals.append([start, stop, key])
        limit = intervals[-1][1]

        # Velger et tilfeldig tall mellom 0 og den øvre grensen i det siste intervallet.
        # Intervallet dette tallet ligger i blir da vinnerintervallet, og winner blir da ID'en knyttet til dette
        # intervallet.
        ticket = random.uniform(0, limit)
        winner = -1
        for interval in intervals:
            if interval[1] >= ticket > interval[0]:
                winner = interval[2]

        # Returnerer vinnerens motor-anbefaling og halt-request.
        return recommendations[winner][1], recommendations[winner][2]
