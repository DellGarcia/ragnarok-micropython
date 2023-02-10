states = dict()
current_state_name = None


def set_states(beginning_stages):
    global states, states_names
    states = beginning_stages


def setup_states():
    for state_key, state_value in states.items():
        states[state_key]['args'] = dict()

        for phase_key, phase_value in state_value['phases'].items():
            states[state_key]['phases'][phase_key] = [phase_value] if not isinstance(phase_value, list) else phase_value


def current_state():
    try:
        return states[current_state_name]
    except (IndexError, KeyError) as err:
        print('Invalid state name!')
        raise err


def override_state(next_state_name: str):
    global current_state_name
    current_state_name = next_state_name
