import RPi.GPIO as GPIO

PIR_input = 13			#read PIR Output
Buzzer =11		#LED for signalling motion detected	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.output(Buzzer, GPIO.LOW)

while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        GPIO.output(Buzzer, GPIO.HIGH)
        print("Detected")
    else:
        GPIO.output(Buzzer, GPIO.LOW)
        print("Not Detcted")
