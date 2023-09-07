import RPi.GPIO as GPIO

from gpiozero import DistanceSensor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 7
Taster = 5

#Linesensors
cny70_left = 16
cny70_right = 26

#SR04
trigger=25
echo=27

Motor1_PWM = 18
Motor1_IN1 = 17
Motor1_IN2 = 22

Motor2_PWM = 19
Motor2_IN1 = 24
Motor2_IN2 = 4


i = 0

GPIO.setup(LED, GPIO.OUT)

sensor = DistanceSensor(echo=27, trigger=25)

# Display the distance and LED is blinking
while True:
    print("Distance: ", sensor.distance * 100)
   
    GPIO.output(LED, GPIO.HIGH)
    sleep(1)
    GPIO.output(LED, GPIO.LOW)
    sleep(1)
    