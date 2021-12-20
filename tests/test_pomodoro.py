import unittest
from pomodoro import Pomodoro


class PomodoroTestCase(unittest.TestCase):
    def test_app_is_initialized(self):
        app = Pomodoro()
        self.assertTrue(app.title())
