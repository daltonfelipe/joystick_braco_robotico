import pygame, os
from pygame.locals import *
from gpio import ServoPWM

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.joystick.init()

done = False

joystick = pygame.joystick.Joystick(0)
joystick.init()


servo_base = ServoPWM(18)
servo_height = ServoPWM(12)
servo_garra = ServoPWM(13)
servo_frente = ServoPWM(19)

deadzone = 0

def map_val(x,  in_min,  in_max,  out_min,  out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def base(state):
    s = map_val(state, -1, 1, 1, 150)
    print("base: ",s)
    servo_base.set_angle(s)


def frente(state):
    s = map_val(state, -1, 1, 10, 55)
    print("frente: ", s)
    servo_frente.set_angle(s)
    

def garra(state):
    if state == 0:
        servo_garra.set_angle(90)
    elif state == 1:
        servo_garra.set_angle(20)


def height(state):
    s = map_val(state, -1, 1, 5, 80)
    servo_height.set_angle(s)
    


while not done:

    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:
            x1, y1 = joystick.get_axis(0), joystick.get_axis(1)
            x2, y2 = joystick.get_axis(2), joystick.get_axis(3)
            base(x2 or x1)
            height(-y1)
            frente(-y2)
        if event.type == JOYBUTTONDOWN:
            l1 = joystick.get_button(4)
            l2 = joystick.get_button(6)
            if l1 == 1:
                garra(0)
            elif l2 == 0:
                garra(1)

