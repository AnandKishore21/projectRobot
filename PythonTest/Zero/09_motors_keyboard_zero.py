import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 14
Taster = 12

Motor1_PWM = 13
Motor1_IN1 = 6
Motor1_IN2 = 5

Motor2_PWM = 22
Motor2_IN1 = 17
Motor2_IN2 = 27

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(Taster, GPIO.IN, pull_up_down = GPIO.PUD_UP)

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
PWM_2.start(0) #Duty Cycle = 0


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
   
#       z
# s    g h
#y      b
 
    key = input("Taste ")
        
    if key == "y": #forward fast
        PWM_1.ChangeDutyCycle(100)
        M1_forward()
        PWM_2.ChangeDutyCycle(100)
        M2_forward()
    
    
    if key == "z": #forward slow
        PWM_1.ChangeDutyCycle(30)
        M1_forward()
        PWM_2.ChangeDutyCycle(30)
        M2_forward()
        
       
    if key == "b": # backward slow
        PWM_1.ChangeDutyCycle(50)
        M1_backward()
        PWM_2.ChangeDutyCycle(50)
        M2_backward()
        
    if key == "g": #left
        PWM_1.ChangeDutyCycle(70)
        M1_forward()
        PWM_2.ChangeDutyCycle(25)
        M2_forward()  
        
    if key == "h": #right
        PWM_1.ChangeDutyCycle(25)
        M1_forward()
        PWM_2.ChangeDutyCycle(70)
        M2_forward()
        
    if key == "s": #stop
        PWM_1.ChangeDutyCycle(0)
        PWM_2.ChangeDutyCycle(0)

    if key == "q": #quit
        exit()