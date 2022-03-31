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

def adc_sar():
    value = 0

    for i in range(7, -1, -1):
        step   = 2 ** i
        value += step

        GPIO.output(dac, d2b(value))
        time.sleep(0.005)
        
        if GPIO.input(comp) == GPIO.LOW:
            value -= step

    return value

try:
    while True:
        value = adc_sar()

        print("Voltage: {:.2f} V, digit: ".format(value * MAX_VOLTAGE / LEVELS), value)
    

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()