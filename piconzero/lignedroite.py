#! /usr/bin/env python
#
# Basic test of HC-SR04 ultrasonic sensor on Picon Zero

import hcsr04, time
import piconzero as pz

pz.setInputConfig(2,0)
pz.setInputConfig(3,0)
pz.init()
hcsr04.init()

try:
    while True:
        distance = int(hcsr04.getDistance())
	print( "Distance : "), distance
	if (((pz.readInput(2)!=1) or (pz.readInput(3)!=1)) and distance > 13):
		pz.reverse(60)
	else:
		pz.stop()
		time.sleep(0.2)
		pz.spinRight(50)
		time.sleep(0.2)
		pz.stop()
		break
except KeyboardInterrupt:
    print
finally:
    hcsr04.cleanup()
    pz.cleanup()
