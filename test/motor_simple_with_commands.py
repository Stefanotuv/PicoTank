import machine
from machine import Pin
import utime

# Pin Definitions
motor_pwm_pin = machine.Pin(6)  # GP18 as PWM pin for motor speed control
motor_in1_pin = machine.Pin(7,Pin.OUT)  # GP19 as IN1 pin for motor direction control
motor_in2_pin = machine.Pin(8,Pin.OUT)  # GP20 as IN2 pin for motor direction control

# Configure PWM for motor speed control
motor_pwm = machine.PWM(motor_pwm_pin)
motor_pwm.freq(1500)  # Set PWM frequency to 1000 Hz

# Function to control motor direction and speed
def control_motor(speed, direction):
    print(f"Setting motor speed: {speed}, direction: {direction}")
    if direction == "forward":
        motor_in1_pin.value(1)
        motor_in2_pin.value(0)
    elif direction == "backward":
        motor_in1_pin.value(0)
        motor_in2_pin.value(1)
    else:
        motor_in1_pin.value(0)
        motor_in2_pin.value(0)

    motor_pwm.duty_u16(int(speed * 65535))  # Set motor speed (0 to 65535)
    
while True:
    user_input = input("Enter 's' to stop, 'f' for forward, or 'b' for backward: ")

    if user_input == 's':
        print("Stopping the motor")
        control_motor(0, "stop")  # Stop the motor
    elif user_input == 'f':
        print("Running motor forward at half speed")
        control_motor(0.4, "forward")  # Run motor forward at half speed
    elif user_input == 'b':
        print("Running motor backward at full speed")
        control_motor(0.4, "backward")  # Run motor backward at full speed
    else:
        print("Invalid input. Please enter 's', 'f', or 'b'.")

    utime.sleep(2)  # Wait for 2 seconds





