"""Starter Python-programmet på Raspberry Pi'en"""
from PLAB.reflectance_sensors import *
import time

if __name__ == "__main__":
    ir_sensor = ReflectanceSensors(True)
    while True:
        print("klar")
        time.sleep(3.0)
        print("sjekker...")
        ir_sensor.update()
        value = ir_sensor.get_value()
        print(value)