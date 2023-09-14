from machine import Pin, time_pulse_us
import time

# Define the ultrasonic sensor's trigger and echo pins
TRIGGER_PIN = 26
ECHO_PIN = 27

# Set the trigger and echo pins as output and input respectively
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # Trigger the ultrasonic sensor to send a pulse
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    # Measure the duration of the pulse
    pulse_duration = time_pulse_us(echo, 1, 30000)  # Timeout after 30ms
    print("Pulse Duration: {} us".format(pulse_duration))

    # Calculate the distance using the speed of sound (343 m/s)
    distance_cm = (pulse_duration / 2) / 29.1

    return distance_cm

while True:
    distance = measure_distance()
    print("Distance: {:.2f} cm".format(distance))
    time.sleep(1)  # Wait for a second before measuring again
