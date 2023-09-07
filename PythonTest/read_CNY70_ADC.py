import time
import smbus
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

duty_cycle = 0

LED = 7

Motor1_PWM = 18
Motor1_IN1 = 17
Motor1_IN2 = 22

Motor2_PWM = 19
Motor2_IN1 = 24
Motor2_IN2 = 4

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


# Create a new instance of SMBus
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards

# Address of the ADS1015 ADC (You may need to adjust this if using a different address)
ADS1015_ADDRESS = 0x48

# Configuration for the ADC
ADS1015_CONFIG_REG = 0x01
ADS1015_CONVERSION_REG = 0x00

# Single-shot mode, +/-2.048V range, 128 samples per second
ADS1015_CONFIG_VALUE = 0x8483

# Read the ADC value from a specific channel
def read_adc(channel):
    config = ADS1015_CONFIG_VALUE | (channel << 12)
    bus.write_i2c_block_data(ADS1015_ADDRESS, ADS1015_CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])
    time.sleep(0.001)  # Wait for conversion to complete
    data = bus.read_i2c_block_data(ADS1015_ADDRESS, ADS1015_CONVERSION_REG, 2)
    value = (data[0] << 8) + data[1]
    return value
PWM_1.ChangeDutyCycle(90)
M1_forward()
    
PWM_2.ChangeDutyCycle(90)
M2_forward()
       

try:
    while True:
        sensor_value = read_adc(0)  # Read from channel 0 of ADS1015
        print("Sensor value: {}".format(sensor_value))
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
