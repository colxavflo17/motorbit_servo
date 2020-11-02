basic.showIcon(IconNames.Happy)
motorbit.Servo(motorbit.Servos.S1, 90)
basic.forever(function on_forever() {
    basic.pause(200)
    motorbit.Servo(motorbit.Servos.S1, 160)
    basic.pause(200)
    motorbit.Servospeed(motorbit.Servos.S1, 160, 30, 3)
})
