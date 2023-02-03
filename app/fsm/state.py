from app.fsm.state_manager import current_state, append_state


def execute_state():
    execute_phase('actions')
    execute_transitions()


def execute_phase(phase_name):
    for phase in get_phase(phase_name):
        phase()

def execute_transitions():
    for transition in get_phase('transitions'):
        next_state = transition()
        
        if next_state:
            transition_to_next_state(next_state)
            break


def get_phase(phase_name):
    try:
        return current_state()['phases'][phase_name]
    except (IndexError, KeyError):
        return ()
        

def get_arg(arg_name, default_value=None):
    return current_state()['args'][arg_name]
    

def set_arg(arg_name, new_value):
    current_state()['args'][arg_name] = new_value


def transition_to_next_state(next_state):
    if next_state:
        execute_phase('exit')
        append_state(next_state)
        execute_phase('enter')
