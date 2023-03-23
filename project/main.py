#!/usr/bin/env python3

"""
This is the python script that operates our final design.

Authors: Evan Boyd, Sahar Fathi, Jean Kaznji, Shyam Desai
"""

# imports 
from utils.brick import TouchSensor, wait_ready_sensors, Motor, BP, EV3ColorSensor
from time import sleep
from math import sqrt
from color_detection import color_detection_drive, color_detection_delivery # imports for all of our color functionalities
import sys

# BEGINNING OF CONSTANTS

SLEEP = 0.1 # main run while loop sleep delay
DRIVING_COLOR_SENSOR = EV3ColorSensor(2) # at front to control driving
DELIVERY_COLOR_SENSOR = EV3ColorSensor(1) # detects delivery zones
TS = TouchSensor(3) # touch sensor for stop start
wait_ready_sensors(True)
LEFT_WHEEL_MOTOR = Motor('A')
RIGHT_WHEEL_MOTOR = Motor('B')
ROTATING_PLATFORM_MOTOR = Motor('C')
TRAP_DOOR_MOTOR = Motor('D')


MOTOR_POWER_LIMIT = 80 # Power limit for all motors
MOTOR_SPEED_LIMIT = 300 # speed limit for all motors

WHEEL_SPEED = 100 # default wheel speed (dps)
WHEEL_DELTA_SPEED = 150 # how much we speed up by when making a turn (dps)

ROTATING_PLATFORM_SPEED = 300 # how fast the rotating platform spins (dps)
TRAP_DOOR_SPEED = 300 # how fast the trap door opens and closes (dps)


# *** CONSTANTS FOR ROTATING THE ROTATING PLATFORM BASED ON OUR TESTS ***
RED_DEGREES = 0
ORANGE_DEGREES = 47
YELLOW_DEGREES = 92
GREEN_DEGREES = 137
BLUE_DEGREES = 182
PURPLE_DEGREES = 227

def init_motor(motor):
    """
    function to initialize the motors used by our design. Sets the speed
    and power limits based on which motor has been passed to this function,
    and according to the CONSTANTS that we've set.
    """
    try:
        # reset and then set our power to what we need
        motor.reset_encoder()
        motor.set_limits(MOTOR_POWER_LIMIT, MOTOR_SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)
        
def open_trap_door():
    """
    Function to open and close the trap door of our design.
    -180 means it is fully opened, 10 means fully closed.
    This function is called once a cube has been rotated to be above the trap door.
    """
    TRAP_DOOR_MOTOR.set_position(-180)
    sleep(1)
    TRAP_DOOR_MOTOR.set_position(10)    
    sleep(1)


    
def drive():
    """
    Controller for driving our robot. This is called continuously from the main while
    loop in the run function. Keep track
    """
    global green_counter # counts the # of green zones detected
    global prev_color # previous color detected by the driving color sensor
    global delivering # heading out to 6 delivery zones vs back to loading bay; determines which way we need to turn
    global looking #looking for a delivery zone (set to true once green has been detected)
    global driving
    global left_delivery_zone
    

    # perform driving if in the driving state
    if driving:

        # constantly poll the color sensors
        driving_rgb = DRIVING_COLOR_SENSOR.get_rgb()
        delivery_rgb = DELIVERY_COLOR_SENSOR.get_rgb()
        driving_color_detected = ""
        color_deliv_box=""
        if None not in driving_rgb:
            driving_color_detected = color_detection_drive(driving_rgb)
        delivery_color_detected = ""
        if None not in delivery_rgb:
            delivery_color_detected = color_detection_delivery(delivery_rgb)
        
        print(delivery_color_detected)
        print(looking)
        
        if looking and delivery_color_detected != "white":
            left_delivery_zone = False
            print(delivery_rgb)
            color_deliv_counter = 0
            list_deliv_colors = []
            rgb = DELIVERY_COLOR_SENSOR.get_rgb()
            while (color_deliv_counter<9):
                list_deliv_colors.append(color_detection_delivery(rgb))
                print(color_detection_delivery(rgb))
                color_deliv_counter+=1
            
            color_deliv_box = find_avg_color(list_deliv_colors)
            perform_delivery(color_deliv_box)
            left_delivery_zone = True
            
        if looking and left_delivery_zone == True and delivery_color_detected == "white":
            #perform_delivery(color_deliv_box)
            print("dropping")
             
