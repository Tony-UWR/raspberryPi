import RPi.GPIO as GPIO
import time

sensor = 16
led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,False)
print ("IR Sensor Ready.....")
print (" ")

try: 
   while True:
      if GPIO.input(sensor)==False:
          GPIO.output(led,True)
          print ("Object Detected")
          
      if GPIO.input(sensor)==True:
          GPIO.output(led,False)


except KeyboardInterrupt:
    GPIO.cleanup()
