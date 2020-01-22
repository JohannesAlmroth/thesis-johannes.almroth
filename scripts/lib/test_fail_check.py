# pylint: disable=import-error
# pylint: disable=undefined-variable
# pylint: disable=relative-beyond-top-level
import unittest
import fail_tracker as f
from utime import sleep

class TestFailTracker(unittest.TestCase):

	def test_runs(self):
		ft = f.Fail_tracker()
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
	
	def test_grace_period_prevents_strikes(self):
		ft = f.Fail_tracker(grace_period=1)
		ft.strike()
		ft.strike()
		self.assertTrue(ft.strike_count == 1)

	def test_grace_period_start_allowing_strikes_again(self):
		ft = f.Fail_tracker(grace_period=0.5)
		ft.strike()
		sleep(1)
		ft.strike()
		self.assertTrue(ft.strike_count == 2)

	def test_cooldown_removes_strikes(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.3)
		self.assertTrue(ft.strike_count == 0)

	def test_cooldown_allows_strikes(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.3)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)

	def test_cooldown_allows_fluctuating_strikes(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.5)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 2)
		sleep(0.5)
		self.assertTrue(ft.strike_count == 1)

	def test_max_strikes_error_assertion(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=2)
		for i in range(5):
			ft.strike()
			self.assertTrue(ft.strike_count == (i + 1))
		with self.assertRaises(FailureRateError):
			ft.strike()


if __name__ == '__main__':
    unittest.main()