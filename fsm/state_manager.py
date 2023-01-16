from collections import deque


states = dict()
previous_states = deque()


def set_states(beginning_stages):
    states.update(beginning_stages)
    setup_states()


def setup_states():
    for state_key, state_value in states.items():
        for phase_key, phase_value in state_value['phases'].items():
            states[state_key]['phases'][phase_key] = [phase_value] if not isinstance(phase_value, list) else phase_value


def current_state():
    return states[previous_states[-1]]


def append_state(state: str):
    previous_states.append(state)

    if len(previous_states) > 5:
        previous_states.popleft()
