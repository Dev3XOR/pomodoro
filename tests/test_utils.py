import unittest
from pomodoro import format_time, validate_number


class UtilsTestCase(unittest.TestCase):
    def test_time_format(self):
        self.assertEqual(format_time(0), "0:00:00")
        self.assertEqual(format_time(10), "0:00:10")
        self.assertEqual(format_time(75), "0:01:15")

    def test_number_validation(self):
        self.assertTrue(validate_number("10"))
        self.assertFalse(validate_number("1.1"))
        self.assertFalse(validate_number("False"))
