import unittest
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
