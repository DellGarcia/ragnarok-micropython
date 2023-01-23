from collections import deque

states = dict()
previous_states = deque((), 5)


def set_states(beginning_stages):
    global states
    states = beginning_stages


def setup_states():
    for state_key, state_value in states.items():
        states[state_key]['args'] = dict()

        for phase_key, phase_value in state_value['phases'].items():
            states[state_key]['phases'][phase_key] = [phase_value] if not isinstance(phase_value, list) else phase_value


def current_state():
    return states[previous_states[-1]]


def append_state(state: str):
    previous_states.append(state)
