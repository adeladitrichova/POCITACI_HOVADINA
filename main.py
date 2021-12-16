press = 0
hold = 0
reset = 0
def on_forever():
    def on_button_pressed_a():
        global press
        add = 1
        result = press + add
        press = result
        basic.show_number(result)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_logo_event_pressed():
        result = reset
        basic.show_number(reset)
    input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
basic.forever(on_forever)