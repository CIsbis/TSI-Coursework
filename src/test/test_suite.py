import unittest

from src.test.LogIn_mock import TestLogIn
from src.test.Register_mock import TestRegister


def test_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestRegister))
    suite.addTest(loader.loadTestsFromTestCase(TestLogIn))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
