import RPi.GPIO as GPIO
import time

#pin and button layout
red_button_pin = 17
green_button_pin = 27
blue_button_pin = 22

red_led_pin = 26
green_led_pin = 19
blue_led_pin = 13

#set GPIO mode
GPIO.setmode(GPIO.BCM)

#setup LED pins as outputs
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)

#setup button pins as inputs
GPIO.setup(red_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blue_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#function for LEDs
def turn_off_all():
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.output(blue_led_pin, GPIO.LOW)

#all LEDs off
turn_off_all()

try:
    while True:
        #read button states
        red_state = GPIO.input(red_button_pin)
        green_state = GPIO.input(green_button_pin)
        blue_state = GPIO.input(blue_button_pin)

        #LEDs based on button states
        if red_state == GPIO.LOW:
            GPIO.output(red_led_pin, GPIO.HIGH)
            GPIO.output(green_led_pin, GPIO.LOW)
            GPIO.output(blue_led_pin, GPIO.LOW)
        elif red_state == GPIO.HIGH:
            turn_off_all()

        if green_state == GPIO.LOW:
            GPIO.output(red_led_pin, GPIO.LOW)
            GPIO.output(green_led_pin, GPIO.HIGH)
            GPIO.output(blue_led_pin, GPIO.LOW)
        elif green_state == GPIO.HIGH:
            turn_off_all()

        if blue_state == GPIO.LOW:
            GPIO.output(red_led_pin, GPIO.LOW)
            GPIO.output(green_led_pin, GPIO.LOW)
            GPIO.output(blue_led_pin, GPIO.HIGH)
        elif blue_state == GPIO.HIGH:
            turn_off_all()

        time.sleep(0.02)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()