#         if looking and delivery_color_detected != "white":
#             # carry out the delivery according to the color of the delivery zone detected
#             print(delivery_rgb)
#             color_deliv_counter = 0
#             list_deliv_colors = []
#             rgb = DELIVERY_COLOR_SENSOR.get_rgb()
#             while (color_deliv_counter<9):
#                 list_deliv_colors.append(color_detection_delivery(rgb))
#                 print(color_detection_delivery(rgb))
#                 color_deliv_counter+=1
#             
#             color_deliv_box = find_avg_color(list_deliv_colors)
#             perform_delivery(color_deliv_box)
            
            
                
        if driving_color_detected == "blue":
            # blue is on the left when delivering, so turn right
            if delivering:    
                turn_right()
            else:
                turn_left()
            # increment the number of delivery zones (if necessary)
            count_delivery_zones()
            start_looking()
            # set the previous color (allows us to detected green strip delivery zones)
            prev_color = "blue"
        elif driving_color_detected == "red":
            # red and delivering, so turn left
            if delivering:
                turn_left()
            else:
               turn_right()
            # increment the number of delivery zones (if necessary)
            count_delivery_zones()
            start_looking()
            prev_color = "red"
        elif driving_color_detected == "white":
            # white, so we continue straight
            continue_straight()
            # increment the number of delivery zones (if necessary)
            count_delivery_zones()
            start_looking()
            prev_color = "white"
        elif driving_color_detected == "green":
            # time to begin looking for a delivery zone
            prev_color = "green"
        elif driving_color_detected == "yellow" and not delivering:
            # we've seen yellow, so now it is time to rotate the opposite direction and stop driving
            rotate_robot(True)
            delivering = True
            driving = False
                
            
    else:
        # we're not in the driving state as the driving boolean is not true
        # stop the robot
        stop()

def start_looking():
    global prev_color
    global looking
    if prev_color == "green":
        looking = True
        
def find_avg_color(lst):
    color_counter = [lst.count("red"), lst.count("orange"), lst.count("yellow"),
                     lst.count("green"), lst.count("blue"), lst.count("purple")]
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    maximum = color_counter.index(max(color_counter))
    return color_list[maximum]

def rotate_robot(at_loading_bay):
    """
    function to robot to be within the track. Takes an input boolean
    to know if we're at the loading bay and then perform the corresponding rotation. 
    """
    while True:
        # set the motors to go in opposite directions
        LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
        RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
        rgb = DRIVING_COLOR_SENSOR.get_rgb()
        new_driving_color_detected = ""
        if None not in rgb:
            new_driving__color_detected = color_detection_drive(rgb)
        if new_driving_color_detected == "red" and not at_loading_bay:
            stop()
            sleep(1)
            break
        elif new_driving_color_detected == "blue" and at_loading_bay:
            # stop once we see blue when we're performing a rotation at the loading bay.
            stop()
            while True:
                # we've seen blue, now we want to rotate until we see white
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
                rgb = DRIVING_COLOR_SENSOR.get_rgb()
                new_driving_color_detected = ""
                if None not in rgb:
                    new_driving__color_detected = color_detection_drive(rgb)
                if new_driving__color_detected == "white":
                    stop()
                    break
            sleep(1)
            break
        sleep(SLEEP)

def count_delivery_zones():
    global prev_color
    global green_counter
    global delivering
    if prev_color == "green" and delivering:
        # increment the number of delivery zones we've seen as 
        green_counter += 1  


def stop():
    """
    function to stop the driving of the robot
    """
    LEFT_WHEEL_MOTOR.set_dps(0)
    RIGHT_WHEEL_MOTOR.set_dps(0)
    sleep(1)

def continue_straight():
    """
    function to make the robot go straight depending on wheel speed
    """
    LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
    RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)

def turn_left():
    """
    function that turns the robot left.
    We continuously increase the amount that we're turning by
    """
    left_wheel_speed = LEFT_WHEEL_MOTOR.get_dps()
    # flip the sign to get the left wheel moving in the opposite direction
    if left_wheel_speed > 0:
        left_wheel_speed *= -1
    
    LEFT_WHEEL_MOTOR.set_dps(left_wheel_speed - WHEEL_DELTA_SPEED)
    RIGHT_WHEEL_MOTOR.set_dps(RIGHT_WHEEL_MOTOR.get_dps() + WHEEL_DELTA_SPEED)

