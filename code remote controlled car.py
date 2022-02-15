def on_received_value(name, value):
    if name == "vor" and value == 3:
        motors.dual_motor_power(Motor.AB, 100)
    if name == "rlenken" and value == 2:
        motors.dual_motor_power(Motor.AB, 100)
        motors.dual_motor_power(Motor.AB, 0)
    if name == "llenken" and value == 1:
        motors.dual_motor_power(Motor.A, 100)
        motors.dual_motor_power(Motor.B, 0)
    if name == "Bremsen" and value == 4:
        motors.dual_motor_power(Motor.AB, 0)
radio.on_received_value(on_received_value)
