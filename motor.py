def motorstart():
    import RPi.GPIO as GPIO
    from time import sleep
    from gpiozero import LED
    grøn = LED (17)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, 1)


    GPIO.output(18, 0)
    grøn.on()
    sleep(1)
    GPIO.output(18, 1)
    grøn.off()
