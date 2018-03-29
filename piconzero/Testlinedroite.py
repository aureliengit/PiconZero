import piconzero as pz
import time


pz.setInputConfig (2,0)
pz.setInputConfig (3,0)
pz.init()

try:
	while True:

		test = pz.readInput(2)

		if (pz.readInput(2) != 1 and pz.readInput(3) != 1):
			pz.reverse(100)

		else:
			pz.reverse(100)
finally:
	pz.cleanup()

