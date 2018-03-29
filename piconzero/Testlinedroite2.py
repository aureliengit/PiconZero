import piconzero as pz
import time

import sys
import tty
import termios

pz.setInputConfig (2,0)
pz.setInputConfig (3,0)
pz.init()
try:
	while True:

		test = pz.readInput(2)

		if (pz.readInput(2) != 1 and pz.readInput(3) != 1):
			pz.reverse(40)
			print "valeur : test",test

		elif (pz.readInput(2) != 1 and pz.readInput(3) ==1):
			pz.stop()
			pz.spinLeft(100)
			pz.spinRight(30)

		elif (pz.readInput(3) != 1 and pz.readInput(2) ==1):
			pz.stop()
			pz.spinRight(100)
			pz.spinLeft(30)


finally:
	pz.cleanup()

