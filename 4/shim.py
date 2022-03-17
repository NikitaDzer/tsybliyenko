import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(24, 0.5)
p.start(100)
input("Press return to stop:");
p.stop()
GPIO.cleanup()