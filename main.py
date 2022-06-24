"""

Set default settings for mouse position and starting axis

"""
# Define Functions

def on_bluetooth_connected():
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            1907,
            5000,
            151,
            255,
            1500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            5000,
            2486,
            253,
            27,
            1500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        SoundExpressionPlayMode.UNTIL_DONE)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

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
    absmouse.movexy(0, 0)
    music.play_melody("- - C C5 C C5 C - ", 1000)
    basic.show_string("#")
    basic.show_leds("""
        # # . # #
                # # . # #
                . . . . .
                # # . # #
                # # . # #
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_logo_pressed():
    global Mouse_Mode
    Mouse_Mode = 0
    control.wait_micros(50)
    keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.APPLE) + "l")
    control.wait_micros(50)
    keyboard.send_string("www.youtube.com")
    keyboard.send_string(keyboard.keys(keyboard._Key.ENTER))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Absolute_Mouse_Y = 0
Absolute_Mouse_X = 0
Mouse_Mode = 0
Input_Mode = 0
keyboard.start_keyboard_service()
absmouse.start_absolute_mouse_service()
mouse.start_mouse_service()
basic.show_string("#")
# Set default settings for mouse position and starting axis
Mouse_Mode = 0
Absolute_Mouse_X = 0
Absolute_Mouse_Y = 0
Mouse_Speed_X = 250
Mouse_Speed_Y = 250
# Main Program

def on_forever():
    global Absolute_Mouse_X, Absolute_Mouse_Y, Mouse_Mode
    if input.button_is_pressed(Button.B):
        keyboard.send_string(keyboard.raw_scancode(44))
        while input.button_is_pressed(Button.B):
            pass
    if Mouse_Mode == 1:
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while Mouse_Mode == 1:
            while Mouse_Mode == 1 and Absolute_Mouse_X <= 32767:
                Absolute_Mouse_X += Mouse_Speed_X
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
                Absolute_Mouse_Y += Mouse_Speed_Y
                absmouse.send(Absolute_Mouse_X,
                    Absolute_Mouse_Y,
                    False,
                    False,
                    False,
                    False)
            if Mouse_Mode == 2:
                Absolute_Mouse_Y = -32767
    if Mouse_Mode == 3:
        for index in range(2):
            basic.show_icon(IconNames.SMALL_DIAMOND)
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    400,
                    600,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.WARBLE,
                    InterpolationCurve.LINEAR),
                SoundExpressionPlayMode.UNTIL_DONE)
            basic.show_icon(IconNames.DIAMOND)
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    400,
                    600,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.WARBLE,
                    InterpolationCurve.LINEAR),
                SoundExpressionPlayMode.UNTIL_DONE)
        if Mouse_Mode == 3:
            music.play_melody("E G - - - - - - ", 1000)
            mouse.click()
            Mouse_Mode = Mouse_Mode + 1
    if Mouse_Mode >= 4:
        Mouse_Mode = 0
        music.play_melody("E D - - - - - - ", 200)
        basic.show_string("#")
basic.forever(on_forever)
