from time import sleep
from machine import Pin, PWM
#import machine
import time

# Define the Pin numbers for L298N IN1 to IN4
#IN1 = 10
#IN2 = 11
#IN3 = 13
#IN4 = 14

IN1 = 7
IN2 = 8
IN3 = 19
IN4 = 20

# Set the PWM frequency to 1500Hz (adjust this value as needed)
pwm_freq = 1500
speed = 0.8


class Motor_Speed_Main:
    def __init__(self, mot_a_forward=IN1,mot_b_forward=IN2,mot_a_back=IN3,mot_b_back=IN4):
        self.a_forward = Pin(mot_a_forward, Pin.OUT)
        self.b_forward = Pin(mot_b_forward, Pin.OUT)
        self.a_back = Pin(mot_a_back, Pin.OUT)
        self.b_back = Pin(mot_b_back, Pin.OUT)
        # Initialize PWM objects for motor control
        self.EN_A = PWM(Pin(6))
        self.EN_B = PWM(Pin(18))

        self.EN_A.freq(pwm_freq)
        self.EN_B.freq(pwm_freq)


# Set the speed to 50% (you can change this value as needed) range 1 - 0.6 (.5 doesnt move)
    def move_forward(self,speed=speed):
        print("Moving Forward")  
        
        self.a_forward.value(0)
        self.b_forward.value(1)
        self.a_back.value(1)
        self.b_back.value(0)  
               
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))

    def move_backward(self,speed=speed):
        print("Moving Backward")
        
        self.a_forward.value(1)
        self.b_forward.value(0)
        self.a_back.value(0)
        self.b_back.value(1)
        
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))
        
    def move_left(self,speed=speed):
        print("Moving Left")  
        self.a_forward.value(1)
        self.b_forward.value(0)
        self.a_back.value(1)
        self.b_back.value(0)                
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))        

    def move_right(self,speed=speed):
        print("Moving Rigt")  
        self.a_forward.value(0)
        self.b_forward.value(1)
        self.a_back.value(0)
        self.b_back.value(1)                
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))



    def move_stop(self):
        self.a_forward.value(0)
        self.b_forward.value(0)
        self.a_back.value(0)
        self.b_back.value(0)

# Set the speed to 50% (you can change this value as needed) range 1 - 0.6 (.5 doesnt move)
    def move_forward_api(self,speed=speed):
        print("Moving Forward")  
        
        self.a_forward.value(0)
        self.b_forward.value(1)
        self.a_back.value(1)
        self.b_back.value(0)  
               
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))
        
        sleep(.3)
        self.move_stop_api()


    def move_backward_api(self,speed=speed):
        print("Moving Backward")
        
        self.a_forward.value(1)
        self.b_forward.value(0)
        self.a_back.value(0)
        self.b_back.value(1)
        
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))
        sleep(.3)
        self.move_stop_api()
        
    def move_left_api(self,speed=speed):
        print("Moving Left")  
        self.a_forward.value(1)
        self.b_forward.value(0)
        self.a_back.value(1)
        self.b_back.value(0)                
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))        
        sleep(.3)
        self.move_stop_api()
        
    def move_right_api(self,speed=speed):
        print("Moving Rigt")  
        self.a_forward.value(0)
        self.b_forward.value(1)
        self.a_back.value(0)
        self.b_back.value(1)                
        self.EN_A.duty_u16(int(speed * 65535))
        self.EN_B.duty_u16(int(speed * 65535))
        sleep(.3)
        self.move_stop_api()


    def move_stop_api(self):
        self.a_forward.value(0)
        self.b_forward.value(0)
        self.a_back.value(0)
        self.b_back.value(0)



