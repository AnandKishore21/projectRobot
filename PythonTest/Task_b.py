import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Taster = 5

Motor1_PWM = 18
Motor1_IN1 = 17
Motor1_IN2 = 22

Motor2_PWM = 19
Motor2_IN1 = 24
Motor2_IN2 = 4

GPIO.setup(Taster, GPIO.IN, pull_up_down = GPIO.PUD_UP)

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

while (1):
    if GPIO.input(Taster) == GPIO.LOW: 
        PWM_1.ChangeDutyCycle(70) #LEFT MOTOR WILL RUN FOR 10 SECONDS WITH 70% DUTYCYCLE
        M1_forward() #This function will rotate the Left motor in forward direction
        time.sleep(10)
        PWM_1.ChangeDutyCycle(0) #MOTOR 1 STOP
        
        PWM_2.ChangeDutyCycle(70) #RIGHT MOTOR WILL RUN FOR 10 SECONDS WITH 70% DUTYCYCLE
        M2_forward() #This function will rotate the Right motor in forward direction
        time.sleep(10)
        PWM_2.ChangeDutyCycle(0) #MOTOR 2 STOP






