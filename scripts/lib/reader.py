def default_poller(start = 0, inc = 1):
	x = start
	while True:
		yield x
		x += inc

def default_transmitter(msg):
	return

class Reader:
	def __init__(self, 
	poller = lambda: next(default_poller),
	transmitter = default_transmitter,

	unit_value_max = 100,
	unit_value_min = 0,

	polling_delay_init = 1,
	polling_delay_max = 3,
	polling_delay_min = 0.5,
	polling_delay_inc = 0.5

	
	):
		self.poller = poller
		self.transmitter = transmitter
		# Defines the range of units that can be polled
		# while still considered normal within the
		# context of the application
		self.MAX_UNIT_VALUE = unit_value_max
		self.MIN_UNIT_VALUE = unit_value_min

		# Defines the range of values the delay
		# between pollings can have and the 
		# increment when increasing/decreasing it
		self.polling_delay = polling_delay_init
		self.POLLING_DELAY_MAX = polling_delay_max
		self.POLLING_DELAY_MIN = polling_delay_min
		self.POLLING_DELAY_INC = polling_delay_inc

		self.polling_delay_setup_check()

		self.iterations = 0

	def polling_delay_setup_check(self):
		if (self.polling_delay <= 0):
			raise ValueError("Initial polling delay cannot be zero or less")

		if (self.POLLING_DELAY_MAX < self.polling_delay):
			raise ValueError("Initial max value for polling delay cannot be less than the initial delay value")

		if (self.POLLING_DELAY_MIN > self.polling_delay):
			raise ValueError("Initial minimum value for polling delay cannot be more than the initial delay value")
		
		if (self.POLLING_DELAY_MIN < 0):
			raise ValueError("Initial minimum value for polling delay cannot be less than zero")

		if (self.POLLING_DELAY_INC < 0):
			raise ValueError("Initial increment value for polling delay cannot be less than zero")
		
		diff = self.POLLING_DELAY_MAX - self.POLLING_DELAY_MIN
		if (diff % self.POLLING_DELAY_INC != 0):
			raise ValueError("Initial increment value for polling delay must be divisible by the difference between the max and min values of the polling delay")

		diff = self.polling_delay - self.POLLING_DELAY_MIN
		if (diff % self.POLLING_DELAY_INC != 0):
			raise ValueError("Distance between initial polling delay and mininimum polling delay must be divisible by polling delay increment")

		diff = self.POLLING_DELAY_MAX - self.polling_delay
		if (diff % self.POLLING_DELAY_INC != 0):
			raise ValueError("Distance between initial polling delay and maximum polling delay must be divisible by polling delay increment")

	def run(self, iterations = 1):
		for _ in range(iterations):
			self.iterations += 1
			value = self.poller()
			if(self.verify_data(value)):
				self.adjust_reading_rate(value)
			
	def verify_data(self, value):
		if ((value <= self.MAX_UNIT_VALUE) and (value >= self.MIN_UNIT_VALUE)):
			return True
		return False
	
	def adjust_reading_rate(self, value):
		return




