import Adafruit_DHT
import time

# Set the sensor type and the GPIO pin
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin number where the data pin of DHT11 is connected

while True:
    # Read the humidity and temperature from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Check if the reading was successful
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature}°C  Humidity: {humidity}%')
    else:
        print('Failed to get reading. Try again!')

    # Wait for a while before the next reading
    time.sleep(2)
