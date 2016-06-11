import RPi.GPIO as GPIO
import time
from helpers.RedisHelper import RedisHelper


class AmbientLightSensor:
    channel = None
    pin_id = None

    def __init__(self, channel, pin_id):
        GPIO.setmode(GPIO.BCM)
        self.channel = channel
        self.pin_id = pin_id

    def RCtime(self, pin, interval=0.5):
        reading = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(interval)
        GPIO.setup(pin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(pin) == GPIO.LOW):
            reading += 1
        return reading

    def start(self, interval):
        while True:
            value = self.RCtime(self.pin_id, interval=1)
            RedisHelper().publish(self.channel, value)
            print('Light Level: ', -1 * value, '                   ', end="\r", flush=True)


if __name__ == '__main__':
    AmbientLightSensor().start(1)
