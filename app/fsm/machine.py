from app.fsm.state_manager import set_states
from app.fsm.state import execute_state, transition_to_next_state


def init(states, first_state):
    set_states(states)
    transition_to_next_state(first_state)


def execute_machine():
    execute_state()
