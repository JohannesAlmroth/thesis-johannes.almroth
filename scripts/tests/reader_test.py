# pylint: disable=import-error
# pylint: disable=relative-beyond-top-level
import unittest
from ..lib.reader import Reader
from ..lib.data_generator import *


class ReaderTest(unittest.TestCase):

    def test_run_function_works(self):
        r = Reader()
        r.run(10)
        self.assertEquals(r.iterations, 10)

    def test_polling_delay_stays_the_same(self):
        x = (i for i in iter(int(), 1))
        p = lambda: next(x)
        r = Reader(poller = p)
        delay = r.polling_delay
        for _ in range(10):
            r.run()
            self.assertEquals(r.polling_delay, delay)

    def test_polling_delay_increases(self):
        self.assertEquals(1, 10)

    def test_polling_delay_decreases(self):
        self.assertEquals(1, 10)

    def test_polling_delay_fluctuates(self):
        self.assertEquals(1, 10)

    def test_polling_delay_stabilizes(self):
        self.assertEquals(1, 10)

    def test_can_detect_false_values(self):
        self.assertEquals(1, 10)

if __name__ == '__main__':
    unittest.main()