#!/usr/bin/env python3

"""
This is the python script that operates our final design.

Authors: Evan Boyd, Sahar Fathi, Jean Kaznji, Shyam Desai
"""

"""
Brand new version!!!!!!!!!!!
"""

# imports 
from utils.brick import TouchSensor, wait_ready_sensors, Motor, BP, EV3ColorSensor
from time import sleep
from math import sqrt
from color_detection_two import color_detection_drive, color_detection_delivery # imports for all of our color functionalities
import sys

SLEEP = 0.05 # main run while loop sleep delay
DRIVING_COLOR_SENSOR = EV3ColorSensor(2) # Initializing the front color sensor
DELIVERY_COLOR_SENSOR = EV3ColorSensor(1) # Initializing the front color sensor
TS = TouchSensor(3) # Initializing the delivery zone color sensor to start the navgiation sequence
wait_ready_sensors(True)

#Initializing the two NXT motors responsible for the robot navigation
LEFT_WHEEL_MOTOR = Motor('A')
RIGHT_WHEEL_MOTOR = Motor('B')

ROTATING_PLATFORM_MOTOR = Motor('C')#Initializing the NXT motor responsible for rotating the platform
TRAP_DOOR_MOTOR = Motor('D')#Initializing the NXT motor responsible for opening and closing the trap doorr

#Constant variables
MOTOR_POWER_LIMIT = 80 # Power limit for all motors
MOTOR_SPEED_LIMIT = 300 # speed limit for all motors

WHEEL_SPEED = 175 # default wheel speed (dps)
WHEEL_DELTA_SPEED = 87.5 # how much we speed up by when making a turn (dps)

ROTATING_PLATFORM_SPEED = 300 # how fast the rotating platform spins (dps)
TRAP_DOOR_SPEED = 300 # how fast the trap door opens and closes (dps)


# CONSTANTS FOR ROTATING THE ROTATING PLATFORM BASED ON OUR TESTS ***
RED_DEGREES = 45+35
ORANGE_DEGREES = 2*45 + 35
YELLOW_DEGREES = 3*45 + 35
GREEN_DEGREES = 4*45 + 35 + 3
BLUE_DEGREES = 5*45 + 35
PURPLE_DEGREES = 6*45 + 35 + 3

def init_motor(motor):
    """
    function to initialize the motors used by our design. Sets the speed
    and power limits based on which motor has been passed to this function,
    and according to the CONSTANTS that we've set.
    
    Input - motor(Motor): the motor to be initialized
    Output - NONE
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
    
    Input - None
    Output - None
    """
    TRAP_DOOR_MOTOR.set_position(-200)
    sleep(1)
    TRAP_DOOR_MOTOR.set_position(10)    
    sleep(1)

    
def drive():
    """
    Controller for driving our robot. This is called continuously from the main while
    loop in the run function. Keeps track of the system position and adjusts it accordingly
    
    Input - None
    Output - None
    """
    global green_counter # counts the # of green zones detected
    global prev_color # previous color detected by the driving color sensor
    global delivering # heading out to 6 delivery zones vs back to loading bay; determines which way we need to turn
    global looking #looking for a delivery zone (set to true once green has been detected)
    global driving
    global left_delivery_zone
    global delivery_order
    global driving_history
    

    # perform driving if in the driving state
    if driving:
        # constantly poll the color sensors
        driving_rgb = DRIVING_COLOR_SENSOR.get_rgb()
        delivery_rgb = DELIVERY_COLOR_SENSOR.get_rgb()
        driving_color_detected = ""
        #the order of the color is placed into its index

        color_deliv_box=""
        if None not in driving_rgb:
            driving_color_detected = color_detection_drive(driving_rgb)
        delivery_color_detected = ""
        if None not in delivery_rgb:
            delivery_color_detected = color_detection_delivery(delivery_rgb)
        driving_history.append(driving_color_detected)
        print("Driving color: "+driving_color_detected)
        
        
        if looking:
            WHEEL_SPEED = 100
            WHEEL_DELTA_SPEED = 50
        
        
        #print("driving color: " + driving_color_detected)
        
        #isLookingForWhite=False
        
        if looking and delivery_color_detected != "white":
        # carry out the delivery according to the color of the delivery zone detected
            #print(delivery_rgb)
            color_deliv_counter = 0
            list_deliv_colors = []
            
            while (color_deliv_counter<12):
                rgb = DELIVERY_COLOR_SENSOR.get_rgb()
                list_deliv_colors.append(color_detection_delivery(rgb))
                print(color_detection_delivery(rgb))
                #print(color_detection_delivery(rgb))
                color_deliv_counter+=1
                
            color_deliv_box = find_avg_color(list_deliv_colors)
            print("delivery colors: "+str(list_deliv_colors))
