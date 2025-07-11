import RPi.GPIO as GPIO
import time

buttonPin = 17
BLUE = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(BLUE, GPIO.OUT)

try:
	while True:
			if(GPIO.input(buttonPin)):
				print("button released")
				GPIO.output(BLUE, GPIO.HIGH)
			else:
				print("button pressed")
				GPIO.output(BLUE, GPIO.LOW)
			time.sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
