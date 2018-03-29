import piconzero as pz
import time

pz.setInputConfig (2,0)
pz.init()
try:
	while True:

		if pz.readInput(2):
			print "IR droite : Black"
			pz.stop()
			time.sleep(1)
			break
		else:
			print "IR droite : White"
			time.sleep(1)
			pz.reverse(35)

		if pz.readInput(3):
			print "IR gauche : Black"
			pz.stop()
			time.sleep(1)
			break
		else:
			print "IR gauche : White"
			pz.reverse(35)
			time.sleep(1)
except KeyboardInterrupt:
	print
finally:
	pz.cleanup()
