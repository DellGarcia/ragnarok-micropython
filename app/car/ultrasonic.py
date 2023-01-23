from app.car.hcsr04 import HCSR04
from app.enviroments import envs
from app.fsm.state import set_arg


ultra_sensor = HCSR04(trigger_pin=envs['ultra_trigger'], echo_pin=envs['ultra_echo'], echo_timeout_us=10000)

def set_ultra_arg():
    set_arg('ultra_cm', ultra_sensor.distance_cm())
