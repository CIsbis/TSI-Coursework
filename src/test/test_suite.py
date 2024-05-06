import unittest

from src.test.LoginMock import LoginMock
from src.test.RegisterMock import RegisterMock


def test_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(RegisterMock))
    suite.addTest(loader.loadTestsFromTestCase(LoginMock))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
