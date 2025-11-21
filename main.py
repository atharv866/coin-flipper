def on_button_pressed_a():
    if Math.random_boolean():
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            # # # # #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)
