# webserver.py
    
from robot_controller import RobotController
import utime

if __name__ == "__main__":
    controller = RobotController()
    try:
        controller.start()
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt (Ctrl+C) here
        
        print("Program interrupted by user.")
        controller.oled.fill(0)
        controller.oled.text("Goodbye", 0, 0)
        controller.oled.show()
        controller.oled.fill(0)
        controller.oled.show()
        # You can perform cleanup or other necessary actions here    
