import inputs
from gpio import ServoPWM

servo_base = ServoPWM(18)
servo_height = ServoPWM(12)
servo_garra = ServoPWM(13)
servo_frente = ServoPWM(19)

pads = inputs.devices.gamepads

"""

DEADZONE = 128

ROLETA 1    
    CODIGO -> ABS_Y  (cima e baixo)
        CIMA  -> DEADZONE ATÉ 0  
        BAIXO -> DEADZONE ATÉ 255
    CODIGO -> ABS_X  (dir e esq)
        ESQ   -> DEADZONE ATÉ 0 
        DIR   -> DEADZONE ATÉ 255

ROLETA 2
    CODIGO -> ABS_Z  (cima e baixo)
        CIMA  -> DEADZONE ATÉ 0  
        BAIXO -> DEADZONE ATÉ 255
    CODIGO -> ABS_RZ (dir e esq)
        ESQ   -> DEADZONE ATÉ 0 
        DIR   -> DEADZONE ATÉ 255

    CODIGO -> ABS_RZ (esquerda e direita)
"""
deadzone = 128

def map_val( x,  in_min,  in_max,  out_min,  out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def base(state):
    s = map_val(state, 0, 255, 0, 180)
    print("base: ",s)
    servo_base.set_angle(s)


def frente(state):
    s = map_val(state, 0, 255, 5, 55)
    print("frente: ", s)
    servo_frente.set_angle(s)
    

def garra(state):
    if state == 1:
        servo_garra.set_angle(90)
    else:
        servo_garra.set_angle(20)


def height(state):
    s = map_val(state, 0, 255, 0, 80)
    servo_height.set_angle(s)
    


COMMANDS = {
    'ABS_X': base,
    'ABS_Y': frente,
    'ABS_RZ': height,
    'ABS_Z': base,
    'BTN_TOP2': garra
}


if len(pads) == 0:
    raise Exception('Nenhum joystick encontrado! Reconecte e tente novamente!')

while True:
    events = inputs.get_gamepad()
    for event in events:
        #print("Tipo: {}\n\tCodigo: {}\n\tEstado: {}\n".format(event.ev_type,event.code, event.state))
        cmd = COMMANDS.get(event.code)
        if callable(cmd):
            s = event.state
            if s == deadzone:
                s = 0
            elif s < deadzone:
                s /= -deadzone
            else:
                s /= 255
            print(s)
            #cmd(event.state)
        
                
