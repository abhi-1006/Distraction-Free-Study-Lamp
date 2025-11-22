lightValue = 0
# Microbit A - phone detector
radio.set_group(7)
threshold = 200

def on_forever():
    global lightValue
    lightValue = input.light_level()
    if lightValue < threshold:
        # Phone is inside
        radio.send_string("OK")
    else:
        # Phone removed
        radio.send_string("ALARM")
        basic.show_icon(IconNames.NO)
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
    basic.pause(500)
basic.forever(on_forever)
