import RPi.GPIO as GPIO
import time
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
    M1_forward()
    M2_forward()
    
    rVal = GPIO.input(cny70_right)
    lVal = GPIO.input(cny70_left)
    print("Right:",rVal)
    print("lVal:",lVal)
    time.sleep
    
    
    
