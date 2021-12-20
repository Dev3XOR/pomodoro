import unittest
import time
from pomodoro import Clock


class ClockTestCase(unittest.TestCase):
    def test_clock_is_running(self):
        c = Clock()
        # Check if this will not throw any errors
        c.stop()
        self.assertFalse(c.running)
        c.start()
        self.assertTrue(c.running)
        c.stop()
        self.assertFalse(c.running)

    def test_clock_timeouts(self):
        c = Clock()
        c.set_timeout(10)
        self.assertEqual(c.get_timeout(), 10)

    def test_clock_interval(self):
        c = Clock(timeout=10)
        c.start()
        time.sleep(1)
        self.assertEqual(c.get_timeout(), 9)
