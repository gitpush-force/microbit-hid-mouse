def on_bluetooth_connected():
    music.play_tone(131, music.beat(BeatFraction.EIGHTH))
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_button_pressed_a():
    global Mouse_Clicks
    Mouse_Clicks = Mouse_Clicks + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Mouse_Clicks, Absolute_Mouse_X, Absolute_Mouse_Y
    Mouse_Clicks = 0
    Absolute_Mouse_X = 0
    Absolute_Mouse_Y = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Absolute_Mouse_Y = 0
Absolute_Mouse_X = 0
Mouse_Clicks = 0
absmouse.start_absolute_mouse_service()
mouse.start_mouse_service()
absmouse.movexy(0, 0)
# Set default settings for mouse position and starting axis
Mouse_Clicks = 0
Absolute_Mouse_X = -32767
Absolute_Mouse_Y = -32767
basic.show_string("!")
# Main Program

def on_forever():
    global Absolute_Mouse_X, Absolute_Mouse_Y, Mouse_Clicks
    while Mouse_Clicks == 0:
        basic.show_string("#")
    if Mouse_Clicks == 1:
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while Mouse_Clicks == 1:
            while Mouse_Clicks == 1 and Absolute_Mouse_X <= 32767:
                Absolute_Mouse_X += 250
                absmouse.send(Absolute_Mouse_X,
                    Absolute_Mouse_Y,
                    False,
                    False,
                    False,
                    False)
            if Mouse_Clicks == 1:
                Absolute_Mouse_X = -32767
    if Mouse_Clicks == 2:
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while Mouse_Clicks == 2:
            while Mouse_Clicks == 2 and Absolute_Mouse_Y <= 32767:
                Absolute_Mouse_Y += 250
                absmouse.send(Absolute_Mouse_X,
                    Absolute_Mouse_Y,
                    False,
                    False,
                    False,
                    False)
            if Mouse_Clicks == 2:
                Absolute_Mouse_Y = -32767
        while Mouse_Clicks == 3:
            mouse.click()
            mouse.click()
        if Mouse_Clicks >= 4:
            basic.show_string("$")
            Mouse_Clicks = 0
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
