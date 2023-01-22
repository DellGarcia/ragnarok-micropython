from app.fsm.state import get_arg, set_arg
from app.car import read_infra, forward, stop, left, right, ultra_distance_cm
from app.bluetooth import demo

def set_infra_arg():
    left, center, right = read_infra()
    set_arg('left_on', left)
    set_arg('center_on', center)
    set_arg('right_on', right)


def read_ultra():
    set_arg('ultra_cm', ultra_distance_cm())


states = {
    'bluetooth_demo': {
        'phases': {
            'actions': demo,
            'enter': [],
            'exit': [],
            'transitions': []
        }
    },
    'forward': {
        'phases': {
            'actions': [
                set_infra_arg,
                forward,
                read_ultra
            ],
            'transitions': [
                lambda: 'left' if get_arg('left_on')  == 1 else None,
                lambda: 'right' if get_arg('right_on') == 1 else None
            ]
        }
    },
    'stop': {
        'phases': {
            'enter': stop
        }
    },
    'left': {
        'phases': {
            'actions': [
                set_infra_arg,
                left
            ],
            'transitions': [
                lambda: 'forward' if get_arg('center_on') == 1 else None
            ]
        }
    },
    'right': {
        'phases': {
            'actions': [
                set_infra_arg,
                right
            ],
            'transitions': [
                lambda: 'forward' if get_arg('center_on') == 1 else None
            ]
        }
    }
}
