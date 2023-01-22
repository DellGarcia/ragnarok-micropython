from app.fsm.state_manager import current_state, append_state


def execute_state():
    execute_phase('actions')
    execute_transitions()


def execute_phase(phase_name):
    for function in get_current_phase(phase_name):
        function()

def execute_transitions():
    for transition in get_current_phase('transitions'):
        transition_to_next_state(transition())


def get_current_phase(phase_name, default_return=()):
    try:
        return current_state()['phases'][phase_name]
    except (KeyError, IndexError):
        return default_return


def get_arg(arg_name, default_value=None):
    try:
        return current_state()['args'][arg_name]
    except (KeyError, IndexError):
        return default_value


def set_arg(arg_name, new_value):
    try:
        current_state()['args'][arg_name] = new_value
        return True
    except (KeyError, IndexError):
        return False


def transition_to_next_state(next_state):
    if next_state:
        execute_phase('exit')
        append_state(next_state)
        execute_phase('enter')
