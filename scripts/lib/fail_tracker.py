class Fail_tracker:
	def __init__(self,
	grace_period = 1,
	cooldown = 1,
	max_allowed_strikes = 10,
	
	debug = False):
		self.GRACE_PERIOD = grace_period
		self.COOLDOWN = cooldown
		self.MAX_ALLOWED_STRIKES = max_allowed_strikes
		self.strike_count = 0
		self.DEBUG = debug

	def strike(self):
		self.strike_count = self.strike_count + 1
		if(self.DEBUG): print("strike_count is now", self.strike_count)