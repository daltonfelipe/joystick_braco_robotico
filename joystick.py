import inputs

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

def base(state):
    if state < deadzone:
        print('Esq: ',state)
    elif state > deadzone:
        print('Dir: ', state)
    else:
        print("Deadzone: ", state)


def front(state):
    if state < deadzone:
        print('Esq')
    if state > deadzone:
        print('Dir') 


COMMANDS = {
    'ABS_X': None,
    'ABS_Y': None,
    'ABS_RZ': None,
    'ABS_Z': base,
}


if len(pads) == 0:
    raise Exception('Nenhum joystick encontrado!')

while True:
    events = inputs.get_gamepad()
    for event in events:
        #print("Tipo: {}\n\tCodigo: {}\n\tEstado: {}\n".format(event.ev_type,event.code, event.state))
        cmd = COMMANDS.get(event.code)
        if callable(cmd):
            print(cmd.__name__,":")
            cmd(event.state)
        
                
