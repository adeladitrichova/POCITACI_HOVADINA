let press = 0
let hold = 0
let reset = 0
basic.forever(function on_forever() {
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        let add = 1
        let result = press + add
        press = result
        basic.showNumber(result)
    })
    input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
        let result = reset
        basic.showNumber(reset)
    })
})
