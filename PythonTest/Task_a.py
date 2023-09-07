import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 7
Taster = 5

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Taster, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Pressing the pushbutton (Taster) LED is ON
while (1):
        if GPIO.input(Taster) == GPIO.LOW: # BUTTON IS CONNECTED TO GND WHEN PRESSED(GPIO.LOW)
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)

