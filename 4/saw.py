import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
period = 0

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        period = input("Period in seconds: ")

        if period == "q":
            break
        
        try:
            period = float(period) / (2 * 256)


            while True:
                for i in range(255):
                    GPIO.output(dac, decimal2binary(i))
                    time.sleep(period)

                for i in range(255, 0, -1):
                    GPIO.output(dac, decimal2binary(i))
                    time.sleep(period)


        except ValueError:
            print("You can use only numbers >= 0.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

