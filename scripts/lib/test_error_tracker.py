# pylint: disable=import-error
# pylint: disable=undefined-variable
# pylint: disable=relative-beyond-top-level
import unittest
import error_tracker as f
from utime import sleep
import _thread

class TestErrorTracker(unittest.TestCase):

	def test_runs(self):
		ft = f.Error_tracker()
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)
	
	def test_grace_period_prevents_strikes(self):
		ft = f.Error_tracker(grace_period=1)
		ft.error_occurred()
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)

	def test_grace_period_start_allowing_strikes_again(self):
		ft = f.Error_tracker(grace_period=0.5)
		ft.error_occurred()
		sleep(1)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 2)

	def test_cooldown_removes_strikes(self):
		ft = f.Error_tracker(grace_period=0.1, cooldown=0.1)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)
		sleep(0.3)
		self.assertTrue(ft.error_count == 0)

	def test_cooldown_allows_strikes(self):
		ft = f.Error_tracker(grace_period=0.1, cooldown=0.1)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)
		sleep(0.3)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)

	def test_cooldown_allows_fluctuating_strikes(self):
		ft = f.Error_tracker(grace_period=0.1, cooldown=0.5)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 1)
		sleep(0.2)
		ft.error_occurred()
		self.assertTrue(ft.error_count == 2)
		sleep(3)
		self.assertTrue(ft.error_count == 1)

	def test_max_strikes_error_assertion(self):
		ft = f.Error_tracker(max_allowed_errors=10, grace_period=0.1, cooldown=1)
		with self.assertRaises(f.MaxErrorException):
			for i in range(11):
				sleep(0.2)
				ft.error_occurred()




if __name__ == '__main__':
    unittest.main()