#             perform_delivery(color_deliv_box)
            print(delivery_order)
            
            #isWhite = True if color_detection_delivery(DELIVERY_COLOR_SENSOR.get_rgb())=="white" else False
            while True:
                isWhite=False
                if color_detection_delivery(DELIVERY_COLOR_SENSOR.get_rgb())!= None:
                    isWhite = True if color_detection_delivery(DELIVERY_COLOR_SENSOR.get_rgb())=="white" else False
                continue_straight()
                if isWhite:
                    print("performing delivery")
                    perform_delivery(color_deliv_box)
                    break
                sleep(SLEEP)
                    
                """
            if color_deliv_box not in delivery_order:
                
                print("here before if")
                continue_straight()
                sleep(1)
                perform_delivery(color_deliv_box)
                print("here after if")
                delivery_order.append(color_deliv_box)
                print(delivery_order)
                """
            
        if prev_color == "green" and driving_color_detected!="green":
                sleep(0.2)
                if not delivering:
                    sleep(0.420)
                adjust()
                looking=True
                
        if driving_color_detected == "blue":
            # blue is on the left when delivering, so turn right
            if delivering:    
                turn_right()
            else:
                turn_left()
            if prev_color == "green":
                sleep(0.2)
            # set the previous color (allows us to detected green strip delivery zones)
            prev_color = "blue"
        elif driving_color_detected == "red":
            # red and delivering, so turn left
            if delivering:
                turn_left()
            else:
               turn_right()
               
            if prev_color == "green":
                sleep(0.2)
            prev_color = "red"
        elif driving_color_detected == "white":
            # white, so we continue straight
            continue_straight()
            if prev_color == "green":
                sleep(0.2)
            prev_color = "white"
        elif driving_color_detected == "green":
            # time to begin looking for a delivery zone
            prev_color = "green"
            
        elif driving_color_detected == "yellow":
            prev_color = "yellow"
        
        last_five_values=[driving_history[-1],driving_history[-2],driving_history[-3],driving_history[-4],driving_history[-5]]
        if len(set(last_five_values))==1 and last_five_values[0]=="yellow" and not delivering:
            # we've seen yellow, so now it is time to rotate the opposite direction and stop driving
            rotate_robot(True)
            delivering = True
            driving = False
            green_counter=0
            while True:
                go_back()
                sleep(2)
                break
            stop()
            
            
        
def find_avg_color(lst):
    """
    Function to find the most repeated element in a given list
    
    Input - lst(list): a list of Strings that contain the colors of the delivery zones
    Output - color_list[maximum] (str): a string value of one of the delivery zone colors
    """
    color_counter = [lst.count("red"), lst.count("orange"), lst.count("yellow"),
                     lst.count("green"), lst.count("blue"), lst.count("purple")]
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    maximum = color_counter.index(max(color_counter))
    return color_list[maximum]


def rotate_robot(at_loading_bay):
    print("start rotating")
    """
    function to rotate the robot while staying within the track. Takes an input boolean
    to know if we're at the loading bay and then perform the corresponding rotation. 
    
    Input - at_loading_bay (bool): boolean to indicates where the robot is (last delivery zone or loading bay)
    Output - None
    """
    if not at_loading_bay:
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "red":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
                break
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "blue":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
                break
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "white":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
                break
        return
    else:
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "red":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "blue":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
        while True:
            # set the motors to go in opposite directions
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(SLEEP)
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            new_driving_color_detected = ""
            if None not in rgb:
                new_driving_color_detected = color_detection_drive(rgb)
            
            if new_driving_color_detected == "white":
                stop()
                sleep(1)
                break
            elif new_driving_color_detected=="green":
                go_back()
                sleep(0.2)
        return


def stop():
    """
    function to stop the driving of the robot by setting the speed of the two NXT motors to zero
    
    Input - None
    Output - None
    """
    LEFT_WHEEL_MOTOR.set_dps(0)
    RIGHT_WHEEL_MOTOR.set_dps(0)
    sleep(0.2)

def continue_straight():
    """
    function to make the robot go straight depending on wheel speed
    
    Input - None
    Output - None
    """
    LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
    RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)

def go_back():
    """
    function to make the robot go backwared depending on wheel speed
    
    Input - None
    Output - None
    """
    LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
    RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)

