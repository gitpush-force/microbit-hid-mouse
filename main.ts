bluetooth.onBluetoothConnected(function () {
    music.playMelody("C F C F C F - - ", 600)
})
input.onButtonPressed(Button.A, function () {
    if (Mouse_Mode == 3) {
        Mouse_Mode = 0
    } else {
        Mouse_Mode = Mouse_Mode + 1
    }
})
input.onButtonPressed(Button.AB, function () {
    Mouse_Mode = 0
    Absolute_Mouse_X = 0
    Absolute_Mouse_Y = 0
    music.playMelody("- - C C5 C - - - ", 1000)
    basic.showString("#")
})
input.onButtonPressed(Button.B, function () {
    Mouse_Mode = 0
    control.waitMicros(50)
    keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.apple) + "l")
    control.waitMicros(50)
    keyboard.sendString("www.youtube.com")
    keyboard.sendString(keyboard.keys(keyboard._Key.enter))
})
let Absolute_Mouse_Y = 0
let Absolute_Mouse_X = 0
let Mouse_Mode = 0
keyboard.startKeyboardService()
absmouse.startAbsoluteMouseService()
mouse.startMouseService()
absmouse.movexy(0, 0)
// Set default settings for mouse position and starting axis
Mouse_Mode = 0
Absolute_Mouse_X = -32767
Absolute_Mouse_Y = -32767
basic.showString("#")
// Main Program
basic.forever(function () {
    if (Mouse_Mode == 1) {
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while (Mouse_Mode == 1) {
            while (Mouse_Mode == 1 && Absolute_Mouse_X <= 32767) {
                Absolute_Mouse_X += 250
                absmouse.send(
                Absolute_Mouse_X,
                Absolute_Mouse_Y,
                false,
                false,
                false,
                false
                )
            }
            if (Mouse_Mode == 1) {
                Absolute_Mouse_X = -32767
            }
        }
    }
    if (Mouse_Mode == 2) {
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while (Mouse_Mode == 2) {
            while (Mouse_Mode == 2 && Absolute_Mouse_Y <= 32767) {
                Absolute_Mouse_Y += 250
                absmouse.send(
                Absolute_Mouse_X,
                Absolute_Mouse_Y,
                false,
                false,
                false,
                false
                )
            }
            if (Mouse_Mode == 2) {
                Absolute_Mouse_Y = -32767
            }
        }
    }
    if (Mouse_Mode == 3) {
        basic.showIcon(IconNames.SmallDiamond)
        music.playMelody("E - E - E - E - ", 200)
        if (Mouse_Mode == 3) {
            music.playMelody("E G - - - - - - ", 1000)
            mouse.click()
            Mouse_Mode = Mouse_Mode + 1
        }
    }
    if (Mouse_Mode >= 4) {
        Mouse_Mode = 0
        music.playMelody("- G A - - - - - ", 1000)
        basic.showString("#")
    }
})
