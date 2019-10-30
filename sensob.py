from PLAB.ultrasonic import Ultrasonic
from PLAB.reflectance_sensors import ReflectanceSensors
from PLAB.camera import Camera


class Sensob:

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


class UltrasonicSensob(Sensob):

    def __init__(self):
        super().__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].get_value()
        print("Ultrasonic: ", self.value)
        return self.value


class ReflectanceSensob(Sensob):

    def __init__(self):
        super().__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].get_value()
        print("Reflectance: ", self.value)
        return self.value


class CameraSensob(Sensob):
    def __init__(self):
        super().__init__()
        self.camera_obj = Camera()
        self.sensors = [self.camera_obj]

    def rgb(self, img):
        rgb_list = [0,0,0]

        for x in range(40,80):
            for y in range(40,50):
                band = img.getpixel((x,y))
                rgb_list[0] += band[0]
                rgb_list[1] += band[1]
                rgb_list[2] += band[2]
        tot = sum(rgb_list)
        rgb_list[0] = rgb_list[0] / tot
        rgb_list[1] = rgb_list[1] / tot
        rgb_list[2] = rgb_list[2] / tot

        return rgb_list

    def update(self):
        self.value = self.rgb(self.sensors[0].update())
        print("Camera: ", self.value)
        return self.value
