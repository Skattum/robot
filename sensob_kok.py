from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors

class Sensob_kok:


    def __init__(self):
        self.sensors = [] #inneholder instanser av sensor_wrapper
        self.value = None

    def update(self):
        pass

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset() #alle sensorer har en reset metode

class UltrasonicSensob(Sensob_kok):

    def __init__(self):
        super().__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].get_value()
        print("Ultrasonic: ", self.value)
        return self.value

class ReflectanceSensob(Sensob_kok):

    def __init__(self):
        super().__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].get_value()
        print("Reflectance: ", self.value)
        return self.value




