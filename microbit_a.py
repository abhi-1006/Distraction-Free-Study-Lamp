def on_button_pressed_a():
    global running, timeLeft
    running = True
    timeLeft = 1500
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global running
    if receivedString == "ALARM":
        running = False
        basic.show_icon(IconNames.NO)
        music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
            MelodyOptions.ONCE)
    elif receivedString == "OK":
        running = True
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global running, timeLeft
    running = False
    timeLeft = 1500
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

running = False
timeLeft = 0
timeLeft = 1500
radio.set_group(7)

def on_forever():
    global timeLeft
    if running:
        basic.show_number(Math.idiv(timeLeft, 60))
        if timeLeft > 0:
            timeLeft += 0 - 1
        basic.pause(500)
basic.forever(on_forever)
