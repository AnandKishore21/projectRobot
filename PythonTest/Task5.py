import socketio
import sys
import RPi.GPIO as GPIO
import time

from gpiozero import DistanceSensor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 7
Taster = 5


#SR04
trigger=25
echo=27

Motor1_PWM = 18
Motor1_IN1 = 17
Motor1_IN2 = 22

Motor2_PWM = 19
Motor2_IN1 = 24
Motor2_IN2 = 4

def Forward():

    
    GPIO.output(Motor1_IN2,GPIO.LOW)
    GPIO.output(Motor1_IN1,GPIO.HIGH)
    GPIO.output(Motor2_IN2,GPIO.LOW)
    GPIO.output(Motor2_IN1,GPIO.HIGH)
    PWM_1.ChangeDutyCycle(30)
    PWM_2.ChangeDutyCycle(30)
    
def Backward():
    
    GPIO.output(Motor1_IN1,GPIO.LOW)
    GPIO.output(Motor1_IN2,GPIO.HIGH)
    GPIO.output(Motor2_IN1,GPIO.LOW)
    GPIO.output(Motor2_IN2,GPIO.HIGH)
    PWM_1.ChangeDutyCycle(30)
    PWM_2.ChangeDutyCycle(30)

    
def Stop():
    GPIO.output(Motor1_PWM, GPIO.LOW)
    GPIO.output(Motor2_PWM, GPIO.LOW)
    GPIO.output(Motor1_IN1,GPIO.LOW)
    GPIO.output(Motor1_IN2,GPIO.LOW)
    GPIO.output(Motor2_IN1,GPIO.LOW)
    GPIO.output(Motor2_IN2,GPIO.LOW)

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

GPIO.setup(LED, GPIO.OUT)

sensor = DistanceSensor(echo=27, trigger=25)

sio =  socketio.Client()

@sio.event
def connect():
	print('connected')

@sio.event
def connect_error(e):
	print('error')

@sio.event
def disconnect():
	print('disconnected')

@sio.event
def forward(data):
    print('forward', data)
    if data == 1:
        while 1:
            d = sensor.distance*100
            sio.emit('distance',d)
            Forward()
            sleep(0.1)
            if d <= 10:
                sio.emit('forward',0)
                Stop()
                break
            d = round(d)
            
        else:
            Stop()

@sio.event
def backward(data):
    print('backward', data)
    if data == 1:
        while 1:
            d = sensor.distance*100
            sio.emit('distance',d)
            Backward()
            sleep(0.1)
            if d >= 50:
                sio.emit('backward',0)
                Stop()
                break
        d = round(d)
       
       
    else:
        Stop()

sio.connect('http://localhost:8080')
sio.wait()


    
        
  
    
    