import RPi.GPIO as GPIO
import time

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17

MAX_VOLTAGE = 3.3
BITS        = 8
LEVELS      = 2 ** BITS

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(LEVELS):
        GPIO.output(dac, d2b(i))
        time.sleep(0.005)
        
        if GPIO.input(comp) == GPIO.LOW:
            return i

    return -1

try:
    while True:
        value = adc()

        if value == -1:
            print("Cannot properly resolve voltage. Minimum voltage: ", MAX_VOLTAGE, "v")
        else:
            print("Voltage: {:.2f} , digit: ".format(value * MAX_VOLTAGE / LEVELS), value)
    

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()