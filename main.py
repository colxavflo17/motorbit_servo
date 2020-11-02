basic.show_icon(IconNames.HAPPY)
motorbit.servo(motorbit.Servos.S1, 90)

def on_forever():
    basic.pause(200)
    motorbit.servo(motorbit.Servos.S1, 160)
    basic.pause(200)
    motorbit.servospeed(motorbit.Servos.S1, 160, 30, 3)
basic.forever(on_forever)
