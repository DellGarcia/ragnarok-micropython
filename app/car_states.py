from app.fsm.state import get_arg, set_arg
from car import read_infra, forward, stop, left, right

def set_infra_arg():
    left, center, right = read_infra()
    set_arg('left_on', left)
    set_arg('center_on', center)
    set_arg('right_on', right)


states = {
    'bluetooth_demo': {
        'phases': {
            'actions': lambda: print("Bluetooth")
        }
    },
    'forward': {
        'phases': {
            'actions': [
                set_infra_arg,
                forward
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
