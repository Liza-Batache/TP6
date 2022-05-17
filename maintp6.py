humidité = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if humidité < 60:
        basic.show_string("Watering the plant")
    else:
        basic.show_string("No need to water the plant")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if input.light_level() < 120:
        basic.show_string("Plants needs more light")
    if input.temperature() < 10:
        basic.show_string("Place the plant in a warmer environment")
basic.forever(on_forever)

def on_every_interval():
    global humidité
    humidité = randint(0, 100)
    basic.show_string("H :")
    basic.show_number(humidité)
    if humidité < 60:
        basic.show_string("Please press logo to water the plant")
loops.every_interval(120000, on_every_interval)
