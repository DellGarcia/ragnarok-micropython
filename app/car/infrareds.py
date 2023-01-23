from machine import Pin
from app.enviroments import envs
from app.fsm.state import get_arg, set_arg


infras = {
    'left': None,
    'center': None,
    'right': None
}

for key in infras.keys():
    infras[key] = Pin(envs[key + '_infra'], Pin.IN)

def read_infras():
    return [infra.value() for infra in infras.values()]

def display_infra():
    print(' | '.join(infras.values()))

def has_activated(name):
    return get_arg(name + '_on') == 1

def set_infras_arg():
    for name, value in zip(('left_on', 'center_on', 'right_on'), read_infras()):
        set_arg(name, value)
