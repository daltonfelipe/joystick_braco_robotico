import pygame, os
from pygame.locals import *

# custom class for GPIO handler
from gpio import ServoPWM

# desable video driver for pygame class
os.environ["SDL_VIDEODRIVER"] = "dummy"

# init the loop of pygame
pygame.init()

# init the loop for joystick events
pygame.joystick.init()

# control loop of main code
done = False

# connect with gamepad
joystick = pygame.joystick.Joystick(0)
joystick.init()

# servo controllers
servo_base = ServoPWM(18)
servo_height = ServoPWM(12)
servo_garra = ServoPWM(13)
servo_front = ServoPWM(19)

# value of neutral position in gamepad axis
deadzone = 0


# make a interpolation of scales
def map_val(x,  in_min,  in_max,  out_min,  out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# change the angle of servos
def base(state):
    s = map_val(state, -1, 1, 1, 150)
    print("base: ",s)
    servo_base.set_angle(s)


def front(state):
    s = map_val(state, -1, 1, 10, 55)
    print("front: ", s)
    servo_front.set_angle(s)
    

def garra(state):
    if state == 0:
        servo_garra.set_angle(90)
    elif state == 1:
        servo_garra.set_angle(20)


def height(state):
    s = map_val(state, -1, 1, 5, 80)
    servo_height.set_angle(s)


# main loop of program
while not done:
    # get joystick events
    for event in pygame.event.get():
        # identify the type of event
        if event.type == JOYAXISMOTION:
            # get values of both axis
            # up or down
            x1, y1 = joystick.get_axis(0), joystick.get_axis(1)
            # left or right
            x2, y2 = joystick.get_axis(2), joystick.get_axis(3)
            # change the angle of base servo
            base(x2 or x1)
            # change angle of height servo
            height(-y1)
            # change angle of front servo
            front(-y2)
        if event.type == JOYBUTTONDOWN:
            # get value of l1 and l2 buttons
            l1 = joystick.get_button(4)
            l2 = joystick.get_button(6)
            # change actual state of garra
            if l1 == 1:
                garra(0)
            elif l2 == 0:
                garra(1)

