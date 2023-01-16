from app.car import left_infra, center_infra, right_infra
from app.car import will_collide, display_infra
from app.car import adjust_to_left, adjust_to_right, forward, stop
from app.car import DEBUG_MODE

def run():

    while True:
        if DEBUG_MODE:
            display_infra()
        
        if will_collide():
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
        