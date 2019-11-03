"""henter verdier fra sensorer"""
from bbcon import BBCON
from sensob import *
from behavior import *
from supply_files.ultrasonic import Ultrasonic
from supply_files.reflectance_sensors import ReflectanceSensors
from supply_files.motors import *
from supply_files.zumo_button import ZumoButton
from supply_files.robodemo import dancer
import time
import wiringpi as wp
from motob import Motob


if __name__ == "__main__":
    refsens = ReflectanceSensors(True)
    ZumoButton().wait_for_press()
    wp.wiringPiSetupGpio()
    # m = Motors()
    # m.set_value([0.7, -0.4], 0.2)
    # m.set_value([-0.4, 0.7], 0.2)
    motob = Motob()
    motob.commands["adjust left"]

    """
    for i in range(0, 50):
        x = refsens.update()
        refsens.reset()
        y = []
        for val in x:
            y.append(val.__round__(2))
        print(y)
        time.sleep(.1)
    m.stop()
    """
