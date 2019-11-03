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
        recommendations = {}
        behavior_id = 0
        intervals = [[0, 0, 0]]
        for behavior in self.bbcon.active_behaviors:
            recommendations[behavior_id] = (behavior.weight, behavior.motor_recommandations, behavior.halt_request)
            behavior_id += 1
        for key in recommendations.keys():
            a = intervals[-1][1]
            b = a + recommendations[key][0]
            intervals.append([a, b, key])
        limit = intervals[-1][1]
        ticket = random.uniform(0, limit)
        winner = -1
        for interval in intervals:
            if interval[1] >= ticket > interval[0]:
                winner = interval[2]
        print(recommendations[winner])
        return recommendations[winner][1]
