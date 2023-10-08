import machine
import utime

# Pin Definitions
motor_pwm_pin = machine.Pin(18)  # GP18 as PWM pin for motor speed control
motor_in1_pin = machine.Pin(19)  # GP19 as IN1 pin for motor direction control
motor_in2_pin = machine.Pin(20)  # GP20 as IN2 pin for motor direction control

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

# Main loop
while True:
    print("Running motor forward at half speed")
    control_motor(0.5, "forward")  # Run motor forward at half speed
    utime.sleep(2)                 # Wait for 2 seconds

    print("Running motor backward at full speed")
    control_motor(1.0, "backward") # Run motor backward at full speed
    utime.sleep(2)                 # Wait for 2 seconds

    print("Stopping the motor")
    motor_pwm.duty_u16(0)          # Stop the motor
    utime.sleep(2)                 # Wait for 2 seconds
