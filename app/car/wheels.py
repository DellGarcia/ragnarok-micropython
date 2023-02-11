from machine import Pin, PWM
from app.enviroments import envs
from app.car.motor import DCMotor


wheels = {
    'left': None,
    'right': None
}

min_duty = envs['min_duty']
max_duty = envs['max_duty']
frequency = envs['frequency']
speed = envs['speed']
back_speed = speed * 3

for key in wheels.keys():
    pin1 = Pin(envs[key + '_pin1'], Pin.OUT)
    pin2 = Pin(envs[key + '_pin2'], Pin.OUT)
    enable_pin = PWM(Pin(envs[key + '_enable_pin']), frequency)
    motor = DCMotor(pin1, pin2, enable_pin, min_duty, max_duty)
    wheels[key] = motor

left_wheel = wheels['left']
right_wheel = wheels['right']


def set_wheels_speed(left_speed, right_speed):
    forward(left_speed=left_speed, right_speed=right_speed)

def left():
    left_wheel.forward(speed)
    right_wheel.backwards(speed)


def right():
    right_wheel.forward(speed)
    left_wheel.backwards(speed)


def forward(left_speed=speed, right_speed=speed):
    left_wheel.forward(left_speed)
    right_wheel.forward(right_speed)


def backward():
    left_wheel.backwards(back_speed)
    right_wheel.backwards(back_speed)


def stop():
    left_wheel.stop()
    right_wheel.stop()
