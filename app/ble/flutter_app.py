import bluetooth

from app.ble.bluetooth import BLEUART
from app.car.wheels import forward, backwards, left, right, stop, config_speed
from app.fsm.state import get_arg, set_arg


commands = {
    'FW': forward,
    'BW': backwards,
    'LT': left,
    'RT': right,
    'ST': stop,
}


def init():
    uart = BLEUART(bluetooth.BLE())
    uart.irq(handler=on_rx)

    config_speed(40, 40)

    set_arg('uart', uart)
    set_arg('current_command', 'ST')


def close():
    get_arg('uart').close()


def on_rx():
    command = get_arg('uart').read().decode().strip()

    if command in commands:
        set_arg('current_command', command)


def exec_command():
    commands[get_arg('current_command')]()
