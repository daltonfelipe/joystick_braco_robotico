import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.joystick.init()

done = False

joystick = pygame.joystick.Joystick(0)
joystick.init()

deadzone = 0

def base(state):
    if state < deadzone:
        print('Esq')
    elif state > deadzone:
        print('Dir')
    else:
        print("Deadzone")


def front(state):
    if state < deadzone:
        print('Esq')
    elif state > deadzone:
        print('Dir')
    else:
        print("Deadzone")


COMMANDS = {
    'ABS_X': None,
    'ABS_Y': None,
    'ABS_RZ': None,
    'ABS_Z': base,
}

while not done:

    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:
            x1, y1 = joystick.get_axis(0), joystick.get_axis(1)
            x2, y2 = joystick.get_axis(2), joystick.get_axis(3)
            base(x2)
            # print('L1: ',x1,' | ', y1)
            # print('L2: ',x2,' | ', y2)