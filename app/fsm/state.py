from app.fsm.state_manager import current_state, override_state


def execute_current_state():
    execute_phase('actions')
    execute_transitions()


def execute_phase(phase_name):
    for function in get_functions_from_phase(phase_name):
        function()


def execute_transitions():
    for transition_function in get_functions_from_phase('transitions'):
        next_state = transition_function()

        if next_state:
            transition_to_next_state(next_state)
            break


def get_functions_from_phase(phase_name):
    try:
        return current_state()['phases'][phase_name]
    except (IndexError, KeyError):
        return ()


def get_arg(arg_name):
    return current_state()['args'][arg_name]


def set_arg(arg_name, new_value):
    current_state()['args'][arg_name] = new_value


def transition_to_next_state(next_state):
    if next_state:
        execute_phase('exit')
        override_state(next_state)
        execute_phase('enter')