def turn_right():
    """
    function that turns the robot right.
    We continuously increase the amount that we're turning by
    """
    LEFT_WHEEL_MOTOR.set_dps(LEFT_WHEEL_MOTOR.get_dps() + WHEEL_DELTA_SPEED)
    right_wheel_speed = RIGHT_WHEEL_MOTOR.get_dps()
    if right_wheel_speed > 0:
        right_wheel_speed *= -1
        
    RIGHT_WHEEL_MOTOR.set_dps(right_wheel_speed - WHEEL_DELTA_SPEED)

def perform_delivery(delivery_color_detected):
    """
    function to perform a delivery based on the color that has been detected
    """
    global green_counter
    global looking
    not_delivered = True
    # stop the driving
    stop()

    while not_delivered:
        # rotate to the corresponding colored cube
        print(delivery_color_detected)
        rotate_platform(delivery_color_detected)
        # open and close the trap door
        open_trap_door()
        # reset platform to the reference angle
        reset_to_reference_angle()
        not_delivered = False
    
    # we've delivered the cube, reset to not be looking for a delivery zone
    looking = False
    
    # if we're at the final delivery zone, we want to rotate the robot once the delivery has been carried out
    if green_counter == 6:
        # we're at the final delivery zone and not the loading, so rotate the robot
        rotate_robot(False)
        

def rotate_platform(delivery_color_detected):
    """
    function to rotate our platform to the correct colored cube.
    uses the degrees that we have found through our tests to rotate to the correct cube
    """
    if delivery_color_detected == "red":
        ROTATING_PLATFORM_MOTOR.set_position(RED_DEGREES)
    elif delivery_color_detected == "orange":
        ROTATING_PLATFORM_MOTOR.set_position(ORANGE_DEGREES)
    elif delivery_color_detected == "yellow":
        ROTATING_PLATFORM_MOTOR.set_position(YELLOW_DEGREES)
    elif delivery_color_detected == "purple":
        ROTATING_PLATFORM_MOTOR.set_position(PURPLE_DEGREES)
    elif delivery_color_detected == "green":
        ROTATING_PLATFORM_MOTOR.set_position(GREEN_DEGREES)
    elif delivery_color_detected == "blue":
        ROTATING_PLATFORM_MOTOR.set_position(BLUE_DEGREES)
    else:
        reset_to_reference_angle()
    
    # sleep for 6 seconds in order to wait for the platform to get into position
    sleep(3)

    
def reset_to_reference_angle():
    """
    function to reset the rotating dial back to its starting position
    """
    ROTATING_PLATFORM_MOTOR.set_position(-15)
    sleep(3)
    
    
def run():
    """The run method contains a while loop to constantly poll our input touch sensors
    and call helper methods to perform corresponding functionalities"""
    try:
        global left_delivery_zone
        left_delivery_zone = False
        # global variables are initialized here
        global green_counter
        green_counter = 0 # number of delivery zones detected
        global prev_color
        prev_color = "" # previous color that has been detected by our driving color sensor
        global delivering
        global looking
        global driving
        driving = True # not in the driving state until we press the touch sensor to initiate driving
        delivering = True # boolean to check if we are heading out on the path towards delivery zones.
        looking = False # boolean that turns true after we've detected the green zone to begin detecting delivery zones
        # motor initializations
        init_motor(TRAP_DOOR_MOTOR)
        init_motor(LEFT_WHEEL_MOTOR)
        init_motor(RIGHT_WHEEL_MOTOR)
        init_motor(ROTATING_PLATFORM_MOTOR)
        while True:
            # constantly poll the driving function within a while loop
            drive()
            sleep(SLEEP)
#             if TS.is_pressed():
#                 # toggle the driving state if the ts has been pressed
#                 driving = True
#                 print(driving)
#             drive()
#             sleep(SLEEP)
        

    except KeyboardInterrupt:
        print("ctrl+c")
    finally:
        BP.reset_all()
    BP.reset_all()
        

if __name__=='__main__':
    # call the main run function
    run()
