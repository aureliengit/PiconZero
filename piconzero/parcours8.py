

import time
import piconzero as pz
import hcsr04

pz.setInputConfig(2,0)
pz.setInputConfig(3,0)
pz.init()
hcsr04.init()
speed = 100
try:
	while True:
		if ((pz.readInput(2)!=1) and (pz.readInput(3)==1)):
			pz.stop()
			time.sleep(0.09)
			pz.spinRight(95)
			time.sleep(0.09)
			pz.spinLeft(100)
			time.sleep(0.15)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)!=1)):
			pz.stop()
			time.sleep(0.09)
			pz.spinLeft(95)
			time.sleep(0.09)
			pz.spinRight(100)
			time.sleep(0.15)
		elif((pz.readInput(2)==1) and (pz.readInput(3)==1)):
			pz.reverse(speed)
		else:
			pz.reverse(speed)
except KeyboardInterrupt:
	print "Au revoir"
finally:
	pz.cleanup()
