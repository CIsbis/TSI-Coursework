import unittest
from src.main import welcome
from src.test.LogInStub import LogInStub


class LogInStubTest(unittest.TestCase):

    def test_verified(self):
        LogIn = LogInStub()
        verified = welcome
        self.assertTrue(verified)


