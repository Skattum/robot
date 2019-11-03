"""Docstring"""
from PLAB.reflectance_sensors import *

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


class Line_sensob(Sensob):
    """Sjekker om roboten er sentrert på linjen"""

    ir_sensor = ReflectanceSensors(True)
    ir_sensor.setup()
    values = ir_sensor.update()
    print(values)