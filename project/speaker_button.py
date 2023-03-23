#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors, Motor
from time import sleep


MOTOR_A = Motor("A")
MOTOR_B = Motor("B")
MOTOR_C = Motor("C")
MOTOR_D = Motor("D")

wait_ready_sensors() # Note: Touch sensors actually have no initialization time


def play_sound_1():
    "Play a single note."
    SOUND.play()
    SOUND.wait_done()

def play_sound_2():
    "Play a single note."
    SOUND2.play()
    SOUND2.wait_done()
def play_sound_3():
    "Play a single note."
    SOUND3.play()
    SOUND3.wait_done()
def play_sound_4():
    "Play a single note."
    SOUND4.play()
    SOUND4.wait_done() 
def play_sound_on_button_press():
    "In an infinite loop, play a single note when the touch sensor is pressed."
    try:
        #infinite while loop
        motorOn= False
        while True:
            #if touch sensor is pressed
                    
            if TOUCH_SENSOR_1.is_pressed():
                sleep(0.15)
                if TOUCH_SENSOR_2.is_pressed():
                    print("Drumming switch")
                    if motorOn:
                        MOTOR.set_power(0)
                        motorOn= False
                    else:
                        MOTOR.set_power(100)
                        motorOn= True
                    sleep(0.5)
                else:
                    print("sound 1")
                    play_sound_1()
                    
            if TOUCH_SENSOR_2.is_pressed():
                sleep(0.15)
                if TOUCH_SENSOR_1.is_pressed():
                    print("Drumming switch")
                    if motorOn:
                        MOTOR.set_power(0)
                        motorOn= False
                    else:
                        MOTOR.set_power(100)
                        motorOn= True
                    sleep(0.5)
                else:
                    print("sound 2")
                    play_sound_2()
            if TOUCH_SENSOR_3.is_pressed():
                sleep(0.15)
                if TOUCH_SENSOR_4.is_pressed():
                #call play_sound() to have the speaker play a sound
                    print("emergency stop") 
                    MOTOR.set_power(0)
                    sleep(0.5)
                    exit()
                else:
                    play_sound_3()
                    print("souund 3 inside loop")
                    
            if TOUCH_SENSOR_4.is_pressed():
                sleep(0.15)
                if TOUCH_SENSOR_3.is_pressed():
                    print("emergency stop")
                    MOTOR.set_power(0)
                    sleep(0.5)
                    exit()

                else:
                    print("sound 4")
                    play_sound_4()
            
            
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        MOTOR.set_power(0)
        print("exception")
        sleep(0.5)
        exit()

def move():
    MOTOR_D.set_power(20)
    sleep(0.7)
    MOTOR_D.set_power(0)

def drop_cube():
    MOTOR_A.set_power(20)
    sleep(1)
    MOTOR_A.set_power(-20)
    sleep(1.5)
    MOTOR_A.set_power(20)
    sleep(0.5)
    MOTOR_A.set_power(0)
    
def push_cubes(cubes):
    if cubes == 5:
        print(cubes)
        #length 5 blocks
        MOTOR_B.set_power(-20)
        MOTOR_C.set_power(-20)
        sleep(2.6)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(1)
        MOTOR_B.set_power(20)
        MOTOR_C.set_power(20)
        sleep(2.7)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(2)
        
    elif cubes == 4:
        print(cubes)
        #length 4 blocks
        MOTOR_B.set_power(-20)
        MOTOR_C.set_power(-20)
        sleep(2.1)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(1)
        MOTOR_B.set_power(20)
        MOTOR_C.set_power(20)
        sleep(2.2)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(2)
        
    elif cubes == 3:
        print(cubes)
        #length 3 blocks
        MOTOR_B.set_power(-20)
        MOTOR_C.set_power(-20)
        sleep(1.6)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(1)
        MOTOR_B.set_power(20)
        MOTOR_C.set_power(20)
        sleep(1.7)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(2)
        
    elif cubes == 2:
        print(cubes)
        #length 2 blocks
        MOTOR_B.set_power(-20)
        MOTOR_C.set_power(-20)
        sleep(1.1)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(1)
        MOTOR_B.set_power(20)
        MOTOR_C.set_power(20)
        sleep(1.2)
        MOTOR_B.set_power(0)
        MOTOR_C.set_power(0)
        sleep(2)
        
    else:
        print(cubes)
        
if __name__=='__main__':
    #for x in range(5):
        #drop_cube()
    #exit()
    drop_cube()
    push_cubes(5)
    
    drop_cube()
    push_cubes(4)
    
    drop_cube()
    push_cubes(3)
    
    drop_cube()
    push_cubes(2)
    
    drop_cube()
    push_cubes(1)