# pylint: disable=import-error
# pylint: disable=undefined-variable
# pylint: disable=relative-beyond-top-level
import unittest
import reader as re

class TestreaderMethods(unittest.TestCase):

    def test_run_function_works(self):
        r = re.Reader()
        r.run(10)
        self.assertTrue(r.iterations == 10)
    
    def test_polling_delay_increment_mismatch(self):
        with self.assertRaises(ValueError):
            r = re.Reader(polling_delay_inc=0.5, polling_delay_init=0.6)

    def test_polling_delay_increment_mismatch_2(self):
        with self.assertRaises(ValueError):
            r = re.Reader(polling_delay_max=1 ,polling_delay_init=1, polling_delay_inc=0.3)

    def test_polling_delay_increment_correct_input(self):
        try:
            r = re.Reader(polling_delay_max=1 ,polling_delay_min=0, polling_delay_init=1, polling_delay_inc=0.25)
        except ValueError:
            self.fail()

    def test_polling_delay_stays_the_same(self):
        x = (i for i in iter(int(), 1))
        r = re.Reader(poller = lambda: next(x))
        delay = r.polling_delay
        for _ in range(10):
            r.run()
            self.assertEqual(r.polling_delay, delay)

    def test_polling_delay_decreases(self):
        l = []
        r = re.Reader(poller=lambda: next(p))
        init_delay = r.polling_delay
        r.run(20)
        self.assertTrue(init_delay > r.polling_delay)

    def test_polling_delay_increases(self):
        r = re.Reader()
        l = [].append([50 for i in range(20)])
        p = iter(l)
        r = re.Reader(poller=lambda: next(p))
        init_delay = r.polling_delay
        r.run(20)
        self.assertTrue(r.polling_delay > init_delay)

    def test_polling_delay_fluctuates(self):
        l = []
        l = add_linear_data(l, 20, 0, 100)
        l = add_linear_data(l, 20, 75, 25)
        l = add_linear_data(l, 20, 50, 150)
        r = re.Reader()
        delay = r.polling_delay
        r.run(20)
        self.assertTrue(delay > r.polling_delay)
        delay = r.polling_delay
        r.run(20)
        self.assertTrue(r.polling_delay > delay)
        delay = r.polling_delay
        r.run(20)
        self.assertTrue(delay > r.polling_delay)

    # def test_can_detect_false_values(self):
    #     l = []
    #     l = add_linear_data(l, 20, 120, 100)
    #     r = Reader(unit_value_max=100, unit_value_min=75)
    #     self.assertEquals()

if __name__ == '__main__':
    unittest.main()