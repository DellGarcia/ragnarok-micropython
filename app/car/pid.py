from time import ticks_ms, ticks_diff

from app.fsm.state import get_arg, set_arg
from app.car.wheels import set_wheels_speed
from app.enviroments import envs


KP = envs['KP']
KI = envs['KI']
KD = envs['KD']
LIMIT = envs['LIMIT']


def init_pid():
    set_arg('previous_time', ticks_ms())
    set_arg('previous_error', 0)
    set_arg('integral', 0)


def get_ir_values():
    return [get_arg('infras')[key] for key in ('left', 'center', 'right')]


def calc_error():
    left, center, right = get_ir_values()

    # The central sensor can be ignored, since the error = 0, it means that it is already on the line
    error = (left * -1) + (center * 0) + (right * 1)

    # error = 0

    # if center:
    #     error = 0
    # elif left and not right:
    #     error = -1
    # elif right and not left:
    #     error = 1
    # else:
    #     error = 2

    return error


def calc_correction():
    current_time = ticks_ms()
    previous_time = get_arg('previous_time')
    previous_error = get_arg('previous_error')
    integral = get_arg('integral')

    # Delta time
    deltatime = ticks_diff(current_time, previous_time)

    # Calculate the error between the desired position and the current position
    error = calc_error()

    # Calculate the integral of the error
    integral += error * deltatime

    # Calculate the derivative of the error
    derivative = (error - previous_error) / deltatime

    # Calculate the correction term
    correction = (KP * error) + (KI * integral) + (KD * derivative)

    set_arg('integral', integral)
    set_arg('previous_error', error)
    set_arg('previous_time', current_time)

    return correction


def adjust_motor_speed():
    correction = calc_correction()
    set_wheels_speed(LIMIT - correction, LIMIT + correction)
