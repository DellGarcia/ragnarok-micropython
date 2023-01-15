from machine import Pin, PWM
from hcsr04 import HCSR04
from DCMotor import DCMotor
from time import sleep

left_infra = Pin(34, Pin.IN)
center_infra = Pin(35, Pin.IN)
right_infra = Pin(19, Pin.IN)

sensor = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=10000)
 
frequency = 1000       
pin1 = Pin(5, Pin.OUT)    
pin2 = Pin(18, Pin.OUT)  
enable1 = PWM(Pin(32), frequency)

pin3 = Pin(16, Pin.OUT)    
pin4 = Pin(17, Pin.OUT)  
enable2 = PWM(Pin(33), frequency)

left_motor = DCMotor(pin1, pin2, enable1, min_duty=400, max_duty=1023)
right_motor = DCMotor(pin3, pin4, enable2, min_duty=400, max_duty=1023)

speed = 40
back_speed = speed * 3

distance = 0

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
    
def adjust_to_left():
    while center_infra.value() == 0:
        left()
        
def adjust_to_right():      
    while center_infra.value() == 0:
        right()

while True:
    # print(left_infra.value(), " | ", center_infra.value(), " | ", right_infra.value())
    # sleep(0.5)
    
    distance = sensor.distance_cm()
    
    if distance < 10:
        stop()
    
    leftOn = left_infra.value()
    rightOn = right_infra.value()
    centerOn = center_infra.value()
    
    '''
        Black line equals to 1
    '''
    if leftOn == 1:
        adjust_to_left()
    elif rightOn == 1:
        adjust_to_right()
    else:
        forward()
    