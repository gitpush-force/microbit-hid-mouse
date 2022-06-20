// Define Functions
bluetooth.onBluetoothConnected(function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 1907, 5000, 151, 255, 1500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
})
bluetooth.onBluetoothDisconnected(function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 2486, 253, 27, 1500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
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
    absmouse.movexy(0, 0)
    music.playMelody("- - C C5 C C5 C - ", 1000)
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
basic.showString("#")
// Set default settings for mouse position and starting axis
Mouse_Mode = 0
Absolute_Mouse_X = -32767
Absolute_Mouse_Y = -32767
let Mouse_Speed_X = 250
let Mouse_Speed_Y = 250
// Main Program
basic.forever(function () {
    if (Mouse_Mode == 1) {
        absmouse.movexy(Absolute_Mouse_X, Absolute_Mouse_Y)
        while (Mouse_Mode == 1) {
            while (Mouse_Mode == 1 && Absolute_Mouse_X <= 32767) {
                Absolute_Mouse_X += Mouse_Speed_X
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
                Absolute_Mouse_Y += Mouse_Speed_Y
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
        for (let index = 0; index < 2; index++) {
            basic.showIcon(IconNames.SmallDiamond)
            music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
            basic.showIcon(IconNames.Diamond)
            music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
        }
        if (Mouse_Mode == 3) {
            music.playMelody("E G - - - - - - ", 1000)
            mouse.click()
            Mouse_Mode = Mouse_Mode + 1
        }
    }
    if (Mouse_Mode >= 4) {
        Mouse_Mode = 0
        music.playMelody("E D - - - - - - ", 200)
        basic.showString("#")
    }
})
