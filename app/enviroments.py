possible_states = ['bang-bang', 'pid', 'ble_flutter']

envs = {
    'DEBUG_MODE': False,
    'COLLISION_CHECK': False,

    # Finite State Machine
    'INITIAL_STATE': possible_states[0],

    # Bluetooth Options
    'BLUETOOTH_NAME': 'ragnarok',

    # Infrareds
    'left_infra': 34,
    'center_infra': 35,
    'right_infra': 19,

    # Ultrasonic
    'ultra_trigger': 13,
    'ultra_echo': 12,

    # Wheels
    'frequency': 1000,

    'left_pin1': 5,
    'left_pin2': 18,
    'left_enable_pin': 32,

    'right_pin1': 16,
    'right_pin2': 17,
    'right_enable_pin': 33,

    'min_duty': 400,
    'max_duty': 1023,

    'speed': 30,

    # PID
    'KP': 1.0,
    'KI': 0.1,
    'KD': 0.5,
    'LIMIT': 50
}
