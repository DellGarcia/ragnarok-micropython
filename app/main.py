from fsm.machine import init, execute_machine
from app.car_states import states


def run():
    init(states, 'forward')

    while True:
        execute_machine()
