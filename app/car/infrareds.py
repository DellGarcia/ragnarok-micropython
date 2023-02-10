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
    return [infras[key].value() for key in ('left', 'center', 'right')]

def display_infra():
    print(infras['left'].value(), ' | ', infras['center'].value() , ' | ', infras['right'].value())

def has_activated(name):
    return get_arg('infras')[name] == 1

def set_infras_arg():
    left, center, right = read_infras()

    set_arg('infras', {
        'left': left,
        'center': center,
        'right': right
    })
