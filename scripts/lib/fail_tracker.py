class Fail_tracker:
	def init(self,
	grace_period = 1,
	cooldown = 1,
	max_allowed_strikes = 10):
		self.GRACE_PERIOD = grace_period
		self.COOLDOWN = cooldown
		self.MAX_ALLOWED_STRIKES = max_allowed_strikes
		self.strike_count = 0

	def strike(self):
		self.strike_count += 1