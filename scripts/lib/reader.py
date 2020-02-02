# pylint: disable=import-error
from utime import sleep

def generator(start = 0, inc = 1):
	x = start
	while True:
		yield x
		x += inc

gen = generator()

def default_poller():
	return next(gen)

def default_transmitter(*args):
	return

class DisconnectErrorException(Exception):
	pass

class Reader:
	def __init__(self, 
	testing = False,
	poller = default_poller,
	transmitter = default_transmitter,

	buffer_len = 10,

	unit_value_max = 100,
	unit_value_min = 0,

	polling_delay_init = 3,
	polling_delay_max = 5,
	polling_delay_min = 1,
	polling_delay_inc = 0.5,

	delta_treshold = 10,
	dc_treshold = 10,

	debug = False
	):
		self.DEBUG = debug
		self.TESTING = testing
		self.poller = poller
		self.transmitter = transmitter
		self.data_buffer = FIFO(buffer_len)
		self.DELTA_THRESHOLD = delta_treshold
		self.DC_THRESHOLD = dc_treshold
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
			if(not self.TESTING): sleep(self.polling_delay)

			self.iterations += 1
			value = self.poller()
			if(self.verify_data(value)):
				self.data_buffer.add(value)

				if self.DEBUG: print("Queue is", self.data_buffer.queue)
				
				self.dc_check()
				self.adjust_polling_rate()
				self.transmitter(value)

	def dc_check(self):
		if (self.data_buffer.maxlen == len(self.data_buffer.queue) and all(0.0 == x for x in self.data_buffer.queue)):
			raise DisconnectErrorException


	def verify_data(self, value):
		return (value <= self.MAX_UNIT_VALUE) and (value >= self.MIN_UNIT_VALUE)
	
	def adjust_polling_rate(self):
		delta = self.current_delta()
		if abs(delta) > self.DELTA_THRESHOLD:
			self.decrease_polling_delay()
		else:
			self.increase_polling_delay()

	def current_delta(self):
		if self.DEBUG: print("Queue is", self.data_buffer.queue)
		prev = self.data_buffer.queue[0]
		total_delta = 0
		for x in self.data_buffer.queue[1:]:
			new_delta = prev - x
			total_delta += new_delta
			prev = x

		if self.DEBUG: print("Current delta is", total_delta)
		
		return total_delta
	
	def increase_polling_delay(self):
		if self.polling_delay < self.POLLING_DELAY_MAX:
			new_polling_delay = self.polling_delay + self.POLLING_DELAY_INC
			
			if self.DEBUG: print("Increased the delay from ", self.polling_delay, "to", new_polling_delay)
			
			self.polling_delay = new_polling_delay 
		else: 
			if self.DEBUG: print("Already at max polling delay")


	def decrease_polling_delay(self):
		if self.polling_delay > self.POLLING_DELAY_MIN:
			new_polling_delay = self.polling_delay - self.POLLING_DELAY_INC
			
			if self.DEBUG: print("Decreased the delay from ", self.polling_delay, "to", new_polling_delay)
			
			self.polling_delay = new_polling_delay
		else: 
			if self.DEBUG: print("Already at min polling delay")

class FIFO:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.queue = []
    
    def add(self, value):
        self.queue.append(value)
        if len(self.queue) > self.maxlen:
            self.queue = self.queue[-self.maxlen:]


