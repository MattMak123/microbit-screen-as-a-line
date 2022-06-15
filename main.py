def on_button_pressed_ab():
    flybit.disarm_block()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

flybit.start_radio(62)
basic.show_leds("""
    # # # . .
        # . # . #
        # # # # .
        # . # . #
        # . # . .
""")
basic.show_string("ijijijij")
basic.pause(100)
flybit.initial_animation(IconNames.HEART, 500)

def on_forever():
    pass
basic.forever(on_forever)
