input.onButtonPressed(Button.A, function () {
    if (input.temperature() > 37.5) {
        soundExpression.sad.playUntilDone()
    } else {
        music.stopAllSounds()
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.lightLevel() > 50) {
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
    } else {
        music.stopAllSounds()
    }
})
