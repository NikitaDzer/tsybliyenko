import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

shim = GPIO.PWM(2, 1000)

try:
    shim.start(0)

    while True:
        call_of_duty = input("Duty cycle: ")

        try:
            if call_of_duty == "q":
                break

            call_of_duty = float(call_of_duty)

            if 0 <= call_of_duty and call_of_duty <= 100:
                shim.ChangeDutyCycle(call_of_duty)
                print("Expected voltage: ", "{:.3f}".format(3.3 * call_of_duty / 100), "V")
            else:
                print("Bad duty cycle.")
            
        except ValueError:
            print("Chell, only numbers >= 0 are available.")


finally:
    shim.stop()
    GPIO.cleanup()