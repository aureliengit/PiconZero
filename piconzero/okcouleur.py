import piconzero as pz
import time

pz.setInputConfig (2,0)
pz.init()
try:
	while True:

		test = pz.readInput(2)
		
		if pz.readInput(2):
			print "IR droite : Black /test ",test 
			time.sleep(1)
		else:
			print "IR droite : White /test",test
			time.sleep(1)
		if pz.readInput(3):
			print "IR gauche : Black"
			time.sleep(1)
		else:
			print "IR gauche : White"
			time.sleep(1)

finally:
	pz.cleanup()
