import RPi.GPIO as GPIO

from gpiozero import DistanceSensor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 7
Taster = 5
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Taster, GPIO.IN, pull_up_down = GPIO.PUD_UP)
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

GPIO.setup(Motor1_IN1,GPIO.OUT)
GPIO.setup(Motor1_IN2,GPIO.OUT)
GPIO.setup(Motor1_PWM,GPIO.OUT)
PWM_1 = GPIO.PWM(Motor1_PWM, 90) #GPIO als PWM mit Frequenz 90Hz
PWM_1.start(0) #Duty Cycle = 0


GPIO.setup(Motor2_IN1,GPIO.OUT)
GPIO.setup(Motor2_IN2,GPIO.OUT)
GPIO.setup(Motor2_PWM,GPIO.OUT)
PWM_2 = GPIO.PWM(Motor2_PWM, 90) #GPIO als PWM mit Frequenz 90Hz
PWM_2.start(0) #Duty Cycle = 0

def M1_forward():
    GPIO.output(Motor1_IN2,GPIO.LOW)
    GPIO.output(Motor1_IN1,GPIO.HIGH)


def M2_forward():
    GPIO.output(Motor2_IN2,GPIO.LOW)
    GPIO.output(Motor2_IN1,GPIO.HIGH)

sensor = DistanceSensor(echo=27, trigger=25)


# Display the distance
j=0
arr = [None]*1000

GPIO.output(LED, GPIO.LOW)
sleep(10)

PWM_1.ChangeDutyCycle(75) #LEFT MOTOR WITH 75% DUTYCYCLE
PWM_2.ChangeDutyCycle(75) #LEFT MOTOR WITH 75% DUTYCYCLE

while True:
        
    GPIO.output(LED, GPIO.HIGH)
    M1_forward() #This function will rotate the Left motor in forward direction
    M2_forward() #This function will rotate the Right motor in forward direction
    arr[j] = (sensor.distance * 100)
    j=j+1
    sleep(0.1)
    
    if (GPIO.input(Taster) == GPIO.LOW):
        PWM_1.ChangeDutyCycle(0)
        PWM_2.ChangeDutyCycle(0)
        j=0
        while j<=1000:
            
            print (str(arr[j]) + " " + ",")
            j = j+1
   
        sleep(1)
        

        

