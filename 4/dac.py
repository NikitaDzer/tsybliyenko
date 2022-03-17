import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
period = 0

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("[0, 255]: ")

        if num.isdigit():
            num = int(num)

            if (0 <= num and num <= 255):
                GPIO.output(dac, decimal2binary(num))
                print("Expected CAP: ", "{:.3f}".format(3.3 * num / 255), "V")
            else:
                print("Bro, available range - [0, 255].")

        elif num == "q":
            break

        print("Why did you write it? Only numbers [0, 255] are available.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
