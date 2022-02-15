def on_button_pressed_a():
    radio.send_value("llenken", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    radio.send_value("Bremsen", 4)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    radio.send_value("vor", 3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_value("rlenken", 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
radio.set_transmit_power(7)
