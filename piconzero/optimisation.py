#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import piconzero as pz
import hcsr04

pz.setInputConfig(2,0)
pz.setInputConfig(3,0)
pz.init()
hcsr04.init()
speed = 70
noir = 0
try:
	while True:
		if ((pz.readInput(2)!=1) and (pz.readInput(3)==1)):
			pz.stop()
			time.sleep(0.15)
			pz.spinLeft(100)
			time.sleep(0.25)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)!=1)):
			pz.stop()
			time.sleep(0.15)
			pz.spinRight(100)
			time.sleep(0.25)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)==1)):
			print "noir avant",noir
			noir+=1
			print "noir après",noir
			if (noir==1):
				pz.stop()
				pz.spinRight(100)
				time.sleep(1.7)
				pz.reverse(speed)
				time.sleep(1.5)
				pz.spinRight(100)
				time.sleep(1.7)
			elif ( noir == 2):
				pz.stop()
				break
			else :
				pz.stop()
				break
		else:
			pz.reverse(speed)
except KeyboardInterrupt:
	print "Au revoir"
finally:
	pz.cleanup()
	hcsr04.cleanup()
