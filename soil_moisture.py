import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # GPIO pin 17 is used to read the digital signal

try:
    while True:
        # Read the digital value from the sensor
        sensor_value = GPIO.input(17)
        
        # Check if the sensor is high (wet) or low (dry)
        if sensor_value == GPIO.HIGH:
            print("Soil is wet")
        else:
            print("Soil is dry")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
