
def on_bluetooth_connected():
    music.play_melody("C F C F C F - - ", 600)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_button_pressed_a():
    global Mouse_Mode
    if Mouse_Mode == 3:
        Mouse_Mode = 0
    else:
        Mouse_Mode = Mouse_Mode + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Mouse_Mode, Absolute_Mouse_X, Absolute_Mouse_Y
    Mouse_Mode = 0
    Absolute_Mouse_X = 0
    Absolute_Mouse_Y = 0
    music.play_melody("- - C C5 C - - - ", 1000)
    basic.show_string("#")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Mouse_Mode
    Mouse_Mode = 0
    control.wait_micros(50)
    keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.APPLE) + "l")
    control.wait_micros(50)
    keyboard.send_string("www.youtube.com")
    keyboard.send_string(keyboard.keys(keyboard._Key.ENTER))
input.on_button_pressed(Button.B, on_button_pressed_b)

Absolute_Mouse_Y = 0
Absolute_Mouse_X = 0
Mouse_Mode = 0
keyboard.start_keyboard_service()
absmouse.start_absolute_mouse_service()
mouse.start_mouse_service()
absmouse.movexy(0, 0)
# Set default settings for mouse position and starting axis
Mouse_Mode = 0
Absolute_Mouse_X = -32767
Absolute_Mouse_Y = -32767
basic.show_string("#")
# Main Program

def on_forever():
    global Absolute_Mouse_X, Absolute_Mouse_Y, Mouse_Mode
    if Mouse_Mode == 1:
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while Mouse_Mode == 1:
            while Mouse_Mode == 1 and Absolute_Mouse_X <= 32767:
                Absolute_Mouse_X += 250
                absmouse.send(Absolute_Mouse_X,
                    Absolute_Mouse_Y,
                    False,
                    False,
                    False,
                    False)
            if Mouse_Mode == 1:
                Absolute_Mouse_X = -32767
    if Mouse_Mode == 2:
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while Mouse_Mode == 2:
            while Mouse_Mode == 2 and Absolute_Mouse_Y <= 32767:
                Absolute_Mouse_Y += 250
                absmouse.send(Absolute_Mouse_X,
                    Absolute_Mouse_Y,
                    False,
                    False,
                    False,
                    False)
            if Mouse_Mode == 2:
                Absolute_Mouse_Y = -32767
    if Mouse_Mode == 3:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        music.play_melody("E - E - E - E - ", 200)
        if Mouse_Mode == 3:
            music.play_melody("E G - - - - - - ", 1000)
            mouse.click()
            Mouse_Mode = Mouse_Mode + 1
    if Mouse_Mode >= 4:
        Mouse_Mode = 0
        music.play_melody("- G A - - - - - ", 1000)
        basic.show_string("#")
basic.forever(on_forever)
