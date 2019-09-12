#pylint: disable=no-member

import pycom
import time

def blink():
	pycom.heartbeat(False)
	for _ in range(100): # stop after 100 cycles
		pycom.rgbled(0x007f00) # green
		time.sleep(1)
		pycom.rgbled(0x7f7f00) # yellow
		time.sleep(1)
		pycom.rgbled(0x7f0000) # red
		time.sleep(1)