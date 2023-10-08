import machine
import utime

# GPS Module UART Connection
gps_module = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# Function to read GPS data
def read_gps_data():
    while True:
        line = gps_module.readline()
        if line:
            try:
                sentence = line.decode("utf-8").strip()
                if sentence.startswith("$GPGGA"):
                    parts = sentence.split(',')
                    if len(parts) >= 15 and parts[6] == "1":
                        latitude = float(parts[2]) / 100
                        longitude = float(parts[4]) / 100
                        if parts[3] == "S":
                            latitude = -latitude
                        if parts[5] == "W":
                            longitude = -longitude
                        satellites = int(parts[7])
                        gps_time = parts[1][:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                        return latitude, longitude, satellites, gps_time
            except Exception as e:
                print("Error:", e)
        utime.sleep_ms(500)

while True:
    try:
        latitude, longitude, satellites, gps_time = read_gps_data()
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Satellites:", satellites)
        print("GPS Time:", gps_time)
    except Exception as e:
        print("Error:", e)
    utime.sleep(1)  # Read GPS data every second
