from utime import sleep
import _thread

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

		self.grace_period_is_active = False
		self.cooldown_is_active_ = False

	def strike(self):
		if(self.grace_period_is_active == False):
			self.grace_period_is_active = True
			self.strike_count = self.strike_count + 1
			_thread.start_new_thread(self.grace_period_timer, (1,))

		if(self.DEBUG): print("strike_count is now", self.strike_count)


	def grace_period_timer(self, args):
		sleep(self.GRACE_PERIOD)

		if(self.DEBUG): print("Exiting grace period")

		self.grace_period_is_active = False

	def cooldown_timer(self):
		sleep(self.GRACE_PERIOD)


