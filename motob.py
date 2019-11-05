# pylint: disable=C0301, C0201, R0902
"""Motob-klassen"""
from supply_files.motors import Motors
import time

class Motob:
    """Motob-klassen"""
    def __init__(self, motors, commands):
        """Init"""
        self.motors = motors
        self.recommendation = None
        self.value = []
        self.time = 0

        self.commands = commands

    def update(self, recommendation):
        """Tar inn en recommendation, lagrer den og sender til operationalize"""
        self.recommendation = recommendation
        self.value = self.commands[recommendation][0:2]
        self.time = self.commands[recommendation][2]
        self.operationalize()

    def operationalize(self):
        self.motors.set_value(self.value)
        if self.time > 0:
            time.sleep(self.time)
