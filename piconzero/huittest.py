

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
			time.sleep(1)
			pz.spinLeft(75)
			time.sleep(1)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)!=1)):
			pz.stop()
			time.sleep(1)
			pz.spinRight(75)
			time.sleep(1)
		elif ((pz.readInput(2)==1) and (pz.readInput (3)==1)):
			pz.stop()
			time.sleep(1)
			pz.spinLeft(75)
			pz.reverse(45)
except KeyboardInterrupt:
	print "Au revoir"
finally:
	pz.cleanup()
	hcsr04.cleanup()
