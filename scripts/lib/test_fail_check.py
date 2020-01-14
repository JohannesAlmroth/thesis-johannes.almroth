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
	
	def test_grace_period_1(self):
		ft = f.Fail_tracker()
		ft.strike()
		ft.strike()
		self.assertTrue(ft.strike_count == 1)

	def test_grace_period_2(self):
		ft = f.Fail_tracker(grace_period=0.1)
		ft.strike()
		sleep(0.2)
		ft.strike()
		self.assertTrue(ft.strike_count == 2)

	def test_cooldown_1(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.3)
		self.assertTrue(ft.strike_count == 0)

	def test_cooldown_2(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.3)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)

	def test_cooldown_3(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=0.5)
		ft.strike()
		self.assertTrue(ft.strike_count == 1)
		sleep(0.1)
		ft.strike()
		self.assertTrue(ft.strike_count == 2)
		sleep(0.5)
		self.assertTrue(ft.strike_count == 1)

	def test_max_strikes(self):
		ft = f.Fail_tracker(grace_period=0.1, cooldown=2)
		for i in range(5):
			ft.strike()
			self.assertTrue(ft.strike_count == (i + 1))
		with self.assertRaises(FailureRateError):
			ft.strike()


if __name__ == '__main__':
    unittest.main()