def turn_left():
    """
    function that turns the robot left.
    We continuously increase the amount that we're turning by
    
    Input - None
    Output - None
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
    
    Input - None
    Output - None
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
    global delivering
    
    if delivering:
        ROTATING_PLATFORM_MOTOR.set_dps(90)
        not_delivered = True
        # stop the driving
        stop()
        while not_delivered:
            # rotate to the corresponding colored cube
            print("delivery color:"+delivery_color_detected)
            rotate_platform(delivery_color_detected)
            green_counter = green_counter + 1
            print("green_counter:"+str(green_counter))
            # open and close the trap door
            open_trap_door()
            # we've delivered the cube, reset to not be looking for a delivery zone
            looking = False
            # reset platform to the reference angle
            reset_to_reference_angle()
            not_delivered = False
        
        
        # if we're at the final delivery zone, we want to rotate the robot once the delivery has been carried out
        if green_counter == 6:
            while True:
                #Move forward a bit at the last zone
                continue_straight()
                sleep(2)
                break
            # we're at the final delivery zone and not the loading, so rotate the robot
            rotate_robot(False)
            delivering = False
            green_counter=0
            
        
        adjust()
        WHEEL_SPEED = 175
        WHEEL_DELTA_SPEED = 87.5
        
def adjust():
    """
    Turn the robot to be in the middle of the path after each delivery.
    """
    print("adjusting")
    if delivering:
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "blue":
                break
            if color_detected == "green":
                looking=True
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(0.1)
        
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "red":
                break
            if color_detected == "green":
                looking=True
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(0.1)
            
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "blue":
                break
            if color_detected == "green":
                looking=True
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(0.1)
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "white":
                sleep(0.2)
                break
            if color_detected == "green":
                looking=True
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(0.1)
    else:
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "blue":
                break
            if color_detected == "green":
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(0.1)
        
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "red":
                break
            if color_detected == "green":
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(0.1)
            
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "blue":
                break
            if color_detected == "green":
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            sleep(0.1)
        while True:
            rgb = DRIVING_COLOR_SENSOR.get_rgb()
            color_detected = ""
            if None not in rgb:
                color_detected = color_detection_drive(rgb)
            if color_detected == "white":
                sleep(0.2)
                break
            if color_detected == "green":
                LEFT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
                sleep(0.5)
            LEFT_WHEEL_MOTOR.set_dps(-WHEEL_SPEED)
            RIGHT_WHEEL_MOTOR.set_dps(WHEEL_SPEED)
            sleep(0.1)
        
def rotate_platform(delivery_color_detected):
    """
    function to rotate our platform to the correct colored cube.
    uses the degrees that we have found through our tests to rotate to the correct cube
    
    Input - delivery_color_detected(str): a String value representing the color detected by the delivery color sensor
    Ouptut - None
    """
    #ROTATING_PLATFORM_MOTOR.set_dps(90)
    if delivery_color_detected == "red":
        ROTATING_PLATFORM_MOTOR.set_position(RED_DEGREES)
        sleep(0.5)
    elif delivery_color_detected == "orange":
        ROTATING_PLATFORM_MOTOR.set_position(ORANGE_DEGREES)
        sleep(0.5)
    elif delivery_color_detected == "yellow":
        ROTATING_PLATFORM_MOTOR.set_position(YELLOW_DEGREES)
        sleep(0.5)
    elif delivery_color_detected == "purple":
        ROTATING_PLATFORM_MOTOR.set_position(PURPLE_DEGREES) 
        sleep(0.5)
    elif delivery_color_detected == "green":
        ROTATING_PLATFORM_MOTOR.set_position(GREEN_DEGREES)
        sleep(0.5)
    elif delivery_color_detected == "blue":
        ROTATING_PLATFORM_MOTOR.set_position(BLUE_DEGREES)
        sleep(0.5)
    else:
        reset_to_reference_angle()
    
    # sleep for 6 seconds in order to wait for the platform to get into position
    sleep(3)

    
def reset_to_reference_angle():
    """
    function to reset the rotating dial back to its starting position
    
    Input - None
    Output - None
    """
    ROTATING_PLATFORM_MOTOR.set_position(30)
    sleep(2)
    ROTATING_PLATFORM_MOTOR.set_position(-8)
    sleep(2)
    
    
def run():
    """The run method contains a while loop to constantly poll our input touch sensors
    and call helper methods to perform corresponding functionalities
    
    Input - None
    Output - None
    """
    
    try:
        global left_delivery_zone
        left_delivery_zone = False
        # global variables are initialized here
        global green_counter
        green_counter = 0 # number of delivery zones detected
        white_counter=0#keeps track of the amount of time we get the white color to adjust if necessary
        global prev_color
        prev_color = "" # previous color that has been detected by our driving color sensor
        global delivering
        global looking
        global driving
        global delivery_order
        delivery_order = []
        driving = False # not in the driving state until we press the touch sensor to initiate driving
        delivering = True # boolean to check if we are heading out on the path towards delivery zones.
        looking = False # boolean that turns true after we've detected the green zone to begin detecting delivery zones
        global driving_history
        driving_history=["white","white","white","white","white"]
        # motor initializations
        init_motor(TRAP_DOOR_MOTOR)
        init_motor(LEFT_WHEEL_MOTOR)
        init_motor(RIGHT_WHEEL_MOTOR)
        init_motor(ROTATING_PLATFORM_MOTOR)
        while True:
            if(TS.is_pressed()):
                #perform_delivery("purple")
                driving= True
                continue_straight()
                sleep(0.2)
                #while True:
                    #rgb = DELIVERY_COLOR_SENSOR.get_rgb()
                    #color_detected = ""
                    #if None not in rgb:
                        #color_detected = color_detection_delivery(rgb)
                    #print(color_detected)
        
            # constantly poll the driving function within a while loop
            drive()
            sleep(SLEEP)
            if (prev_color=="white"):
                white_counter+=1
            else:
                white_counter=0
            #print("white counter: "+str(white_counter))
            if(white_counter>=40 and driving):
                #print("white adjust")
                adjust()
                white_counter=0
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


