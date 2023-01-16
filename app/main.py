def run():
    from car import left_infra, center_infra, right_infra
    from car import will_collide, display_infra
    from car import adjust_to_left, adjust_to_right, forward, stop
    from car import DEBUG_MODE

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
        