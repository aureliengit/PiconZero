#! /usr/bin/env python
#
# Basic test of HC-SR04 ultrasonic sensor on Picon Zero

import hcsr04, time
import piconzero as pz

hcsr04.init()

try:
    while True:
        distance = int(hcsr04.getDistance())
        print "Distance:", distance
        time.sleep(1)
	if (distance > 40 and distance < 1000):
		pz.reverse(60)

	else:
		pz.stop()
		break
except KeyboardInterrupt:
    print
finally:
    hcsr04.cleanup()
    pz.cleanup()
