"""Starter Python-programmet på Raspberry Pi'en"""
from PLAB.reflectance_sensors import *
import time

if __name__ == "__main__":
    ir_sensor = ReflectanceSensors(True)
    ir_sensor.setup()
    while True:
        print("klar")
        time.sleep(3.0)
        print("sjekker...")
        values = ir_sensor.update()
        print(values)