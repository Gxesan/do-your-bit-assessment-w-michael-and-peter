def on_button_pressed_a():
    if input.temperature() > 37.5:
        soundExpression.sad.play_until_done()
    else:
        music.stop_all_sounds()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if gatorParticle.heartbeat(HeartbeatType.BPM) > 85:
        music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if input.light_level() > 50:
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
    else:
        music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

gatorParticle.begin()