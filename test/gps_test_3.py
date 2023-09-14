import machine
from machine import UART, I2C,SoftI2C
from ssd1306 import SSD1306_I2C
import utime

# Initialize UART for GPS module
gps_uart = UART(1, baudrate=9600, tx=machine.Pin(8), rx=machine.Pin(9))

# Initialize I2C for OLED display
i2c = SoftI2C(sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

# Initialize OLED display
oled.fill(0)
oled.text("Testing GPS Module", 0, 0)
oled.show()

print("GPS Module Testing")

# Read and display GPS data
while True:
    gps_data = gps_uart.readline()
    if gps_data:
        decoded_data = gps_data.decode('utf-8').strip()
        print("Received GPS Data:", decoded_data)

        oled.fill(0)
        oled.text("GPS Data Received:", 0, 0)
        oled.text(decoded_data, 0, 20)
        oled.show()
        utime.sleep(1)  # Display data for 1 second
    else:
        print("No GPS Data")

        oled.fill(0)
        oled.text("No GPS Data", 0, 0)
        oled.show()
