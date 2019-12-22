def default_poller(start = 0, inc = 1):
	x = start
	while True:
		yield x
		x += inc

def default_transmitter(msg):
	return

class Reader:
	def __init__(self, 
	poller = default_poller(), 
	transmitter = default_transmitter, 
	max_unit_value = 200,
	min_unit_value = 0,
	max_polling_delay = 1,
	min_polling_delay = 0.5,
	polling_delay_inc = 0.5
	):
		# Defines the range of units that can be polled
		# while still considered normal within the
		# context of the application
		self.MAX_UNIT_VALUE = max_unit_value
		self.MIN_UNIT_VALUE = min_unit_value

		# Defines the range of values the delay
		# between pollings can have and the 
		# increment when increasing/decreasing it
		self.MAX_POLLING_DELAY = max_polling_delay
		self.MIN_POLLING_DELAY = min_polling_delay
		self.POLLING_DELAY_INC = polling_delay_inc



