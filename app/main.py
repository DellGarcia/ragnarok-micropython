from app.fsm.machine import init, execute_machine
from app.car_states import states
from app.enviroments import envs


def run():
    init(states, envs["INITIAL_STATE"])

    while True:
        execute_machine()
