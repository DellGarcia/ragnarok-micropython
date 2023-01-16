from time import sleep
from machine import Pin, PWM
from app.hcsr04 import HCSR04
from app.motor import DCMotor
from app.enviroments import envs

left_infra = Pin(envs["left_infra"], Pin.IN)
center_infra = Pin(envs["center_infra"], Pin.IN)
right_infra = Pin(envs["right_infra"], Pin.IN)

ultra_sensor = HCSR04(trigger_pin=envs["ultra_trigger"], echo_pin=envs["ultra_echo"], echo_timeout_us=10000)
 
frequency = envs["frequency"]

left_pin1 = Pin(envs["left_pin1"], Pin.OUT)    
left_pin2 = Pin(envs["left_pin2"], Pin.OUT)  
left_enable = PWM(Pin(envs["left_enable"]), frequency)

right_pin1 = Pin(envs["right_pin1"], Pin.OUT)    
right_pin2 = Pin(envs["right_pin2"], Pin.OUT)  
right_enable = PWM(Pin(envs["right_enable"]), frequency)

left_motor = DCMotor(left_pin1, left_pin2, left_enable, min_duty=envs["min_duty"], max_duty=envs["max_duty"])
right_motor = DCMotor(right_pin1, right_pin2, right_enable, min_duty=envs["min_duty"], max_duty=envs["max_duty"])

speed = envs["speed"]
back_speed = speed * 3

DEBUG_MODE = envs["DEBUG_MODE"]

def left():
    left_motor.forward(speed)
    right_motor.backwards(speed)
    
def right():
    right_motor.forward(speed)
    left_motor.backwards(speed)

def forward():
    left_motor.forward(speed)
    right_motor.forward(speed)
    
def backward():
    left_motor.backwards(back_speed)
    right_motor.backwards(back_speed)
    
def stop():
    left_motor.stop()
    right_motor.stop()
    
def will_collide():
    if not envs["COLLISION_CHECK"]:
        return False
    
    return ultra_sensor.distance_cm() < 10
    
def adjust_to_left():
    while center_infra.value() == 0:
        if will_collide():
            break;
        left()
        
def adjust_to_right():      
    while center_infra.value() == 0:
        if will_collide():
            break;
        right()

def display_infra():
    print(left_infra.value(), " | ", center_infra.value(), " | ", right_infra.value())
    sleep(0.5)
