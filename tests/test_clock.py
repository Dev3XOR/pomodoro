import unittest


class DummyTestCase(unittest.TestCase):
    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 4)
