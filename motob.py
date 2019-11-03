"""Motob-klassen"""
from supply_files.motors import Motors


class Motob:
    """Motob-klassen"""
    def __init__(self, motors, commands):
        """Init"""
        self.motors = motors
        self.value = []

        self.commands = commands

    def update(self, recommendation):
        """Tar inn en recommendation, lagrer den og sender til operationalize"""
        self.value = self.commands[recommendation]
        self.operationalize()

    def operationalize(self):
        self.motors.set_value(self.value)
