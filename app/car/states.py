
from app.car.wheels import forward, stop, left, right
from app.car.infrareds import set_infras_arg, has_activated
from app.car.ultrasonic import set_ultra_arg
from app.ble.bluetooth import demo
from app.fsm.state import get_arg
from app.ble.flutter_app import exec_command, init, close
from app.car.pid import adjust_motor_speed, init_pid


states = {
    'ble_flutter': {
        'phases': {
            'enter': init,
            'actions': exec_command,
            'exit': close
        }
    },
    'pid': {
        'phases': {
            'enter': [
                init_pid
            ],
            'actions': [
                set_infras_arg,
                adjust_motor_speed
            ]
        }
    },
    'bang-bang': {
        'phases': {
            'transitions': lambda: 'forward'
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
