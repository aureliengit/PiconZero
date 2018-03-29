import RPi.GPIO as GPIO

sensor=3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

try:
	while True:
		if GPIO.input(sensor):
			print "White"
		else:
			print "Black"

finally:
	GPIO.cleanup()
