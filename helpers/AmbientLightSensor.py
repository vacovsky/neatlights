import RPi.GPIO as GPIO
import time

PIN_ID = 25
GPIO.setmode(GPIO.BCM)


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

if __name__ == '__main__':
    ambientlight = 0
    while True:  # ambientlight > 0:
        ambientlight = RCtime(PIN_ID)
        time.sleep(1)
        if ambientlight > 0:
            print(ambientlight)
        else:
            print("bright light!")
