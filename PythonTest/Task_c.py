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
    
def M1_backward():
    GPIO.output(Motor1_IN1,GPIO.LOW)
    GPIO.output(Motor1_IN2,GPIO.HIGH)


def M2_forward():
    GPIO.output(Motor2_IN2,GPIO.LOW)
    GPIO.output(Motor2_IN1,GPIO.HIGH)

def M2_backward():
    GPIO.output(Motor2_IN1,GPIO.LOW)
    GPIO.output(Motor2_IN2,GPIO.HIGH)

i=20 #duty cycle will start from 20% as below 20% motors are not working correctly due to low current.
while (1):
    
    if GPIO.input(Taster) == GPIO.LOW:
        
        while(i<=100): #ACCELERATION IN FORWARD DIRECTION
            PWM_1.ChangeDutyCycle(i)
            PWM_2.ChangeDutyCycle(i)
            M1_forward()
            M2_forward()
            print(i)
            time.sleep(0.3)
            i = i+1

        i = 100
        
        while(i>=20): #DECELERATION IN FORWARD DIRECTION
            PWM_1.ChangeDutyCycle(i)
            PWM_2.ChangeDutyCycle(i)
            M1_forward()
            M2_forward()
            print(i)
            time.sleep(0.3)
            i = i-1
            
        PWM_1.ChangeDutyCycle(0)
        PWM_2.ChangeDutyCycle(0)
        
        i = 20
        
        while(i<=100): #ACCELERATION IN BACKWARD DIRECTION
            PWM_1.ChangeDutyCycle(i)
            PWM_2.ChangeDutyCycle(i)
            M1_backward()
            M2_backward()
            print(i)
            time.sleep(0.3)
            i = i+1
            
        i = 100
        
        while(i>=20): #DECELERATION IN BACKWARD DIRECTION
            PWM_1.ChangeDutyCycle(i)
            PWM_2.ChangeDutyCycle(i)
            M1_backward()
            M2_backward()
            print(i)
            time.sleep(0.3)
            i = i-1
            
        PWM_1.ChangeDutyCycle(0) # MOTOR1 STOP
        PWM_2.ChangeDutyCycle(0) # MOTOR2 STOP
        
        
            
        

            
            

        
            

      









