import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 14
Taster = 12

#Linesensors
cny70_left = 24
cny70_right = 7

#SR04
trigger=8
echo=25


Motor1_PWM = 13
Motor1_IN1 = 6
Motor1_IN2 = 5

Motor2_PWM = 22
Motor2_IN1 = 17
Motor2_IN2 = 27

#---------------------------------

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(Taster, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(cny70_left, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(cny70_right, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Using PWM in RPi.GPIO
# see https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
GPIO.setup(Motor1_IN1,GPIO.OUT)
GPIO.setup(Motor1_IN2,GPIO.OUT)
GPIO.setup(Motor1_PWM,GPIO.OUT)
PWM_1 = GPIO.PWM(Motor1_PWM, 90) #GPIO als PWM mit Frequenz 90Hz
PWM_1.start(0) #Duty Cycle = 0

GPIO.setup(Motor2_IN1,GPIO.OUT)
GPIO.setup(Motor2_IN2,GPIO.OUT)
GPIO.setup(Motor2_PWM,GPIO.OUT)
PWM_2 = GPIO.PWM(Motor2_PWM, 90) #GPIO als PWM mit Frequenz 90Hz
PWM_2.start(00) #Duty Cycle = 0


def M1_forward():
    GPIO.output(Motor1_IN2,GPIO.LOW)
    GPIO.output(Motor1_IN1,GPIO.HIGH)
    
def M1_backward():
    GPIO.output(Motor1_IN1,GPIO.LOW)
    GPIO.output(Motor1_IN2,GPIO.HIGH)

def M2_forward():
    GPIO.output(Motor2_IN2,GPIO.LOW)
    GPIO.output(Motor2_IN1,GPIO.HIGH)
    
def M2_backward():
    GPIO.output(Motor2_IN1,GPIO.LOW)
    GPIO.output(Motor2_IN2,GPIO.HIGH)

while (1):
    
    if (GPIO.input(cny70_right) == GPIO.HIGH) & (GPIO.input(cny70_left) == GPIO.HIGH): #black line
            GPIO.output(LED, GPIO.HIGH)
            print("gerade")
            
    if (GPIO.input(cny70_right) == GPIO.HIGH) & (GPIO.input(cny70_left) == GPIO.LOW)
            print("links")

    if (GPIO.input(cny70_right) == GPIO.LOW) & (GPIO.input(cny70_left) == GPIO.HIGH)
            print("rechts")

    if (GPIO.input(cny70_right) == GPIO.LOW) & (GPIO.input(cny70_left) == GPIO.LOW)
            GPIO.output(LED, GPIO.LOW)
            print("stop")
            
            
    sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    M1_forward();