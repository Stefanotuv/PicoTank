import machine
from machine import Pin,PWN
import utime
from time import sleep

# Pin Definitions
motor_pwm_pin = 6  # GP18 as PWM pin for motor speed control
motor_in1_pin = 7  # GP19 as IN1 pin for motor direction control
motor_in2_pin = 8  # GP20 as IN2 pin for motor direction control

# Configure PWM for motor speed control
motor_pwm = machine.PWM(motor_pwm_pin)
motor_pwm.freq(1500)  # Set PWM frequency to 1000 Hz
speed = .8

class Motor_Steps_Main:
    def __init__(self, mot_a_forward=motor_in1_pin,mot_a_back=motor_in2_pin,EN_A=motor_pwm_pin,speed=speed):
            self.a_forward = Pin(mot_a_forward, Pin.OUT)
            self.a_back = Pin(mot_a_back, Pin.OUT)
            
            # Initialize PWM objects for motor control
            self.EN_A = PWM(Pin(EN_A))
            self.speed = speed

    def move_forward(self,speed=self.speed):
        print("Moving Forward")  
        self.a_forward.value(0)
        self.a_back.value(1)
        self.EN_A.duty_u16(int(speed * 65535))
        
    def move_backward(self,speed=self.speed):
        print("Moving Backrward")  
        self.a_forward.value(1)
        self.a_back.value(0)
        self.EN_A.duty_u16(int(speed * 65535))
    
    def stop(self):
        print("Moving Backrward")  
        self.a_forward.value(0)
        self.a_back.value(0)        
        
    def step_forward(self,step=.1):
        self.move_forward()
        sleep(step)
        self.stop()

    def step_backward(self,step=.1):
        self.move_backward()
        sleep(step)
        self.stop()        
        