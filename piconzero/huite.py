

import time
import piconzero as pz
import hcsr04

pz.setInputConfig(2,0)
pz.setInputConfig(3,0)
pz.init()
hcsr04.init()
speed = 75
i=0
try:
	while True:
		if ((pz.readInput(2)!=1) and (pz.readInput(3)==1)):
			pz.stop()
			time.sleep(0.1)
			pz.spinLeft(100)
			time.sleep(0.25)
		elif ((pz.readInput(2)!=1) and (pz.readInput(3)!=1)):
			pz.stop()
			time.sleep(0.1)
			pz.spinRight(100)
			time.sleep(0.25)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)!=1)):
			i=i+1
			if i%2==0:
				pz.stop()
				time.sleep(0.1)
				pz.spinLeft(100)
				time.sleep(0.25)
			else:
				pz.stop()
				time.sleep(0.1)
				pz.spinRight(100)
				time.sleep(0.25)
		else:
			pz.reverse(speed)
except KeyboardInterrupt:
	print "Au revoir"
finally:
	pz.cleanup()
	hcsr04.cleanup()
