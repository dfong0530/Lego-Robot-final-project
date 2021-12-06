#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
#Initializing motors
#CHECK THAT YOUR CHANNELS "outA, outB, outC, outD" ARE CORRECT BEFORE RUNNING
motorLeft = LargeMotor('outB'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outC'); motorRight.stop_action = 'hold'
#Uncomment the line below if you want to use the third, smaller, motor for anything
#MM = MediumMotor('outA'); MM.stop_action = 'hold' 

#Initializing lightsensors
# 
leftSensor = ColorSensor(INPUT_2)
rightSensor = ColorSensor(INPUT_3)

#If you want your robot to make sounds!
sound = Sound()

#Setting a black value to compare to. Reflected light intensity returns a number between 0 and 100 -- higher values are brighter, lower values are darker.
leftBlack = leftSensor.reflected_light_intensity
rightBlack = rightSensor.reflected_light_intensity



def turnRight():
    motorLeft.run_to_rel_pos(position_sp= 275, speed_sp = 250)
    motorRight.run_to_rel_pos(position_sp= -275, speed_sp = 250)
    sleep(1)

def turnLeft():
    motorLeft.run_to_rel_pos(position_sp= -270, speed_sp = 250)
    motorRight.run_to_rel_pos(position_sp= 270, speed_sp = 250)

    sleep(1)

def forward():
    motorLeft.on(30)
    motorRight.on(30)
    while(leftSensor.reflected_light_intensity < 20 and rightSensor.reflected_light_intensity < 20):
        continue
    motorRight.stop()
    motorLeft.stop()
    if(leftSensor.reflected_light_intensity>20):
        motorRight.on(10)
        while(rightSensor.reflected_light_intensity<20):
            continue
    motorRight.stop()
    if(rightSensor.reflected_light_intensity>20):
        motorLeft.on(10)
        while(leftSensor.reflected_light_intensity<20):
            continue
    motorLeft.stop()

    motorLeft.on(10)
    motorRight.on(10)
    while(leftSensor.reflected_light_intensity > 20 and rightSensor.reflected_light_intensity > 20):
        continue
    motorRight.stop()
    motorLeft.stop()
    if(leftSensor.reflected_light_intensity<20):
        motorRight.on(10)
        while(rightSensor.reflected_light_intensity>20):
            continue
    motorRight.stop()
    if(rightSensor.reflected_light_intensity<20):
        motorLeft.on(10)
        while(leftSensor.reflected_light_intensity>20):
            continue
    motorLeft.stop()

    motorLeft.on(30)
    motorRight.on(30)
    sleep(1.3)
    motorLeft.stop()
    motorRight.stop()

def left():

    turnLeft()
    forward()
    turnRight()

def right():
    turnRight()
    forward()
    turnLeft()
    
def back():
    motorLeft.on(-30)
    motorRight.on(-30)
    sleep(2.75)
    motorLeft.stop()
    motorRight.stop()

def robot_say(words):
    sound.speak(words)

def move_robot(n):

    if n == 1:

        forward()

    elif n == 2:

        back()

    elif n == 3:

        turnLeft()

    elif n == 4:

        turnRight()

if __name__ == "__main__":

    '''
    ###
    turnLeft()
    sleep(2)
    turnRight()
    sleep(8)

    ###
    turnRight()
    sleep(3)
    turnLeft()
    '''
    for i in range(20):

        x = int(input("Enter data: "))

        move_robot(x)
