# pylint: disable=import-error
from utime import sleep
import _thread

class MaxErrorException(Exception):
	pass

class Error_tracker:
	def __init__(self,
	grace_period = 1,
	cooldown = 1,
	max_allowed_errors = 10,
	
	debug = False):
		self.GRACE_PERIOD = grace_period
		self.COOLDOWN = cooldown
		self.MAX_ALLOWED_ERRORS = max_allowed_errors
		self.error_count = 0
		self.DEBUG = debug

		self.grace_period_is_active = False
		self.cooldown_is_active = False
		self.cooldown_id = None

	def error_occurred(self):
		if(self.grace_period_is_active == False):
			if(self.error_count >= self.MAX_ALLOWED_ERRORS): raise MaxErrorException

			self.grace_period_is_active = True
			self.cooldown_is_active = False
			self.error_count += 1
			
			_thread.start_new_thread(self.grace_period_timer, (1,))

		if(self.DEBUG): print("error_count is now", self.error_count)


	def grace_period_timer(self, args):
		sleep(self.GRACE_PERIOD)

		if(self.DEBUG): print("Exiting grace period")

		self.grace_period_is_active = False
		self.cooldown_timer()

	def cooldown_timer(self):
		self.cooldown_id = _thread.get_ident()
		self.cooldown_is_active = True
		sleep(self.COOLDOWN)
		
		if(self.cooldown_is_active and 
		not self.grace_period_is_active and
		self.cooldown_id == _thread.get_ident()):

			self.error_count -= 1
			if(self.DEBUG): print("Cooldown successful")
			self.cooldown_is_active = False
