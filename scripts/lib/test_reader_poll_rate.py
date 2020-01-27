# pylint: disable=import-error
# pylint: disable=undefined-variable
# pylint: disable=relative-beyond-top-level
import unittest
import reader as re

class TestReaderPollRate(unittest.TestCase):

    def test_run_function_works(self):
        # Arrange
        r = re.Reader()

        # Act
        r.run(10)

        # Assert
        self.assertTrue(r.iterations == 10)
    
    def test_polling_delay_increment_mismatch(self):
        with self.assertRaises(ValueError):
            re.Reader(polling_delay_inc=0.5, polling_delay_init=0.6)

    def test_polling_delay_increment_mismatch_2(self):
        with self.assertRaises(ValueError):
            re.Reader(polling_delay_max=1 ,polling_delay_init=1, polling_delay_inc=0.3)

    def test_polling_delay_increment_correct_input(self):
        try:
            re.Reader(polling_delay_max=1 ,polling_delay_min=0, polling_delay_init=1, polling_delay_inc=0.25)
        except:
            self.fail()

    def test_polling_delay_decreases(self):
        # Arrange
        l = [i for i in range(0, 100, 5)]
        p = iter(l)
        r = re.Reader(poller=lambda: next(p))
        init_delay = r.polling_delay

        # Act
        r.run(20)

        # Assert
        self.assertTrue(init_delay > r.polling_delay)
        self.assertTrue(r.iterations == 20)

    def test_polling_delay_increases(self):
        # Arrange
        r = re.Reader()
        l = [50 for i in range(20)]
        p = iter(l)
        r = re.Reader(poller=lambda: next(p))
        init_delay = r.polling_delay

        # Act
        r.run(20)

        # Assert
        self.assertTrue(r.polling_delay > init_delay)
        self.assertTrue(r.iterations == 20)

    def test_polling_delay_fluctuates(self):
        # Arrange
        l = [i for i in range(0, 100, 5)]
        l.extend([100 for i in range(20)])
        l.extend([i for i in range(100, 0, -5)])
        l.extend([0 for i in range(100)])
        p = iter(l)
        r = re.Reader(poller=lambda:next(p))
        prev_delay = r.polling_delay

        # Act / Assert
        r.run(20)
        self.assertTrue(prev_delay > r.polling_delay)
        prev_delay = r.polling_delay
        r.run(20)
        self.assertTrue(r.polling_delay > prev_delay)
        prev_delay = r.polling_delay
        r.run(20)
        self.assertTrue(prev_delay > r.polling_delay)

        self.assertTrue(r.iterations == 60)

    def test_false_values_dont_affect(self):
        l = [75 for i in range(10)]
        l.extend([25 for i in range(10)])
        l.extend([100 for i in range(10)])
        l.extend([150 for i in range(10)])
        p = iter(l)
        r = re.Reader(poller=lambda:next(p), unit_value_min=50, unit_value_max=100)

        # Act / Assert
        r.run(10)

        prev_delay = r.polling_delay
        r.run(10)
        self.assertTrue(prev_delay == r.polling_delay)

        prev_delay = r.polling_delay
        r.run(10)
        self.assertTrue(prev_delay != r.polling_delay)

        prev_delay = r.polling_delay
        r.run(10)
        self.assertTrue(prev_delay == r.polling_delay)

        self.assertTrue(r.iterations == 40)
    
    def test_poller_disconnect(self):
        l = [100 for i in range(10)]
        l.extend([75 for i in range(10)])
        l.extend([0 for i in range(30)])
        p = iter(l)

        r = re.Reader(poller=lambda:next(p))

        with self.assertRaises(re.DisconnectErrorException):
            r.run(50)

if __name__ == '__main__':
    unittest.main()