import RPi.GPIO as GPIO
import time
from threading import Thread
from sender import button_send


class ButtonControl:
    gpio_pin = 0

    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def init_button_listener(self):
        Thread(target=self.button_listener, args=()).start()

    def button_listener(self):
        lighting_state = False
        while True:
            input_state = GPIO.input(self.gpio_pin)
            if not input_state:
                print('Button Pressed')
                self.execute_button_function(lighting_state)
                lighting_state = not lighting_state
                time.sleep(0.3)

    def execute_button_function(self, action):
        button_send(action)
