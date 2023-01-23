
from app.car.wheels import forward, stop, left, right
from app.car.infrareds import set_infras_arg, has_activated
from app.car.ultrasonic import set_ultra_arg
from app.bluetooth import demo
from app.fsm.state import get_arg


states = {
    'bluetooth_demo': {
        'phases': {
            'actions': [
                demo
            ],
        }
    },
    'forward': {
        'phases': {
            'actions': [
                set_infras_arg,
                forward
            ],
            'transitions': [
                lambda: 'left' if has_activated('left') else None,
                lambda: 'right' if has_activated('right') else None
            ]
        }
    },
    'stop': {
        'phases': {
            'enter': [
                stop
            ]
        }
    },
    'left': {
        'phases': {
            'actions': [
                set_infras_arg,
                left
            ],
            'transitions': [
                lambda: 'forward' if has_activated('center') else None
            ]
        }
    },
    'right': {
        'phases': {
            'actions': [
                set_infras_arg,
                right
            ],
            'transitions': [
                lambda: 'forward' if has_activated('center') else None
            ]
        }
    }
}
