#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, Motor, BP
from time import sleep

DURATION = 0.3
VOLUME=100
SOUNDA = sound.Sound(duration=DURATION, pitch="A4", volume=VOLUME)
SOUNDB = sound.Sound(duration=DURATION, pitch="F5", volume=VOLUME)
SOUNDC = sound.Sound(duration=DURATION, pitch="D5", volume=VOLUME)
SOUNDD = sound.Sound(duration=DURATION, pitch="B5", volume=VOLUME)
TOUCH_SENSORA = TouchSensor(1)
TOUCH_SENSORB = TouchSensor(2) # 1 and 2 at the same time will trigger SOUNDD
TOUCH_SENSORC = TouchSensor(3)
TOUCH_SENSORD = TouchSensor(4) # this is the emergency stop sensor
NXT_MOTOR = Motor("C")
POWER_LIMIT = 50
SPEED_LIMIT = 720
DELAY = 0.2


wait_ready_sensors(True) # Note: Touch sensors actually have no initialization time


def play_sound(SOUND):
    "Play a single note."
    SOUND.play()
    SOUND.wait_done()


def play_sound_on_button_press():
    "In an infinite loop, play a single note when the touch sensor is pressed."
    try:
        NXT_MOTOR.reset_encoder()
        NXT_MOTOR.set_limits(POWER_LIMIT, SPEED_LIMIT)
        NXT_MOTOR.set_power(0)
        drumming = False
        while True:
            # check for press, then play sound or emergency stop
            if TOUCH_SENSORD.is_pressed():
                # D is the emergency stop. Break from this process and stop motor
                NXT_MOTOR.set_dps(0)
                NXT_MOTOR.set_limits(POWER_LIMIT, 0)
                drumming = False
            if TOUCH_SENSORA.is_pressed() and not TOUCH_SENSORB.is_pressed() and not TOUCH_SENSORC.is_pressed():
                # ensure ONLY touch sensor A is pressed
                print("soundA playing")
                play_sound(SOUNDA)
            if TOUCH_SENSORB.is_pressed() and not TOUCH_SENSORA.is_pressed() and not TOUCH_SENSORC.is_pressed():
                # ensure ONLY touch sensor B is pressed
                print("soundB playing")
                play_sound(SOUNDB)
            if TOUCH_SENSORC.is_pressed() and not TOUCH_SENSORA.is_pressed() and not TOUCH_SENSORB.is_pressed():
                print("soundC playing")
                play_sound(SOUNDC)
            
            if TOUCH_SENSORA.is_pressed() and TOUCH_SENSORB.is_pressed() and not TOUCH_SENSORC.is_pressed():
                # this is where we will start our drumming
                print("soundD playing")
                play_sound(SOUNDD)
            if not TOUCH_SENSORA.is_pressed() and TOUCH_SENSORB.is_pressed() and TOUCH_SENSORC.is_pressed() and not drumming:
                print("Already drumming")
                drumming = True
                NXT_MOTOR.set_dps(400)
                NXT_MOTOR.set_limits(POWER_LIMIT, 400)
            # sleep for delay amounnt of seconds
            sleep(DELAY)
    except BaseException as e:
        print(e)  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        BP.reset_all()
    finally:    
        BP.reset_all()

if __name__=='__main__':

    # TODO Implement this function
    play_sound_on_button_press()
