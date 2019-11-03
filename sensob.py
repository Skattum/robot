"""Sensob-klassen"""


class Sensob:
    """Sensob-klassen"""

    def __init__(self, sensors, bbcon=None):
        """
        :param sensors: Én eller flere sensorer.
        """
        self.sensors = [sensors]
        self.value = None
        self.bbcon = None

    def update(self):
        """Henter alle verdiene fra hver sensor"""
        values = []
        for sensor in self.sensors:
            sensor.update()
            values.append(sensor.get_value())
        self.compute(values)

    def compute(self, values):
        """Bruker sensorenes verdier til noe nyttig"""
        pass


class DistanceSensob(Sensob):
    """Sensob som målet avstanden til objekt foran."""

    def __init__(self, sensors):
        """Init"""
        super().__init__(sensors)

    def compute(self, values):
        self.value = values[0]


class StopLineSensob(Sensob):
    """
    Sjekker om roboten har kommet til en svart linje rett foran.
    Hvis ja, setter den self.value til True
    """

    def __init__(self, sensors):
        """Init"""
        super().__init__(sensors)

    def compute(self, values):
        self.value = False
        val_sum = 0
        for val in values[0]:
            val_sum += val

        treshold = self.bbcon.config_values["stop_line_tresh"]
        self.value = True if (val_sum / 6) < treshold else self.value

        for sensor in self.sensors:
            sensor.reset()


class RightLineSensob(Sensob):
    """
    Sjekker om roboten har kommet til en svart linje på høyre side.
    Hvis ja, setter den self.value til True
    """

    def __init__(self, sensors):
        """Init"""
        super().__init__(sensors)

    def compute(self, values):
        treshold = self.bbcon.config_values["right_line_tresh"]
        self.value = True if values[0][5] < treshold else False

        for sensor in self.sensors:
            sensor.reset()


class LeftLineSensob(Sensob):
    """
    Sjekker om roboten har kommet til en svart linje på venstre side.
    Hvis ja, setter den self.value til True
    """

    def __init__(self, sensors):
        """Init"""
        super().__init__(sensors)

    def compute(self, values):
        treshold = self.bbcon.config_values["left_line_tresh"]
        self.value = True if values[0][0] < treshold else False

        for sensor in self.sensors:
            sensor.reset()
