"""Starter Python-programmet på Raspberry Pi'en"""
from bbcon import BBCON
from sensob import *
from behavior import *
from motob import Motob
from supply_files.reflectance_sensors import ReflectanceSensors
from supply_files.zumo_button import ZumoButton
from supply_files.motors import Motors
import wiringpi as wp
import time

if __name__ == "__main__":
    """
    Bruker denne filen til å sette opp roboten og starte den.
    Her er også flere av instillingene samlet.
    """
    reflective_sensor = ReflectanceSensors(False, 130, 3600)

    sensobs = {
        "s_line": StopLineSensob(reflective_sensor),
        "r_line": RightLineSensob(reflective_sensor),
        "l_line": LeftLineSensob(reflective_sensor)
    }

    commands = {
        # Et dictionary vi kan bruke til å sette og justere de forskjellige motorkommandoene.
        #
        # key:    Navnet på kommandoen/recommendation
        # value:  Verdien som blir sent til motoren som argument i motors.set_value()
        
        "forward": [0.4, 0.4],
        "adjust right": [.7, -.4],
        "adjust left": [-.4, .7],
        "stop": [0, 0]
    }

    config_values = {
        # Et dictionary vi kan bruke til å sette og justere forskjellige variabler, primært for Sensobs.
        #
        # key:    Navnet på variabelen
        # value:  Verdien til variabelen

        "left_line_tresh": .7,
        "right_line_tresh": .7,
        "stop_line_tresh": .7
    }

    autorun = True  # True: kjører roboten uten å vente på knappetrykk

    if autorun:
        wp.wiringPiSetupGpio()
    else:
        ZumoButton().wait_for_press()

    motors = Motors()
    motob = Motob(motors, commands)

    prios = {
        "carry_on": 1
    }

    bbcon = BBCON(config_values, motob)

    behaviors = {
        "carry_on": CarryOn(bbcon, (sensobs[key] for key in ["l_line", "s_line", "r_line"]), True, prios["carry_on"])
    }

    bbcon.add_behavior(behaviors["carry_on"])

    for sensob in sensobs.values():
        bbcon.add_sensob(sensob)

    while True:
        bbcon.run_one_timestep()
