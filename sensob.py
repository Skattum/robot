"""Docstring"""


class Sensob:
    """Sensob-klassen"""

    def __init__(self, sensors=()):
        """Init"""
        # TODO: Skrive metoden
        self.sensors = sensors

    def update(self):
        """Poller sensorer for info og lagrer verdiene."""
        # TODO: 1. Polle verdi
        sensor_values = []
        for sensor in self.sensors:
            sensor_values.append(sensor.update())
        return sensor_values
        # TODO: 2. Lagre konvertere verdiene til pre-prosessert sensob-verdi


class CameraSensob(Sensob):




