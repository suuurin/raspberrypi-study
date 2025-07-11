import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RED = 14
GREEN = 15
BLUE = 18

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
time.sleep(5)
GPIO.cleanup([14, 15, 18])
