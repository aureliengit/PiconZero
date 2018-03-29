#!/usr/bin/python
#coding=utf-8

import time
import piconzero as pz
import hcsr04

pz.init()
hcsr04.init()

try:
	while True:
		distance = int(hcsr04.getDistance())
        	if (distance <=20):
			print( " dis : "), distance
                	pz.stop()
                	pz.spinRight(100)
                	time.sleep(1.1)
                	pz.stop()
                	pz.reverse(100)
                	time.sleep(0.8)
                	pz.stop()
                	pz.spinLeft(100)
                	time.sleep(1.2)
                	pz.stop()
                	pz.reverse(100)
                	time.sleep(1.2)
                	pz.stop()
                	pz.spinLeft(100)
                	time.sleep(1.2)
                	pz.stop()
			pz.reverse(100)
			time.sleep(1)
			pz.stop()
		else:
			pz.reverse(100)

except KeyboardInterrupt:
	print "Au revoir Mr"

finally:
	hcsr04.cleanup()
	pz.cleanup()
