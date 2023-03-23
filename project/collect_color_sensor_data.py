#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor
from time import sleep


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"
DELAY_SEC=1.5
# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(2)
TOUCH_SENSOR = TouchSensor(1)
wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE,"w")
        sleep(1)
        while True:
            if TOUCH_SENSOR.is_pressed():
                cs_output = COLOR_SENSOR.get_rgb()
                if None not in cs_output:
                    print(cs_output)
                    #FIX FORMAT HERE
                    output_file.write(f"{cs_output}\n")
                else:
                    print("scrap")
                sleep(DELAY_SEC)
            
    except BaseException:
        print("exited on exception")
        pass
    #fix exit here
    finally:
        output_file.close()


if __name__ == "__main__":
    collect_color_sensor_data()
